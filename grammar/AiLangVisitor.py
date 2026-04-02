# Generated from ./AiLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AiLangParser import AiLangParser
else:
    from AiLangParser import AiLangParser

# This class defines a complete generic visitor for a parse tree produced by AiLangParser.

class AiLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AiLangParser#prog.
    def visitProg(self, ctx:AiLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#block.
    def visitBlock(self, ctx:AiLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#label.
    def visitLabel(self, ctx:AiLangParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#context.
    def visitContext(self, ctx:AiLangParser.ContextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#bool_context.
    def visitBool_context(self, ctx:AiLangParser.Bool_contextContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#bool_group.
    def visitBool_group(self, ctx:AiLangParser.Bool_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#assignment.
    def visitAssignment(self, ctx:AiLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#id.
    def visitId(self, ctx:AiLangParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#ref_op.
    def visitRef_op(self, ctx:AiLangParser.Ref_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#column_ref_op.
    def visitColumn_ref_op(self, ctx:AiLangParser.Column_ref_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#functionDef.
    def visitFunctionDef(self, ctx:AiLangParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#assign.
    def visitAssign(self, ctx:AiLangParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#reference.
    def visitReference(self, ctx:AiLangParser.ReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#column_reference.
    def visitColumn_reference(self, ctx:AiLangParser.Column_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#printExpr.
    def visitPrintExpr(self, ctx:AiLangParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#block_stat.
    def visitBlock_stat(self, ctx:AiLangParser.Block_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#do_if_else.
    def visitDo_if_else(self, ctx:AiLangParser.Do_if_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#load_op.
    def visitLoad_op(self, ctx:AiLangParser.Load_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#func_def.
    def visitFunc_def(self, ctx:AiLangParser.Func_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#fromToData.
    def visitFromToData(self, ctx:AiLangParser.FromToDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#doIfElse.
    def visitDoIfElse(self, ctx:AiLangParser.DoIfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#bool_stat.
    def visitBool_stat(self, ctx:AiLangParser.Bool_statContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#columnMethod.
    def visitColumnMethod(self, ctx:AiLangParser.ColumnMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#idVal.
    def visitIdVal(self, ctx:AiLangParser.IdValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#mathOp.
    def visitMathOp(self, ctx:AiLangParser.MathOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#basicValExpr.
    def visitBasicValExpr(self, ctx:AiLangParser.BasicValExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#columnID.
    def visitColumnID(self, ctx:AiLangParser.ColumnIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#function.
    def visitFunction(self, ctx:AiLangParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#listValExpr.
    def visitListValExpr(self, ctx:AiLangParser.ListValExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#dataframe.
    def visitDataframe(self, ctx:AiLangParser.DataframeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#group.
    def visitGroup(self, ctx:AiLangParser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#named_arg.
    def visitNamed_arg(self, ctx:AiLangParser.Named_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#arg.
    def visitArg(self, ctx:AiLangParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#arg_list.
    def visitArg_list(self, ctx:AiLangParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#generic_list.
    def visitGeneric_list(self, ctx:AiLangParser.Generic_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#list.
    def visitList(self, ctx:AiLangParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#df.
    def visitDf(self, ctx:AiLangParser.DfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#df_val.
    def visitDf_val(self, ctx:AiLangParser.Df_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#column_id.
    def visitColumn_id(self, ctx:AiLangParser.Column_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#simpleColumn.
    def visitSimpleColumn(self, ctx:AiLangParser.SimpleColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#columnSet.
    def visitColumnSet(self, ctx:AiLangParser.ColumnSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#column_method.
    def visitColumn_method(self, ctx:AiLangParser.Column_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#func.
    def visitFunc(self, ctx:AiLangParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#numList.
    def visitNumList(self, ctx:AiLangParser.NumListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#strList.
    def visitStrList(self, ctx:AiLangParser.StrListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#number.
    def visitNumber(self, ctx:AiLangParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#string.
    def visitString(self, ctx:AiLangParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#group_basic_val.
    def visitGroup_basic_val(self, ctx:AiLangParser.Group_basic_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#intigerLiteral.
    def visitIntigerLiteral(self, ctx:AiLangParser.IntigerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#floatLiteral.
    def visitFloatLiteral(self, ctx:AiLangParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AiLangParser#str.
    def visitStr(self, ctx:AiLangParser.StrContext):
        return self.visitChildren(ctx)



del AiLangParser