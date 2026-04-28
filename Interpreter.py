from dataclasses import dataclass
from io import StringIO
from typing import Callable
import copy
from antlr4 import TerminalNode
from grammar.AiLangLexer import AiLangLexer
from grammar.AiLangParser import AiLangParser

import AiLangLib as _  # Init Import
from AiLangType import (
    BasicValType,
    NumType,
    DfType,
    DfItem,
    ListType,
    NumTypes,
    StrType,
    AiLangType,
    BoolType,
)
from AiLangObj import AiLangObj, NoneObj, fromDFtoObj
from AiLangFunc import AiLangCallable, AiLangFunc, FunctionSpace, MethodSpace
import utils


class BlockTree:
    """A tree class for the block structure"""

    def __init__(self, ctx, label=None, parent=None, is_start=True):
        self.children: list[BlockTree] = []
        self.parent = parent
        self.label = label
        self.ctx = ctx
        self.is_start = is_start
        self.level = 0 if parent is None else parent.level + 1

    def addChild(self, ctx, label) -> BlockTree:

        block = BlockTree(ctx, label, parent=self, is_start=False)
        self.children.append(block)
        return block

    def findLabel(self, label) -> BlockTree | None:
        if self.label == label:
            return self
        for child in self.children:
            if child.label == label:
                return child
            child_return = child.findLabel(label)
            if child_return:
                return child_return
        return None

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
    """Variable Stack that stores variable spaces across blocks and context changes"""

    def __init__(self, interp: Interpreter | None = None):
        self.stack: list[dict[int, AiLangObj]] = []
        self.pushContext()
        self.next_id: int = 0
        self.interp: Interpreter | None = interp

    def _nextID(self) -> int:
        ident = self.next_id
        self.next_id += 1
        return ident

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

    def _findObjInCtx(self, ctx: dict[int, AiLangObj], key: str) -> AiLangObj | None:
        for _, obj in ctx.items():
            if obj.ident == key:
                return obj
        return None

    def _get(self, key: str | AiLangObj) -> AiLangObj | list[AiLangObj] | None:
        ctx = self.getContext()
        if isinstance(key, str):
            return self._findObjInCtx(ctx, key)

        if len(key.members) == 0:
            return self._get(key.ident)

        result_obj = None
        for _, obj in ctx.items():
            if obj.ident == key.getRoot().ident:
                result_obj = obj
        if result_obj is None:
            return None

        key_cur = key
        cur = result_obj
        result = []

        def getResult():
            nonlocal key_cur, cur, result
            if len(key_cur.members) > 0:
                memb = list(key_cur.members.values())
                key_cur = memb[0]
            if isinstance(cur.val, DfType):
                item = cur.getDFItemByID(key_cur.ident)
                if item:
                    result.append(item)
                    return
                memb = list(key_cur.getParent().members.values())
                vals = [(DfItem(m.get().get()), m.ident) for m in memb]
                objs = [AiLangObj(ident, item) for item, ident in vals]
                for obj in objs:
                    cur.setMember(obj)
                result += objs
                return
            if key_cur.ident in cur.members:
                last_cur = cur
                cur = cur.members[key_cur.ident]
                if len(cur.members) == 0:
                    result.append(cur)
                    cur = last_cur
                    getResult()
                del last_cur.members[key_cur.ident]
            else:
                return

        getResult()

        if len(result) == 0:
            return None
        if len(result) == 1:
            return result[0]
        return result

    def get(self, key: str | AiLangObj) -> AiLangObj | FuncParams | list[AiLangObj]:
        ret = self._get(key)
        if ret is None:
            if self.interp is not None and isinstance(key, AiLangObj):
                method_id, parent = self.interp.getMethodAndParentFromKeyObj(
                    copy.deepcopy(key), True
                )
                if MethodSpace().hasMethod(type(parent.val), method_id):
                    return FuncParams(method_id, parent)
            raise ValueError(
                f"The key ({key}) is not in the stack frame {self.getContext()}"
            )
        return ret

    def deepcopy(self) -> dict:
        return copy.deepcopy(self.getContext())


@dataclass
class FuncParams:
    """A struct that represents a function/method attributes"""

    method_id: str
    parent: AiLangObj

    @property
    def vals(self) -> tuple[str, AiLangObj]:
        return self.method_id, self.parent


