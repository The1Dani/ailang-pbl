# Generated from ./AiLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AiLangParser import AiLangParser
else:
    from AiLangParser import AiLangParser

# This class defines a complete listener for a parse tree produced by AiLangParser.
class AiLangListener(ParseTreeListener):

    # Enter a parse tree produced by AiLangParser#prog.
    def enterProg(self, ctx:AiLangParser.ProgContext):
        pass

    # Exit a parse tree produced by AiLangParser#prog.
    def exitProg(self, ctx:AiLangParser.ProgContext):
        pass


    # Enter a parse tree produced by AiLangParser#Block2Block.
    def enterBlock2Block(self, ctx:AiLangParser.Block2BlockContext):
        pass

    # Exit a parse tree produced by AiLangParser#Block2Block.
    def exitBlock2Block(self, ctx:AiLangParser.Block2BlockContext):
        pass


    # Enter a parse tree produced by AiLangParser#Label2Block.
    def enterLabel2Block(self, ctx:AiLangParser.Label2BlockContext):
        pass

    # Exit a parse tree produced by AiLangParser#Label2Block.
    def exitLabel2Block(self, ctx:AiLangParser.Label2BlockContext):
        pass


    # Enter a parse tree produced by AiLangParser#label.
    def enterLabel(self, ctx:AiLangParser.LabelContext):
        pass

    # Exit a parse tree produced by AiLangParser#label.
    def exitLabel(self, ctx:AiLangParser.LabelContext):
        pass


    # Enter a parse tree produced by AiLangParser#context.
    def enterContext(self, ctx:AiLangParser.ContextContext):
        pass

    # Exit a parse tree produced by AiLangParser#context.
    def exitContext(self, ctx:AiLangParser.ContextContext):
        pass


    # Enter a parse tree produced by AiLangParser#bool_context.
    def enterBool_context(self, ctx:AiLangParser.Bool_contextContext):
        pass

    # Exit a parse tree produced by AiLangParser#bool_context.
    def exitBool_context(self, ctx:AiLangParser.Bool_contextContext):
        pass


    # Enter a parse tree produced by AiLangParser#bool_group.
    def enterBool_group(self, ctx:AiLangParser.Bool_groupContext):
        pass

    # Exit a parse tree produced by AiLangParser#bool_group.
    def exitBool_group(self, ctx:AiLangParser.Bool_groupContext):
        pass


    # Enter a parse tree produced by AiLangParser#bool_stat.
    def enterBool_stat(self, ctx:AiLangParser.Bool_statContext):
        pass

    # Exit a parse tree produced by AiLangParser#bool_stat.
    def exitBool_stat(self, ctx:AiLangParser.Bool_statContext):
        pass


    # Enter a parse tree produced by AiLangParser#assignment.
    def enterAssignment(self, ctx:AiLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by AiLangParser#assignment.
    def exitAssignment(self, ctx:AiLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by AiLangParser#id.
    def enterId(self, ctx:AiLangParser.IdContext):
        pass

    # Exit a parse tree produced by AiLangParser#id.
    def exitId(self, ctx:AiLangParser.IdContext):
        pass


    # Enter a parse tree produced by AiLangParser#ref_op.
    def enterRef_op(self, ctx:AiLangParser.Ref_opContext):
        pass

    # Exit a parse tree produced by AiLangParser#ref_op.
    def exitRef_op(self, ctx:AiLangParser.Ref_opContext):
        pass


    # Enter a parse tree produced by AiLangParser#NoneReturn.
    def enterNoneReturn(self, ctx:AiLangParser.NoneReturnContext):
        pass

    # Exit a parse tree produced by AiLangParser#NoneReturn.
    def exitNoneReturn(self, ctx:AiLangParser.NoneReturnContext):
        pass


    # Enter a parse tree produced by AiLangParser#ExprReturn.
    def enterExprReturn(self, ctx:AiLangParser.ExprReturnContext):
        pass

    # Exit a parse tree produced by AiLangParser#ExprReturn.
    def exitExprReturn(self, ctx:AiLangParser.ExprReturnContext):
        pass


    # Enter a parse tree produced by AiLangParser#functionDef.
    def enterFunctionDef(self, ctx:AiLangParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by AiLangParser#functionDef.
    def exitFunctionDef(self, ctx:AiLangParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by AiLangParser#assign.
    def enterAssign(self, ctx:AiLangParser.AssignContext):
        pass

    # Exit a parse tree produced by AiLangParser#assign.
    def exitAssign(self, ctx:AiLangParser.AssignContext):
        pass


    # Enter a parse tree produced by AiLangParser#reference.
    def enterReference(self, ctx:AiLangParser.ReferenceContext):
        pass

    # Exit a parse tree produced by AiLangParser#reference.
    def exitReference(self, ctx:AiLangParser.ReferenceContext):
        pass


    # Enter a parse tree produced by AiLangParser#printExpr.
    def enterPrintExpr(self, ctx:AiLangParser.PrintExprContext):
        pass

    # Exit a parse tree produced by AiLangParser#printExpr.
    def exitPrintExpr(self, ctx:AiLangParser.PrintExprContext):
        pass


    # Enter a parse tree produced by AiLangParser#block_stat.
    def enterBlock_stat(self, ctx:AiLangParser.Block_statContext):
        pass

    # Exit a parse tree produced by AiLangParser#block_stat.
    def exitBlock_stat(self, ctx:AiLangParser.Block_statContext):
        pass


    # Enter a parse tree produced by AiLangParser#do_if_else.
    def enterDo_if_else(self, ctx:AiLangParser.Do_if_elseContext):
        pass

    # Exit a parse tree produced by AiLangParser#do_if_else.
    def exitDo_if_else(self, ctx:AiLangParser.Do_if_elseContext):
        pass


    # Enter a parse tree produced by AiLangParser#load_op.
    def enterLoad_op(self, ctx:AiLangParser.Load_opContext):
        pass

    # Exit a parse tree produced by AiLangParser#load_op.
    def exitLoad_op(self, ctx:AiLangParser.Load_opContext):
        pass


    # Enter a parse tree produced by AiLangParser#return.
    def enterReturn(self, ctx:AiLangParser.ReturnContext):
        pass

    # Exit a parse tree produced by AiLangParser#return.
    def exitReturn(self, ctx:AiLangParser.ReturnContext):
        pass


    # Enter a parse tree produced by AiLangParser#func_def.
    def enterFunc_def(self, ctx:AiLangParser.Func_defContext):
        pass

    # Exit a parse tree produced by AiLangParser#func_def.
    def exitFunc_def(self, ctx:AiLangParser.Func_defContext):
        pass


    # Enter a parse tree produced by AiLangParser#fromToData.
    def enterFromToData(self, ctx:AiLangParser.FromToDataContext):
        pass

    # Exit a parse tree produced by AiLangParser#fromToData.
    def exitFromToData(self, ctx:AiLangParser.FromToDataContext):
        pass


    # Enter a parse tree produced by AiLangParser#doIfElse.
    def enterDoIfElse(self, ctx:AiLangParser.DoIfElseContext):
        pass

    # Exit a parse tree produced by AiLangParser#doIfElse.
    def exitDoIfElse(self, ctx:AiLangParser.DoIfElseContext):
        pass


    # Enter a parse tree produced by AiLangParser#func.
    def enterFunc(self, ctx:AiLangParser.FuncContext):
        pass

    # Exit a parse tree produced by AiLangParser#func.
    def exitFunc(self, ctx:AiLangParser.FuncContext):
        pass


    # Enter a parse tree produced by AiLangParser#mathOp.
    def enterMathOp(self, ctx:AiLangParser.MathOpContext):
        pass

    # Exit a parse tree produced by AiLangParser#mathOp.
    def exitMathOp(self, ctx:AiLangParser.MathOpContext):
        pass


    # Enter a parse tree produced by AiLangParser#basicValExpr.
    def enterBasicValExpr(self, ctx:AiLangParser.BasicValExprContext):
        pass

    # Exit a parse tree produced by AiLangParser#basicValExpr.
    def exitBasicValExpr(self, ctx:AiLangParser.BasicValExprContext):
        pass


    # Enter a parse tree produced by AiLangParser#pathExpr.
    def enterPathExpr(self, ctx:AiLangParser.PathExprContext):
        pass

    # Exit a parse tree produced by AiLangParser#pathExpr.
    def exitPathExpr(self, ctx:AiLangParser.PathExprContext):
        pass


    # Enter a parse tree produced by AiLangParser#function.
    def enterFunction(self, ctx:AiLangParser.FunctionContext):
        pass

    # Exit a parse tree produced by AiLangParser#function.
    def exitFunction(self, ctx:AiLangParser.FunctionContext):
        pass


    # Enter a parse tree produced by AiLangParser#listValExpr.
    def enterListValExpr(self, ctx:AiLangParser.ListValExprContext):
        pass

    # Exit a parse tree produced by AiLangParser#listValExpr.
    def exitListValExpr(self, ctx:AiLangParser.ListValExprContext):
        pass


    # Enter a parse tree produced by AiLangParser#dataframe.
    def enterDataframe(self, ctx:AiLangParser.DataframeContext):
        pass

    # Exit a parse tree produced by AiLangParser#dataframe.
    def exitDataframe(self, ctx:AiLangParser.DataframeContext):
        pass


    # Enter a parse tree produced by AiLangParser#group.
    def enterGroup(self, ctx:AiLangParser.GroupContext):
        pass

    # Exit a parse tree produced by AiLangParser#group.
    def exitGroup(self, ctx:AiLangParser.GroupContext):
        pass


    # Enter a parse tree produced by AiLangParser#methodCall.
    def enterMethodCall(self, ctx:AiLangParser.MethodCallContext):
        pass

    # Exit a parse tree produced by AiLangParser#methodCall.
    def exitMethodCall(self, ctx:AiLangParser.MethodCallContext):
        pass


    # Enter a parse tree produced by AiLangParser#simpleTarget.
    def enterSimpleTarget(self, ctx:AiLangParser.SimpleTargetContext):
        pass

    # Exit a parse tree produced by AiLangParser#simpleTarget.
    def exitSimpleTarget(self, ctx:AiLangParser.SimpleTargetContext):
        pass


    # Enter a parse tree produced by AiLangParser#memberTarget.
    def enterMemberTarget(self, ctx:AiLangParser.MemberTargetContext):
        pass

    # Exit a parse tree produced by AiLangParser#memberTarget.
    def exitMemberTarget(self, ctx:AiLangParser.MemberTargetContext):
        pass


    # Enter a parse tree produced by AiLangParser#named_arg.
    def enterNamed_arg(self, ctx:AiLangParser.Named_argContext):
        pass

    # Exit a parse tree produced by AiLangParser#named_arg.
    def exitNamed_arg(self, ctx:AiLangParser.Named_argContext):
        pass


    # Enter a parse tree produced by AiLangParser#NamedArg.
    def enterNamedArg(self, ctx:AiLangParser.NamedArgContext):
        pass

    # Exit a parse tree produced by AiLangParser#NamedArg.
    def exitNamedArg(self, ctx:AiLangParser.NamedArgContext):
        pass


    # Enter a parse tree produced by AiLangParser#ExprArg.
    def enterExprArg(self, ctx:AiLangParser.ExprArgContext):
        pass

    # Exit a parse tree produced by AiLangParser#ExprArg.
    def exitExprArg(self, ctx:AiLangParser.ExprArgContext):
        pass


    # Enter a parse tree produced by AiLangParser#arg_list.
    def enterArg_list(self, ctx:AiLangParser.Arg_listContext):
        pass

    # Exit a parse tree produced by AiLangParser#arg_list.
    def exitArg_list(self, ctx:AiLangParser.Arg_listContext):
        pass


    # Enter a parse tree produced by AiLangParser#generic_list.
    def enterGeneric_list(self, ctx:AiLangParser.Generic_listContext):
        pass

    # Exit a parse tree produced by AiLangParser#generic_list.
    def exitGeneric_list(self, ctx:AiLangParser.Generic_listContext):
        pass


    # Enter a parse tree produced by AiLangParser#list.
    def enterList(self, ctx:AiLangParser.ListContext):
        pass

    # Exit a parse tree produced by AiLangParser#list.
    def exitList(self, ctx:AiLangParser.ListContext):
        pass


    # Enter a parse tree produced by AiLangParser#NonEmptyDf.
    def enterNonEmptyDf(self, ctx:AiLangParser.NonEmptyDfContext):
        pass

    # Exit a parse tree produced by AiLangParser#NonEmptyDf.
    def exitNonEmptyDf(self, ctx:AiLangParser.NonEmptyDfContext):
        pass


    # Enter a parse tree produced by AiLangParser#EmptyDf.
    def enterEmptyDf(self, ctx:AiLangParser.EmptyDfContext):
        pass

    # Exit a parse tree produced by AiLangParser#EmptyDf.
    def exitEmptyDf(self, ctx:AiLangParser.EmptyDfContext):
        pass


    # Enter a parse tree produced by AiLangParser#df_val.
    def enterDf_val(self, ctx:AiLangParser.Df_valContext):
        pass

    # Exit a parse tree produced by AiLangParser#df_val.
    def exitDf_val(self, ctx:AiLangParser.Df_valContext):
        pass


    # Enter a parse tree produced by AiLangParser#basicIDMember.
    def enterBasicIDMember(self, ctx:AiLangParser.BasicIDMemberContext):
        pass

    # Exit a parse tree produced by AiLangParser#basicIDMember.
    def exitBasicIDMember(self, ctx:AiLangParser.BasicIDMemberContext):
        pass


    # Enter a parse tree produced by AiLangParser#intIDMember.
    def enterIntIDMember(self, ctx:AiLangParser.IntIDMemberContext):
        pass

    # Exit a parse tree produced by AiLangParser#intIDMember.
    def exitIntIDMember(self, ctx:AiLangParser.IntIDMemberContext):
        pass


    # Enter a parse tree produced by AiLangParser#listIDMember.
    def enterListIDMember(self, ctx:AiLangParser.ListIDMemberContext):
        pass

    # Exit a parse tree produced by AiLangParser#listIDMember.
    def exitListIDMember(self, ctx:AiLangParser.ListIDMemberContext):
        pass


    # Enter a parse tree produced by AiLangParser#numList.
    def enterNumList(self, ctx:AiLangParser.NumListContext):
        pass

    # Exit a parse tree produced by AiLangParser#numList.
    def exitNumList(self, ctx:AiLangParser.NumListContext):
        pass


    # Enter a parse tree produced by AiLangParser#strList.
    def enterStrList(self, ctx:AiLangParser.StrListContext):
        pass

    # Exit a parse tree produced by AiLangParser#strList.
    def exitStrList(self, ctx:AiLangParser.StrListContext):
        pass


    # Enter a parse tree produced by AiLangParser#number.
    def enterNumber(self, ctx:AiLangParser.NumberContext):
        pass

    # Exit a parse tree produced by AiLangParser#number.
    def exitNumber(self, ctx:AiLangParser.NumberContext):
        pass


    # Enter a parse tree produced by AiLangParser#string.
    def enterString(self, ctx:AiLangParser.StringContext):
        pass

    # Exit a parse tree produced by AiLangParser#string.
    def exitString(self, ctx:AiLangParser.StringContext):
        pass


    # Enter a parse tree produced by AiLangParser#group_basic_val.
    def enterGroup_basic_val(self, ctx:AiLangParser.Group_basic_valContext):
        pass

    # Exit a parse tree produced by AiLangParser#group_basic_val.
    def exitGroup_basic_val(self, ctx:AiLangParser.Group_basic_valContext):
        pass


    # Enter a parse tree produced by AiLangParser#intigerLiteral.
    def enterIntigerLiteral(self, ctx:AiLangParser.IntigerLiteralContext):
        pass

    # Exit a parse tree produced by AiLangParser#intigerLiteral.
    def exitIntigerLiteral(self, ctx:AiLangParser.IntigerLiteralContext):
        pass


    # Enter a parse tree produced by AiLangParser#floatLiteral.
    def enterFloatLiteral(self, ctx:AiLangParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by AiLangParser#floatLiteral.
    def exitFloatLiteral(self, ctx:AiLangParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by AiLangParser#str.
    def enterStr(self, ctx:AiLangParser.StrContext):
        pass

    # Exit a parse tree produced by AiLangParser#str.
    def exitStr(self, ctx:AiLangParser.StrContext):
        pass



del AiLangParser