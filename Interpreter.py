from antlr4 import tree
from grammar.AiLangParser import AiLangParser
import pandas as pd
import copy

TerminalNode:type = tree.Tree.TerminalNodeImpl

class Interpreter:

    def __init__(self, ast:AiLangParser.ProgContext):
        self.ast = ast
        self.variables = {}

    def interp(self):
        for child in self.ast.children:
            self.evaluate(child)

    def evaluate(self, child):
        if isinstance(child, AiLangParser.StatContext):
            for ch in child.children:
                if isinstance(ch, AiLangParser.ExprContext):
                    print("Expr")
                    print(self.evalExpr(ch))
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

    def evalMathOp(self, child:AiLangParser.MathOpContext):
        simpleColumn = child.getChild(0, ttype=AiLangParser.ColumnIDContext)
        df, col = self.getDfFromColumnCtx(simpleColumn)

        opToken = self.getTerminalSymbol(child.getChild(0, TerminalNode))
        operand = self.evalBasicVal(child.getChild(0, AiLangParser.BasicValExprContext))
        return eval(f"df[col] {opToken} operand", locals={
            "df": df,
            "col": col,
            "operand": operand,
        }) 


    def getColumnDfIdFromColumnCtx(self, child:AiLangParser.ColumnContext):
        idCtx = child.getChild(0, AiLangParser.IdContext)
        dfId = self.getTerminalSymbol(idCtx)
        sep = self.getTerminalSymbol(child.getChild(1))
        if '@' in sep:
            return #Not implemented
        else:
            columnID = self.getTerminalSymbol(child.getChild(0, AiLangParser.Column_idContext))
            return dfId, columnID

    def getDfFromColumnCtx(self, child:AiLangParser.ColumnIDContext) -> tuple[pd.DataFrame, str]:
        dfId, columnID = self.getColumnDfIdFromColumnCtx(child.getChild(0, AiLangParser.ColumnContext))
        df = self.variables[dfId]
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
            for ch in child.getChildren(lambda x: isinstance(x, AiLangParser.ExprContext)):
                l_val.append(self.evalExpr(ch))
            return l_val
    def evalIdVal(self, child):
        id = self.getTerminalSymbol(child)
        return self.variables[id]

    def evalDf(self, child:AiLangParser.DfContext):
        data = {}
        i=0
        for ch in  child.getChildren(lambda x: isinstance(x, AiLangParser.Df_valContext)):
            id = ch.getChild(0, ttype=AiLangParser.IdContext) 
            id = self.getTerminalSymbol(id) if id else i
            l_val = self.getBasicList(ch.getChild(0, ttype=AiLangParser.Basic_listContext))
            data[str(id)] = l_val
            i+=1
        return pd.DataFrame.from_dict(data)

    def getBasicList(self, child):
        if isinstance(child, AiLangParser.NumListContext):
            l_val = []
            for ch in child.getChildren(lambda x: isinstance(x, AiLangParser.IntigerLiteralContext)):
                l_val.append(self.getNumber(ch))
            return l_val
        if isinstance(child, AiLangParser.StrListContext):
            l_val = []
            for ch in child.getChildren(lambda x: isinstance(x, AiLangParser.StrContext)):
                l_val.append(self.getStr(ch))
            return l_val
        
    def evalBasicVal(self, child) -> int|str:
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
        if isinstance(child, tree.Tree.TerminalNodeImpl):
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
        elif isinstance(child, (AiLangParser.Ref_opContext, AiLangParser.Column_ref_opContext)):
            self.evalReference(child)
    
    def getFirstID(self, child):
        return self.getTerminalSymbol(child.getChild(0, ttype=AiLangParser.IdContext))

    def evalAssignment(self, child):
        id = self.getFirstID(child)
        val = self.evalExpr(child.getChild(0, AiLangParser.ExprContext))
        val = copy.deepcopy(val)
        self.variables[id] = val

    def getEvalExpr(self, child, i=0):
        return self.evalExpr(child.getChild(i, AiLangParser.ExprContext))

    def evalReference(self, child):
        if isinstance(child, AiLangParser.Ref_opContext):
            id = self.getFirstID(child)
            val = self.getEvalExpr(child)
            self.variables[id] = val
        elif isinstance(child, AiLangParser.Column_ref_opContext):
            dfId, col = self.getColumnDfIdFromColumnCtx(child.getChild(0, ttype=AiLangParser.ColumnContext))
            df = self.variables[dfId]
            val = self.getEvalExpr(child)
            df[col] = val
            self.variables[dfId] = df