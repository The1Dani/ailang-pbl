from antlr4 import TerminalNode
from grammar.AiLangParser import AiLangParser
import pandas as pd
import copy


class BlockTree:

    def __init__(self, ctx, label=None, parent=None, isStart=True):
        self.children: BlockTree = []
        self.parent = parent
        self.label = label
        self.ctx = ctx
        self.isStart = isStart
        self.level = 0 if parent is None else parent.level + 1

    def addChild(self, ctx, label) -> BlockTree:
        block = BlockTree(ctx, label, parent=self, isStart=False)
        self.children.append(block)
        return block

    def findLabel(self, label) -> BlockTree:
        if self.label == label:
            return self
        for child in self.children:
            if child.label == label:
                return child
            childReturn = child.findLabel(label)
            if childReturn:
                return childReturn

    def printTree(self, level=0):
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
        self.stack = []
        self.pushContext()

    def pushContext(self):
        if len(self.stack) == 0:
            self.stack.append({})
        else:
            self.stack.append(self.deepcopy())

    def popContext(self) -> dict:
        return self.stack.pop()

    def getContext(self) -> dict:
        return self.stack[-1]

    def put(self, key, val):
        self.getContext()[key] = val

    def get(self, key):
        return self.getContext()[key]

    def deepcopy(self) -> dict:
        return copy.deepcopy(self.getContext())

