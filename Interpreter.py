from io import StringIO
from typing import Callable

import AiLangLib  # Init Import
from grammar.AiLangLexer import AiLangLexer
from antlr4 import TerminalNode
from grammar.AiLangParser import AiLangParser
from AiLangType import (
    BasicValType,
    NumType,
    DfType,
    DfItem,
    ListType,
    StrType,
    AiLangType,
)
from AiLangObj import AiLangObj
from AiLangFunc import AiLangFunc, FunctionSpace, MethodSpace
import pandas as pd
import copy
import utils


class BlockTree:

    def __init__(self, ctx, label=None, parent=None, isStart=True):
        self.children: list[BlockTree] = []
        self.parent = parent
        self.label = label
        self.ctx = ctx
        self.isStart = isStart
        self.level = 0 if parent is None else parent.level + 1

    def addChild(self, ctx, label) -> BlockTree:
        block = BlockTree(ctx, label, parent=self, isStart=False)
        self.children.append(block)
        return block

    def findLabel(self, label) -> BlockTree | None:
        if self.label == label:
            return self
        for child in self.children:
            if child.label == label:
                return child
            childReturn = child.findLabel(label)
            if childReturn:
                return childReturn

    def printTree(self, level=0) -> None:
        # Print current node with indentation based on its level
        if level == 0:
            print(self.label)
        else:
            print("├─" + "─" * level + str(self.label))
        # Recursively print children
        for child in self.children:
            child.printTree(level + 1)


class VariableStack:

    def __init__(self):
        self.stack: list[dict[int, AiLangObj]] = []
        self.pushContext()
        self.nextID: int = 0

    def _nextID(self) -> int:
        id = self.nextID
        self.nextID += 1
        return id

    def pushContext(self) -> None:
        if len(self.stack) == 0:
            self.stack.append({})
        else:
            self.stack.append(self.deepcopy())

    def pushFuncContext(self) -> None:
        if len(self.stack) == 0:
            raise ValueError("Stack is empty no function call can happen")
        self.stack.append({})

    def popContext(self) -> dict[int, AiLangObj]:
        return self.stack.pop()

    def getContext(self) -> dict[int, AiLangObj]:
        return self.stack[-1]

    def put(self, val: AiLangObj, key: AiLangObj | None = None) -> None:
        available: AiLangObj | list[AiLangObj] | None = None
        if key:
            available = self._get(key)
            if isinstance(available, list):
                raise NotImplementedError()
            if not available:
                key.getLast().set(val.val)
                self.getContext()[self._nextID()] = key
                return
        if isinstance(available, list):
            raise NotImplementedError()

        if available:
            available.set(val.val)
        else:
            self.getContext()[self._nextID()] = val

    def putReturn(self, val: AiLangObj) -> None:
        self.getContext()[-1] = val

    def _get(self, key: str | AiLangObj) -> AiLangObj | list[AiLangObj] | None:
        ctx = self.getContext()
        if isinstance(key, str):
            for _, obj in ctx.items():
                if obj.id == key:
                    return obj
            return
        if len(key.members) == 0:
            return self._get(key.id)
        else:
            result_obj = None
            for _, obj in ctx.items():
                if obj.id == key.getRoot().id:
                    result_obj = obj
            if result_obj is None:
                return

            key_cur = key
            cur = result_obj
            result = []

            def get_result():
                nonlocal key_cur, cur, result
                if len(key_cur.members) > 0:
                    memb = list(key_cur.members.values())
                    key_cur = memb[0]
                if isinstance(cur.val, DfType):
                    item = cur.getDFItemByID(key_cur.id)
                    if item:
                        result.append(item)
                        return
                    memb = list(key_cur.getParent().members.values())
                    vals = [DfItem(cur.val.get(), m.id) for m in memb]
                    objs = [AiLangObj(df.item, df) for df in vals]
                    [cur.setMember(obj) for obj in objs]
                    result += objs
                    return
                if key_cur.id in cur.members:
                    last_cur = cur
                    cur = cur.members[key_cur.id]
                    if len(cur.members) == 0:
                        result.append(cur)
                        cur = last_cur
                        get_result()
                    del last_cur.members[key_cur.id]
                else:
                    return

            get_result()

            if len(result) == 0:
                return None
            elif len(result) == 1:
                return result[0]
            else:
                return result

    def get(self, key: str | AiLangObj) -> AiLangObj | list[AiLangObj]:
        ret = self._get(key)
        if ret is None:
            raise ValueError("The key is not in the stack frame")
        return ret

    def deepcopy(self) -> dict:
        return copy.deepcopy(self.getContext())