# pylint: disable-next=too-many-public-methods
class Interpreter:
    """Interpreter"""

    def __init__(self, ast: AiLangParser.ProgContext) -> None:
        self.ast = ast
        self.variable_context_stack = VariableStack(self)
        self.block_tree = None
        self.last_label = None
        self.functions = FunctionSpace()
        self.methods = MethodSpace()

    def interp(self) -> None:
        if self.ast.children is None:
            raise ValueError()
        blocks = self.ast.getTypedRuleContexts(AiLangParser.Block_statContext)
        for block in blocks:
            self.constructBlockTree(block)
        func_decls = self.ast.getTypedRuleContexts(AiLangParser.FunctionDefContext)
        for fd in func_decls:
            self.evalFunctionDecl(fd)
        if self.block_tree is None:
            raise ValueError("Block Tree is Empty")
        self.evaluateBlocks()
        # self.blockTree.printTree()

    def evalFunctionDecl(self, func_decl: AiLangParser.FunctionDefContext):
        fd = func_decl.getTypedRuleContext(AiLangParser.Func_defContext, 0)
        if fd is None:
            raise ValueError()
        func = self.evalFuncDef(fd, self.ctxRunnerConstructer())
        self.functions.addFunc(func)

    def evaluateBlocks(self, blocks: BlockTree | None = None) -> None:
        blocks = blocks if blocks is not None else self.block_tree
        if blocks is None:
            raise ValueError("The block tree is not set cannot evaluate")
        # Evaluate all statemnts inside the ctx
        for ch in blocks.ctx.children:
            if isinstance(ch, TerminalNode):
                continue
            if not self.evaluate(ch):
                break
        if len(blocks.children) == 1:
            # If the block has only 1 child we shall skip the context push
            self.evaluateBlocks(blocks.children[0])
        else:
            # If the block has more thna 1 child we shoul duplicate state for each
            for block in blocks.children:
                self.variable_context_stack.pushContext()
                self.evaluateBlocks(block)
                self.variable_context_stack.popContext()

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
        ) -> Callable[[AiLangCallable], dict[int, AiLangObj]]:
            def runner(*args, **kwargs) -> dict[int, AiLangObj]:
                """
                Runner runs the lines of code in ctx and if there is a return
                it puts to the stack frame on address '-1'
                """
                self.variable_context_stack.pushFuncContext()
                for arg in args:
                    if not isinstance(arg, AiLangObj):
                        continue
                    self.variable_context_stack.put(arg)
                for _, arg_val in kwargs.items():
                    if not isinstance(arg_val, AiLangObj):
                        continue
                    self.variable_context_stack.put(arg_val)
                stats = ctx.getTypedRuleContexts(AiLangParser.StatContext)
                for stat in stats:
                    if not self.evaluate(stat):
                        break
                return self.variable_context_stack.popContext()

            return runner

        return constructor

    def constructBlockTree(self, child: AiLangParser.Block_statContext) -> None:
        if isinstance(child, AiLangParser.Block_statContext):
            if child.children is None:
                raise ValueError()
            for ch in child.children:
                if not isinstance(
                    ch,
                    (AiLangParser.Block2BlockContext, AiLangParser.Label2BlockContext),
                ):
                    raise ValueError()
                from_label, label, ctx = self.getBlockCtx(ch)
                # print(f"FromLabel: {fromLabel} Label: {label}")

                if self.block_tree is None:
                    if from_label:
                        raise ValueError("Start must be the first block")

                    self.block_tree = BlockTree(ctx, label)
                    self.last_label = self.block_tree
                else:
                    if from_label:
                        from_block = self.block_tree.findLabel(from_label)
                        if from_block is None:
                            raise ValueError()
                        self.last_label = from_block.addChild(ctx, label)
                    else:
                        if self.last_label is None:
                            raise ValueError()
                        self.last_label = self.last_label.addChild(ctx, label)

    def getBlockCtx(
        self, child: AiLangParser.Block2BlockContext | AiLangParser.Label2BlockContext
    ) -> tuple[None | str, None | str, AiLangParser.ContextContext | None]:
        if isinstance(child, AiLangParser.Block2BlockContext):
            label = child.getTypedRuleContext(AiLangParser.LabelContext, 0)
            if label:
                label = self.getFirstID(label)
            ctx = child.getTypedRuleContext(AiLangParser.ContextContext, 0)
            return None, label, ctx

        # Label2BlockContext
        from_label = child.getTypedRuleContext(AiLangParser.LabelContext, 0)
        label = child.getTypedRuleContext(AiLangParser.LabelContext, 1)
        ctx = child.getTypedRuleContext(AiLangParser.ContextContext, 0)
        if from_label:
            from_label = self.getFirstID(from_label)
        if label:
            label = self.getFirstID(label)
        return from_label, label, ctx

    def evaluate(
        self, child: AiLangParser.StatContext | AiLangParser.ContextContext
    ) -> bool:
        """
        Returns True on normal evaluation adn returns False if there was a return stat
        """
        if child.children is None:
            raise ValueError()
        for ch in child.children:
            if isinstance(ch, TerminalNode):
                continue
            if isinstance(ch, AiLangParser.ExprContext):
                self.evalExpr(ch)
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

    def evalRet(self, child: AiLangParser.RetContext) -> None:
        if isinstance(child, AiLangParser.NoneReturnContext):
            return
        if isinstance(child, AiLangParser.ExprReturnContext):
            expr = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
            if expr is None:
                raise ValueError()
            val = self.evalExpr(expr)
            self.variable_context_stack.putReturn(AiLangObj("Return", val))

    def evalFrom2Data(self, child: AiLangParser.FromToDataContext) -> None:
        str_ctx = child.getTypedRuleContext(AiLangParser.StrContext, 0)
        if str_ctx is None:
            raise ValueError()
        file_str = StrType.make(str_ctx).get()
        ident = self.getFirstID(child)

        data = self.transformFile2Data(file_str)
        df = data.get()
        obj = fromDFtoObj(ident, df)

        self.variable_context_stack.put(obj)

    def transformFile2Data(self, file_name):
        data = utils.tf2d(file_name)
        return DfType(data)

    def evalDoIfElse(self, child: AiLangParser.DoIfElseContext) -> bool:
        # Do Block mandatory
        do_ctx = child.getTypedRuleContext(AiLangParser.ContextContext, 0)
        # If Block mandatory
        ifb_ctx = child.getTypedRuleContext(AiLangParser.Bool_contextContext, 0)
        # Else Block optional
        else_ctx = child.getTypedRuleContext(AiLangParser.ContextContext, 1)
        parent = self

        class DoIfElse:
            """ResolveDoIfElse"""

            def __init__(self, do_ctx, ifb_ctx, else_ctx):
                self.do_ctx = do_ctx
                self.ifb_ctx: AiLangParser.Bool_contextContext = ifb_ctx
                self.else_ctx = else_ctx

            def eval(self) -> bool:
                if self.resolveIf():
                    ctx = self.do_ctx
                elif self.else_ctx is not None:
                    ctx = self.else_ctx
                else:
                    ctx = None

                if ctx is None:
                    return True

                return parent.evalNonBlockContext(ctx)

            def resolveIf(self):
                bool_groups = self.ifb_ctx.getChildren(
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

        return DoIfElse(do_ctx, ifb_ctx, else_ctx).eval()

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
            ops = [self.getPythonBoolOp(op) for op in ops]
        else:
            if not isinstance(statements[0], AiLangParser.Bool_statContext):
                raise ValueError()
            return self.evalBoolStat(statements[0]).get()

        with StringIO() as builder:
            for result in results:
                builder.write(str(result))
                builder.write(" ")
                if len(ops) > 0:
                    builder.write(str(ops.pop(0)))
            bool_str = builder.getvalue()

        return bool(eval(bool_str))

    def getPythonBoolOp(self, op):
        operations = {
            "&": "and",
            "|": "or",  # not in parser
            "&&": "and",
            "||": "or",  # not in parser
        }
        if op in operations:
            return operations[op]
        return op  # TODO: ADD ailang bool translation to python here

    def evalBoolStat(self, child: AiLangParser.Bool_statContext) -> BoolType:
        val1 = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
        val2 = child.getTypedRuleContext(AiLangParser.ExprContext, 1)
        if not (val1 and val2):
            raise ValueError()
        val1 = self.evalExpr(val1)
        val2 = self.evalExpr(val2)

        op = self.getPythonBoolOp(
            utils.getTerminalSymbol(
                child.getToken(AiLangLexer.BOOL_OP, 0)
            )  # Gets the first Terminals Text
        )

        if not (
            isinstance(val1, BoolType)
            and isinstance(val2, BoolType)
            and op in ["and", "or"]
        ):

            raise ValueError(
                "Operators '&' and '|' can only be used for other booleans"
            )

        # TODO: resolve other bool operations like DataFrame operations here
        # To resolve this todo there is a need to decide how the capturing of the
        # variables should resolve

        return BoolType(
            bool(
                eval(
                    f"x {op} y",
                    {
                        "x": val1.get(),
                        "y": val2.get(),
                    },
                )
            )
        )

    # pylint: disable-next=too-many-return-statements
    def evalExpr(self, child: AiLangParser.ExprContext) -> AiLangType:
        if isinstance(child, AiLangParser.MathOpContext):
            return self.evalMathOp(child)
        if isinstance(child, AiLangParser.MethodCallContext):
            return self.evalMethod(child)
        if isinstance(child, AiLangParser.GroupContext):
            expr_ctx = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
            if expr_ctx is None:
                raise ValueError()
            return self.evalExpr(expr_ctx)

        ch = child.getChild(0)
        if isinstance(ch, AiLangParser.Basic_valContext):
            return BasicValType.make(ch)
        if isinstance(ch, AiLangParser.DfContext):
            return DfType.make(ch)
        if isinstance(ch, AiLangParser.ListContext):
            chch = ch.getChild(0)
            if isinstance(chch, AiLangParser.Generic_listContext):
                return self.getGenericList(chch)
            return ListType.make(chch)
        if isinstance(ch, AiLangParser.AssignableContext):
            return self.evalAssignable(ch).get()
        if isinstance(ch, AiLangParser.FuncContext):
            return self.evalFunc(ch)

        raise NotADirectoryError()

    def getGenericList(self, child: AiLangParser.Generic_listContext) -> ListType:
        l_val = []
        for ch in child.getTypedRuleContexts(AiLangParser.ExprContext):
            l_val.append(self.evalExpr(ch))
        return ListType(l_val)

    def getMethodAndParentFromKeyObj(
        self, key: AiLangObj, parent_found=False
    ) -> tuple[str, AiLangObj]:
        method_id = key.getLast().ident
        key.killMembers()
        try:
            if not parent_found:
                # NOTE: this will get the key value there is a chance its not the correct parent
                parent = self.variable_context_stack.get(key)
                if not isinstance(parent, AiLangObj):
                    raise ValueError()
            else:
                parent = key

        except ValueError:
            parent = key
        if not isinstance(key, AiLangObj):
            raise NotImplementedError()
        return method_id, parent

    def evalMethod(self, child: AiLangParser.MethodCallContext) -> AiLangType:
        obj = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
        if obj is None:
            raise ValueError()
        obj = obj.getTypedRuleContext(AiLangParser.AssignableContext, 0)
        if obj is None:
            raise ValueError()
        obj = AiLangObj.make(obj)
        method_id, parent = self.getMethodAndParentFromKeyObj(obj)
        arg_list = child.getTypedRuleContext(AiLangParser.Arg_listContext, 0)
        if arg_list is None:
            raise ValueError()
        args, kwargs = self.evalArgsList(arg_list)
        if isinstance(parent, list):
            raise NotImplementedError()
        if MethodSpace().hasMethod(type(parent.val), method_id):
            return MethodSpace().call(parent, method_id, args, kwargs).get()
        raise ValueError(
            f"Method {method_id} is not available for type {str(type(parent.val))}"
        )

    def evalArgsList(
        self, child: AiLangParser.Arg_listContext
    ) -> tuple[list[AiLangObj], dict[str, AiLangObj]]:
        args = []
        kwargs = {}
        for arg in child.getTypedRuleContexts(AiLangParser.ArgContext):
            arg_val = self.evalArg(arg)
            if arg_val.ident != "":
                kwargs[arg_val.ident] = arg_val
            elif arg_val:
                args.append(arg_val)
        return args, kwargs

    def evalArg(self, child: AiLangParser.ArgContext) -> AiLangObj:
        if isinstance(child, AiLangParser.NamedArgContext):
            named_arg = child.getTypedRuleContext(AiLangParser.Named_argContext, 0)
            if named_arg is None:
                raise ValueError()
            return self.evalNamedArg(named_arg)
        if isinstance(child, AiLangParser.ExprArgContext):
            expr = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
            if expr is None:
                raise ValueError()
            return AiLangObj("", self.evalExpr(expr))

        raise ValueError()

    def evalNamedArg(self, child: AiLangParser.Named_argContext) -> AiLangObj:
        ident = child.getTypedRuleContext(AiLangParser.IdContext, 0)
        if ident is None:
            raise ValueError()
        expr = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
        if expr is None:
            raise ValueError()
        ident = utils.getTerminalSymbol(ident)
        val = self.evalExpr(expr)
        return AiLangObj(ident, val)

    def evalFunc(self, child: AiLangParser.FuncContext) -> AiLangType:
        ids = utils.getAllIds(child)
        if len(ids) != 1:
            raise ValueError()
        func_id = ids[0]

        args_node = child.getTypedRuleContext(AiLangParser.Arg_listContext, 0)
        if args_node is None:
            args = []
            kwargs: dict[str, AiLangObj] = {}
        else:
            args, kwargs = self.evalArgsList(args_node)

        if FunctionSpace().hasFunc(func_id):
            return FunctionSpace().call(func_id, args, kwargs).get()

        raise ValueError(f"Function {func_id} is not in FunctionSpace")

    def evalFuncDef(
        self,
        node: AiLangParser.Func_defContext,
        ctx_runner_constructor: Callable[
            [AiLangParser.ContextContext],
            Callable[[AiLangCallable], dict[int, AiLangObj]],
        ],
    ) -> AiLangFunc:
        func_id = node.getTypedRuleContext(AiLangParser.IdContext, 0)
        if func_id is None:
            raise ValueError()
        func_id = utils.getTerminalSymbol(func_id)
        ids = []
        kwargs = {}

        args = node.getTypedRuleContexts(AiLangParser.Def_argContext)
        for arg in args:
            ch = arg.getChild(0)
            if isinstance(ch, AiLangParser.IdContext):
                ids.append(utils.getTerminalSymbol(ch))
            elif isinstance(ch, AiLangParser.Named_argContext):
                obj = self.evalNamedArg(ch)
                key = obj.ident
                kwargs[key] = obj

        ctx = node.getTypedRuleContext(AiLangParser.ContextContext, 0)
        if ctx is None:
            raise ValueError()
        func = AiLangFunc.constructCallableFromCtx(ctx_runner_constructor(ctx))
        return AiLangFunc(func_id, func, ids, kwargs)

    def evalMathOp(self, child: AiLangParser.MathOpContext):
        """
        Supported Cases:
        a) num {op} num
        b) df{or dfItem} {op} num
        """
        expr1, expr2 = child.getTypedRuleContext(
            AiLangParser.ExprContext, 0
        ), child.getTypedRuleContext(AiLangParser.ExprContext, 1)
        if not (expr1 and expr2):
            raise ValueError()

        lop = self.evalExpr(expr1)
        optoken = utils.getTerminalSymbol(child.getChild(1))
        rop = self.evalExpr(expr2)

        # When a and b are Numerals
        if isinstance(lop, NumType) and isinstance(rop, NumType):
            num = eval(
                f"a {optoken} b",
                locals={
                    "a": lop.get(),
                    "b": rop.get(),
                },
            )
            return NumType(
                num, NumTypes.INT if isinstance(num, int) else NumTypes.FLOAT
            )

        # When a is df and b is a Numeral
        if isinstance(lop, (DfType, DfItem)) and isinstance(
            rop, (NumType, DfType, DfItem)
        ):
            df = eval(
                f"a {optoken} b",
                locals={
                    "a": lop.get(),
                    "b": rop.get(),
                },
            )
            return DfType(df)

        raise ValueError(
            f"{lop} and {rop} has been tried to be conneted with {optoken}"
        )

    def evalAssignable(self, child: AiLangParser.AssignableContext) -> AiLangObj:
        obj = AiLangObj.make(child)
        val = self.variable_context_stack.get(obj)
        if isinstance(val, list):
            raise NotImplementedError()
        if isinstance(val, FuncParams):
            method_id, parent = val.vals
            MethodSpace().call(parent, method_id, [], {})
            return NoneObj()

        return val

    def getFirstID(self, child):
        return utils.getTerminalSymbol(child.getChild(0, ttype=AiLangParser.IdContext))

    def evalAssignment(self, child):
        obj = AiLangObj.make(child.getChild(0))

        val = self.evalExpr(child.getChild(0, AiLangParser.ExprContext))
        val = copy.deepcopy(val)
        obj.set(val)

        self.variable_context_stack.put(obj)

    def evalReference(self, child):
        if isinstance(child, AiLangParser.Ref_opContext):
            assignable = child.getTypedRuleContext(AiLangParser.AssignableContext, 0)
            if assignable is None:
                raise ValueError()
            obj = AiLangObj.make(assignable).getLast()

            # Check If there is a method assisated with the parent
            if obj.parent:
                if MethodSpace().hasMethod(type(obj.parent.val), obj.ident):
                    expr = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
                    if expr is None:
                        raise ValueError()
                    ret = self.evalExpr(expr)
                    if not isinstance(ret, ListType):
                        raise ValueError()
                    MethodSpace().call(obj.parent, obj.ident, ret.get(), {})
                    return

            expr = child.getTypedRuleContext(AiLangParser.ExprContext, 0)
            if not expr:
                raise ValueError()
            val = self.evalExpr(expr)
            self.variable_context_stack.put(AiLangObj("", val), obj.getRoot())