class Interpreter:

    def __init__(self, ast: AiLangParser.ProgContext):
        self.ast = ast
        self.variableContextStack = VariableStack()
        self.blockTree = None
        self.lastLabel = None

    def interp(self):
        for child in self.ast.children:
            self.evaluateGlobal(child)
        if self.blockTree is None:
            return #TODO add error for this case
        self.evaluateBlocks()
        self.blockTree.printTree()

    def evaluateBlocks(self, blocks=None):
        blocks = blocks if blocks else self.blockTree

        #Evaluate all statemnts inside the ctx
        for ch in blocks.ctx.children:
            self.evaluate(ch)
        if len(blocks.children) == 1:
            #If the block has only 1 child we shall skip the context push
            self.evaluateBlocks(blocks.children[0])
        else:
            #If the block has more thna 1 child we shoul duplicate state for each
            for block in blocks.children:
                self.variableContextStack.pushContext()
                self.evaluateBlocks(block)
                self.variableContextStack.popContext()

    def evaluateGlobal(self, child):
        #TODO Add functiond definitions in this method
        if isinstance(child, AiLangParser.Block_statContext):

            for ch in child.children:
                fromLabel, label, ctx = self.getBlockCtx(ch)
                print(f"FromLabel: {fromLabel} Label: {label}")

                if self.blockTree is None:
                    if fromLabel:
                        raise ValueError("Start must be the first block")

                    self.blockTree = BlockTree(ctx, label)
                    self.lastLabel = self.blockTree
                else:
                    if fromLabel:
                        fromBlock = self.blockTree.findLabel(fromLabel)
                        self.lastLabel = fromBlock.addChild(ctx, label)
                    else:
                        self.lastLabel = self.lastLabel.addChild(ctx, label)

    def getBlockCtx(self, child) -> tuple[str | None, any]:
        if isinstance(child, AiLangParser.Block2BlockContext):
            label = child.getChild(0, AiLangParser.LabelContext)
            if label:
                label = self.getFirstID(label)
            ctx = child.getChild(0, AiLangParser.ContextContext)
            return None, label, ctx
        elif isinstance(child, AiLangParser.Label2BlockContext):
            fromLabel = child.getChild(0, AiLangParser.LabelContext)
            label = child.getChild(1, AiLangParser.LabelContext)
            ctx = child.getChild(0, AiLangParser.ContextContext)
            if fromLabel:
                fromLabel = self.getFirstID(fromLabel)
            if label:
                label = self.getFirstID(label)
            return fromLabel, label, ctx

    def evaluate(self, child):
        if isinstance(child, (AiLangParser.StatContext, AiLangParser.ContextContext)):
            for ch in child.children:
                if isinstance(ch, AiLangParser.ExprContext):
                    print("Expr")
                    print(self.evalExpr(ch))
                elif isinstance(ch, TerminalNode):
                    continue
                else:
                    print("Stat")
                    self.evalStat(ch)

    def evalExpr(self, child):

        if isinstance(child, AiLangParser.MathOpContext):
            return self.evalMathOp(child)

        ch = child.getChild(0)
        if isinstance(ch, AiLangParser.Basic_valContext):
            return self.evalBasicVal(ch)
        elif isinstance(ch, AiLangParser.DfContext):
            return self.evalDf(ch)
        elif isinstance(ch, AiLangParser.ListContext):
            return self.getList(ch)
        elif isinstance(ch, AiLangParser.IdContext):
            return self.evalIdVal(ch)
        elif isinstance(ch, AiLangParser.ColumnContext):
            df, col = self.getDfFromColumnCtx(child)
            return df[col]

    def evalMathOp(self, child: AiLangParser.MathOpContext):
        simpleColumn = child.getChild(0, ttype=AiLangParser.ColumnIDContext)
        df, col = self.getDfFromColumnCtx(simpleColumn)

        opToken = self.getTerminalSymbol(child.getChild(0, TerminalNode))
        operand = self.evalBasicVal(child.getChild(0, AiLangParser.BasicValExprContext))
        return eval(
            f"df[col] {opToken} operand",
            locals={
                "df": df,
                "col": col,
                "operand": operand,
            },
        )

    def getColumnDfIdFromColumnCtx(self, child: AiLangParser.ColumnContext):
        idCtx = child.getChild(0, AiLangParser.IdContext)
        dfId = self.getTerminalSymbol(idCtx)
        sep = self.getTerminalSymbol(child.getChild(1))
        if "@" in sep:
            return  # Not implemented
        else:
            columnID = self.getTerminalSymbol(
                child.getChild(0, AiLangParser.Column_idContext)
            )
            return dfId, columnID

    def getDfFromColumnCtx(
        self, child: AiLangParser.ColumnIDContext
    ) -> tuple[pd.DataFrame, str]:
        dfId, columnID = self.getColumnDfIdFromColumnCtx(
            child.getChild(0, AiLangParser.ColumnContext)
        )
        df = self.variableContextStack.get(dfId)
        return df, columnID

    def getList(self, child):
        ch = child.getChild(0)
        if isinstance(ch, AiLangParser.Basic_listContext):
            return self.getBasicList(ch)
        elif isinstance(ch, AiLangParser.Generic_listContext):
            return self.getGenericList(ch)
        elif isinstance(ch, AiLangParser.IdContext):
            return self.evalIdVal(ch)

    def getGenericList(self, child):
        if isinstance(child, AiLangParser.Generic_listContext):
            l_val = []
            for ch in child.getChildren(
                lambda x: isinstance(x, AiLangParser.ExprContext)
            ):
                l_val.append(self.evalExpr(ch))
            return l_val

    def evalIdVal(self, child):
        id = self.getTerminalSymbol(child)
        return self.variableContextStack.get(id)

    def evalDf(self, child: AiLangParser.DfContext):
        data = {}
        i = 0
        for ch in child.getChildren(
            lambda x: isinstance(x, AiLangParser.Df_valContext)
        ):
            id = ch.getChild(0, ttype=AiLangParser.IdContext)
            id = self.getTerminalSymbol(id) if id else i
            l_val = self.getBasicList(
                ch.getChild(0, ttype=AiLangParser.Basic_listContext)
            )
            data[str(id)] = l_val
            i += 1
        return pd.DataFrame.from_dict(data)

    def getBasicList(self, child):
        if isinstance(child, AiLangParser.NumListContext):
            l_val = []
            for ch in child.getChildren(
                lambda x: isinstance(x, AiLangParser.IntigerLiteralContext)
            ):
                l_val.append(self.getNumber(ch))
            return l_val
        if isinstance(child, AiLangParser.StrListContext):
            l_val = []
            for ch in child.getChildren(
                lambda x: isinstance(x, AiLangParser.StrContext)
            ):
                l_val.append(self.getStr(ch))
            return l_val

    def evalBasicVal(self, child) -> int | str:
        # ch = child
        if isinstance(child, AiLangParser.BasicValExprContext):
            child = child.getChild(0)
        ch = child.getChild(0)
        if isinstance(ch, (AiLangParser.NumContext, AiLangParser.NumberContext)):
            return self.getNumber(ch)
        if isinstance(ch, AiLangParser.StrContext):
            return self.getStr(ch)

    def getStr(self, child):
        return self.getTerminalSymbol(child.getChild(0))[1:-1]

    def getTerminalSymbol(self, child) -> str:
        if isinstance(child, TerminalNode):
            return child.symbol.text
        return self.getTerminalSymbol(child.getChild(0))

    def getNumber(self, child) -> int:

        if isinstance(child, AiLangParser.IntigerLiteralContext):
            return int(self.getTerminalSymbol(child))
        elif isinstance(child, AiLangParser.FloatLiteralContext):
            symb = self.getTerminalSymbol(child)
            num = float(".".join(map(lambda x: str(int(x)), symb.split("."))))
            return num
        return None

    def evalStat(self, child):
        
        if isinstance(child, AiLangParser.AssignmentContext):
            self.evalAssignment(child)
        elif isinstance(
            child, (AiLangParser.Ref_opContext, AiLangParser.Column_ref_opContext)
        ):
            self.evalReference(child)

    def getFirstID(self, child):
        return self.getTerminalSymbol(child.getChild(0, ttype=AiLangParser.IdContext))

    def evalAssignment(self, child):
        id = self.getFirstID(child)
        val = self.evalExpr(child.getChild(0, AiLangParser.ExprContext))
        val = copy.deepcopy(val)
        self.variableContextStack.put(id, val)

    def getEvalExpr(self, child, i=0):
        return self.evalExpr(child.getChild(i, AiLangParser.ExprContext))

    def evalReference(self, child):
        if isinstance(child, AiLangParser.Ref_opContext):
            id = self.getFirstID(child)
            val = self.getEvalExpr(child)
            self.variableContextStack.put(id, val)

        elif isinstance(child, AiLangParser.Column_ref_opContext):
            dfId, col = self.getColumnDfIdFromColumnCtx(
                child.getChild(0, ttype=AiLangParser.ColumnContext)
            )
            df = self.variables[dfId]
            val = self.getEvalExpr(child)
            df[col] = val
            self.variableContextStack.put(dfId, df)