class Interpreter:

    def __init__(self, ast: AiLangParser.ProgContext):
        self.ast = ast
        self.variableContextStack = VariableStack()
        self.blockTree = None
        self.lastLabel = None
        self.functions = FunctionSpace()
        self.methods = MethodSpace()

    def interp(self) -> None:
        if self.ast.children is None:
            raise ValueError()
        blocks = self.ast.getTypedRuleContexts(AiLangParser.Block_statContext)
        for block in blocks:
            self.constructBlockTree(block)
        funcDecls = self.ast.getTypedRuleContexts(AiLangParser.FunctionDefContext)
        for fd in funcDecls:
            self.evalFunctionDecl(fd)
        if self.blockTree is None:
            raise ValueError("Block Tree is Empty")
        self.evaluateBlocks()
        # self.blockTree.printTree()

    def evalFunctionDecl(self, funcDecl: AiLangParser.FunctionDefContext):
        fd = funcDecl.getTypedRuleContext(AiLangParser.Func_defContext, 0)
        if fd is None:
            raise ValueError()
        func = AiLangFunc.make(fd, self.ctxRunnerConstructer())
        self.functions.addFunc(func)

    def evaluateBlocks(self, blocks: BlockTree | None = None) -> None:
        blocks = blocks if blocks is not None else self.blockTree
        if blocks is None:
            raise ValueError("The block tree is not set cannot evaluate")
        # Evaluate all statemnts inside the ctx
        for ch in blocks.ctx.children:
            if not self.evaluate(ch):
                break
        if len(blocks.children) == 1:
            # If the block has only 1 child we shall skip the context push
            self.evaluateBlocks(blocks.children[0])
        else:
            # If the block has more thna 1 child we shoul duplicate state for each
            for block in blocks.children:
                self.variableContextStack.pushContext()
                self.evaluateBlocks(block)
                self.variableContextStack.popContext()

    def evalNonBlockContext(self, child: AiLangParser.BlockContext) -> bool:
        #!This evaluation uses the same VariableContext
        if child.children is None:
            raise ValueError()
        for ch in child.children:
            if isinstance(ch, (AiLangParser.StatContext, AiLangParser.ContextContext)):

                if not self.evaluate(ch):
                    return False
        return True

    def ctxRunnerConstructer(
        self,
    ) -> Callable[[AiLangParser.ContextContext], Callable[..., dict[int, AiLangObj]]]:
        def constructor(
            ctx: AiLangParser.ContextContext,
        ) -> Callable[..., dict[int, AiLangObj]]:
            def runner(*args):
                """
                Runner runs the lines of code in ctx and if there is a return
                it puts to the stack frame on address '-1'
                """
                self.variableContextStack.pushFuncContext()
                for arg in args:
                    if not isinstance(arg, AiLangObj):
                        continue
                    self.variableContextStack.put(arg)
                stats = ctx.getTypedRuleContexts(AiLangParser.StatContext)
                for stat in stats:
                    if not self.evaluate(stat):
                        break
                return self.variableContextStack.popContext()

            return runner

        return constructor

    def constructBlockTree(self, child: AiLangParser.Block_statContext) -> None:
        # TODO Add function definitions in this method
        if isinstance(child, AiLangParser.Block_statContext):
            if child.children is None:
                raise ValueError()
            for ch in child.children:
                if not isinstance(
                    ch,
                    (AiLangParser.Block2BlockContext, AiLangParser.Label2BlockContext),
                ):
                    raise ValueError()
                fromLabel, label, ctx = self.getBlockCtx(ch)
                # print(f"FromLabel: {fromLabel} Label: {label}")

                if self.blockTree is None:
                    if fromLabel:
                        raise ValueError("Start must be the first block")

                    self.blockTree = BlockTree(ctx, label)
                    self.lastLabel = self.blockTree
                else:
                    if fromLabel:
                        fromBlock = self.blockTree.findLabel(fromLabel)
                        if fromBlock is None:
                            raise ValueError()
                        self.lastLabel = fromBlock.addChild(ctx, label)
                    else:
                        if self.lastLabel is None:
                            raise ValueError()
                        self.lastLabel = self.lastLabel.addChild(ctx, label)

    def getBlockCtx(
        self, child: AiLangParser.Block2BlockContext | AiLangParser.Label2BlockContext
    ):
        if isinstance(child, AiLangParser.Block2BlockContext):
            label = child.getTypedRuleContext(AiLangParser.LabelContext, 0)
            if label:
                label = self.getFirstID(label)
            ctx = child.getTypedRuleContext(AiLangParser.ContextContext, 0)
            return None, label, ctx
        elif isinstance(child, AiLangParser.Label2BlockContext):
            fromLabel = child.getTypedRuleContext(AiLangParser.LabelContext, 0)
            label = child.getTypedRuleContext(AiLangParser.LabelContext, 1)
            ctx = child.getTypedRuleContext(AiLangParser.ContextContext, 0)
            if fromLabel:
                fromLabel = self.getFirstID(fromLabel)
            if label:
                label = self.getFirstID(label)
            return fromLabel, label, ctx

    def evaluate(
        self, child: AiLangParser.StatContext | AiLangParser.ContextContext
    ) -> bool:
        """
        Returns True on normal evaluation adn returns False if there was a return stat
        """
        if isinstance(child, (AiLangParser.StatContext, AiLangParser.ContextContext)):
            if child.children is None:
                raise ValueError()
            for ch in child.children:
                if isinstance(ch, TerminalNode):
                    continue
                elif isinstance(ch, AiLangParser.ExprContext):
                    exprRet = self.evalExpr(ch)
                    # print(exprRet.get())
                elif isinstance(ch, AiLangParser.FromToDataContext):
                    self.evalFrom2Data(ch)
                elif isinstance(ch, AiLangParser.DoIfElseContext):
                    self.evalDoIfElse(ch)
                elif isinstance(ch, AiLangParser.AssignmentContext):
                    self.evalAssignment(ch)
                elif isinstance(ch, (AiLangParser.Ref_opContext)):
                    self.evalReference(ch)
                elif isinstance(ch, AiLangParser.RetContext):
                    self.evalRet(ch)
                    return False
                else:
                    raise ValueError(f"Type {type(ch)} is tried to be evaluated")
            return True
        return True

    def evalRet(self, child: AiLangParser.RetContext) -> None:
        if isinstance(child, AiLangParser.NoneReturnContext):
            return
        elif isinstance(child, AiLangParser.ExprReturnContext):
            expr = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
            if expr is None:
                raise ValueError()
            val = self.evalExpr(expr)
            self.variableContextStack.putReturn(AiLangObj("Return", val))

    def evalFrom2Data(self, child: AiLangParser.FromToDataContext) -> None:
        strCtx = child.getTypedRuleContext(AiLangParser.StrContext, 0)
        if strCtx is None:
            raise ValueError()
        fileStr = StrType.make(strCtx).get()
        id = self.getFirstID(child)

        data = self.transformFile2Data(fileStr)
        data = DfType(data)
        obj = AiLangObj(id, data)

        self.variableContextStack.put(obj)

    def transformFile2Data(self, fileName):
        return pd.DataFrame()  # TODO: implement me

    def evalDoIfElse(self, child: AiLangParser.DoIfElseContext) -> bool:
        # Do Block mandatory
        doCtx = child.getTypedRuleContext(AiLangParser.ContextContext, 0)
        # If Block mandatory
        ifBCtx = child.getTypedRuleContext(AiLangParser.Bool_contextContext, 0)
        # Else Block optional
        elseCtx = child.getTypedRuleContext(AiLangParser.ContextContext, 1)
        parent = self

        class DoIfElse:
            def __init__(self, doCtx, ifBCtx, elseCtx):
                self.doCtx = doCtx
                self.ifBCtx: AiLangParser.Bool_contextContext = ifBCtx
                self.elseCtx = elseCtx

            def eval(self) -> bool:
                if self.resolveIf():
                    ctx = self.doCtx
                elif self.elseCtx is not None:
                    ctx = self.elseCtx
                else:
                    ctx = None

                if ctx is None:
                    return True

                return parent.evalNonBlockContext(ctx)

            def resolveIf(self):
                bool_groups = self.ifBCtx.getChildren(
                    lambda x: isinstance(x, AiLangParser.Bool_groupContext)
                )

                results = []
                for bool_group in bool_groups:
                    if isinstance(bool_group, AiLangParser.Bool_groupContext):
                        results.append(parent.evalBoolGroup(bool_group))

                acc = False
                for result in results:
                    acc = acc or result
                return acc

        return DoIfElse(doCtx, ifBCtx, elseCtx).eval()

    def evalBoolGroup(self, child: AiLangParser.Bool_groupContext) -> bool:

        statements = list(
            child.getChildren(lambda x: isinstance(x, AiLangParser.Bool_statContext))
        )
        ops = list(child.getChildren(lambda x: isinstance(x, TerminalNode)))

        if len(statements) > 1 and len(ops) > 0:
            results = [
                (
                    self.evalBoolStat(stat)
                    if isinstance(stat, AiLangParser.Bool_statContext)
                    else None
                )
                for stat in statements
            ]
            ops = [utils.getTerminalSymbol(op) for op in ops]
            ops = [self.getPythonOp(op) for op in ops]
        else:
            if not isinstance(statements[0], AiLangParser.Bool_statContext):
                raise ValueError()
            return self.evalBoolStat(statements[0])

        bool_str = ""
        with StringIO() as builder:
            for result in results:
                builder.write(str(result))
                builder.write(" ")
                if len(ops) > 0:
                    builder.write(str(ops.pop(0)))
            bool_str = builder.getvalue()

        return bool(eval(bool_str))

    def getPythonOp(self, op):
        return op  # TODO: ADD ailang bool translation to python here

    def evalBoolStat(self, child: AiLangParser.Bool_statContext) -> bool:
        val1 = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
        val2 = child.getTypedRuleContext(AiLangParser.ExprContext, 1)
        if not (val1 and val2):
            raise ValueError()
        val1 = self.evalExpr(val1).get()
        val2 = self.evalExpr(val2).get()

        op = self.getPythonOp(
            utils.getTerminalSymbol(
                child.getToken(AiLangLexer.BOOL_OP, 0)
            )  # Gets the first Terminals Text
        )

        # TODO: resolve other bool operations like DataFrame operations here

        return bool(
            eval(
                f"x {op} y",
                {
                    "x": val1,
                    "y": val2,
                },
            )
        )

    def evalExpr(self, child: AiLangParser.ExprContext) -> AiLangType:

        if isinstance(child, AiLangParser.MathOpContext):
            return self.evalMathOp(child)
        if isinstance(child, AiLangParser.MethodCallContext):
            return self.evalMethod(child)
        if isinstance(child, AiLangParser.GroupContext):
            exprCtx = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
            if exprCtx is None:
                raise ValueError()
            return self.evalExpr(exprCtx)

        ch = child.getChild(0)
        if isinstance(ch, AiLangParser.Basic_valContext):
            return BasicValType.make(ch)
        elif isinstance(ch, AiLangParser.DfContext):
            return DfType.make(ch)
        elif isinstance(ch, AiLangParser.ListContext):
            chch = ch.getChild(0)
            if isinstance(chch, AiLangParser.Generic_listContext):
                return self.getGenericList(chch)
            return ListType.make(chch)
        elif isinstance(ch, AiLangParser.AssignableContext):
            return self.evalIdVal(ch).get()
        elif isinstance(ch, AiLangParser.FuncContext):
            return self.evalFunc(ch)

        raise NotADirectoryError()

    def getGenericList(self, child: AiLangParser.Generic_listContext) -> ListType:
        l_val = []
        for ch in child.getTypedRuleContexts(AiLangParser.ExprContext):
            l_val.append(self.evalExpr(ch))
        return ListType(l_val)

    def evalMethod(self, child: AiLangParser.MethodCallContext) -> AiLangType:
        obj = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
        if obj is None:
            raise ValueError()
        obj = obj.getTypedRuleContext(AiLangParser.AssignableContext, 0)
        if obj is None:
            raise ValueError()
        obj = self.evalAssignable(obj)
        methodID = obj.getLast().id
        obj.killMembers()
        parent = self.variableContextStack.get(obj)
        argList = child.getTypedRuleContext(AiLangParser.Arg_listContext, 0)
        if argList is None:
            raise ValueError()
        args = self.evalArgsList(argList)
        if isinstance(parent, list):
            raise NotImplementedError()
        if MethodSpace().hasMethod(type(parent.val), methodID):
            return MethodSpace().call(parent, methodID, args).get()
        raise ValueError(
            f"Method {methodID} is not available for type {str(type(parent.val))}"
        )

    def evalArgsList(self, child: AiLangParser.Arg_listContext) -> list[AiLangObj]:
        evaluated = []
        for arg in child.getTypedRuleContexts(AiLangParser.ArgContext):
            evaluated.append(self.evalArg(arg))
        return evaluated

    def evalArg(self, child: AiLangParser.ArgContext) -> AiLangObj:
        if isinstance(child, AiLangParser.NamedArgContext):
            namedArg = child.getTypedRuleContext(AiLangParser.Named_argContext, 0)
            if namedArg is None:
                raise ValueError()
            return self.evalNamedArg(namedArg)
        elif isinstance(child, AiLangParser.ExprArgContext):
            expr = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
            if expr is None:
                raise ValueError()
            return AiLangObj("", self.evalExpr(expr))

        raise ValueError()

    def evalNamedArg(self, child: AiLangParser.Named_argContext) -> AiLangObj:
        id = child.getTypedRuleContext(AiLangParser.IdContext, 0)
        if id is None:
            raise ValueError()
        expr = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
        if expr is None:
            raise ValueError()
        id = utils.getTerminalSymbol(id)
        val = self.evalExpr(expr)
        return AiLangObj(id, val)

    def evalFunc(self, child: AiLangParser.FuncContext) -> AiLangType:
        ids = utils.getAllIds(child)
        if len(ids) != 1:
            raise ValueError()
        funcId = ids[0]

        argList = child.getTypedRuleContext(AiLangParser.Arg_listContext, 0)
        if argList is None:
            argList = []
        else:
            argList = self.evalArgsList(argList)

        if FunctionSpace().hasFunc(funcId):
            return FunctionSpace().call(funcId, argList).get()

        raise ValueError(f"Function {funcId} is not in FunctionSpace")

    def evalMathOp(self, child: AiLangParser.MathOpContext):

        expr1, expr2 = child.getTypedRuleContext(
            AiLangParser.ExprContext, 0
        ), child.getTypedRuleContext(AiLangParser.ExprContext, 1)
        if not (expr1 and expr2):
            raise ValueError()

        lop = self.evalExpr(expr1)
        opToken = utils.getTerminalSymbol(child.getChild(1))
        rop = self.evalExpr(expr2)

        if isinstance(lop, NumType) and isinstance(rop, NumType):
            num = eval(
                f"a {opToken} b",
                locals={
                    "a": lop.get(),
                    "b": rop.get(),
                },
            )
            return NumType(num, int if isinstance(num, int) else float)
        raise ValueError()

    def evalIdVal(self, child: AiLangParser.AssignableContext) -> AiLangObj:
        obj = AiLangObj.make(child)
        val = self.variableContextStack.get(obj)
        if isinstance(val, list):
            raise NotImplementedError()
        return val

    def getFirstID(self, child):
        return utils.getTerminalSymbol(child.getChild(0, ttype=AiLangParser.IdContext))

    def evalAssignable(self, child: AiLangParser.AssignableContext):
        return AiLangObj.make(child)

    def evalAssignment(self, child):
        obj = self.evalAssignable(child.getChild(0))

        val = self.evalExpr(child.getChild(0, AiLangParser.ExprContext))
        val = copy.deepcopy(val)
        obj.set(val)

        self.variableContextStack.put(obj)

    def evalReference(self, child):
        if isinstance(child, AiLangParser.Ref_opContext):
            assignable = child.getTypedRuleContext(AiLangParser.AssignableContext, 0)
            if assignable is None:
                raise ValueError()
            obj = self.evalAssignable(assignable).getLast()
            if obj.parent:
                if MethodSpace().hasMethod(type(obj.parent.val), obj.id):
                    expr = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
                    if expr is None:
                        raise ValueError()
                    ret = self.evalExpr(expr)
                    if not isinstance(ret, ListType):
                        raise ValueError()
                    MethodSpace().call(obj.parent, obj.id, ret.get())
                    return

            expr = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
            if not expr:
                raise ValueError()
            val = self.evalExpr(expr)
            self.variableContextStack.put(AiLangObj("", val), obj.getRoot())
