# Generated from ./AiLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,30,308,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,4,0,62,8,0,11,0,12,0,63,1,1,1,
        1,3,1,68,8,1,1,1,1,1,1,1,1,1,3,1,74,8,1,1,1,1,1,3,1,78,8,1,1,2,1,
        2,1,2,1,3,1,3,5,3,85,8,3,10,3,12,3,88,9,3,1,3,1,3,1,4,1,4,5,4,94,
        8,4,10,4,12,4,97,9,4,1,4,1,4,1,5,1,5,1,5,5,5,104,8,5,10,5,12,5,107,
        9,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,3,10,126,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        3,11,136,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,145,8,12,10,
        12,12,12,148,9,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,
        14,1,14,1,14,1,14,1,14,3,14,164,8,14,1,15,1,15,1,15,1,15,3,15,170,
        8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,182,
        8,16,1,16,1,16,1,16,1,16,1,16,1,16,5,16,190,8,16,10,16,12,16,193,
        9,16,1,17,1,17,1,17,1,17,1,17,1,17,5,17,201,8,17,10,17,12,17,204,
        9,17,1,18,1,18,1,18,1,18,1,19,1,19,3,19,212,8,19,1,20,1,20,1,20,
        1,20,5,20,218,8,20,10,20,12,20,221,9,20,3,20,223,8,20,1,20,1,20,
        1,21,1,21,1,21,1,21,5,21,231,8,21,10,21,12,21,234,9,21,1,21,1,21,
        1,22,1,22,3,22,240,8,22,1,23,1,23,1,23,1,23,5,23,246,8,23,10,23,
        12,23,249,9,23,1,23,1,23,1,23,1,23,3,23,255,8,23,1,24,1,24,1,24,
        3,24,260,8,24,1,24,1,24,1,25,1,25,1,25,1,25,3,25,268,8,25,1,26,1,
        26,1,26,1,26,5,26,274,8,26,10,26,12,26,277,9,26,1,26,1,26,1,26,1,
        26,1,26,1,26,5,26,285,8,26,10,26,12,26,288,9,26,1,26,1,26,3,26,292,
        8,26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,300,8,27,1,28,1,28,3,28,
        304,8,28,1,29,1,29,1,29,0,2,32,34,30,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,0,0,319,
        0,61,1,0,0,0,2,77,1,0,0,0,4,79,1,0,0,0,6,82,1,0,0,0,8,91,1,0,0,0,
        10,100,1,0,0,0,12,108,1,0,0,0,14,112,1,0,0,0,16,116,1,0,0,0,18,118,
        1,0,0,0,20,125,1,0,0,0,22,135,1,0,0,0,24,137,1,0,0,0,26,152,1,0,
        0,0,28,157,1,0,0,0,30,165,1,0,0,0,32,181,1,0,0,0,34,194,1,0,0,0,
        36,205,1,0,0,0,38,211,1,0,0,0,40,213,1,0,0,0,42,226,1,0,0,0,44,239,
        1,0,0,0,46,254,1,0,0,0,48,259,1,0,0,0,50,267,1,0,0,0,52,291,1,0,
        0,0,54,299,1,0,0,0,56,303,1,0,0,0,58,305,1,0,0,0,60,62,3,22,11,0,
        61,60,1,0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,1,1,0,
        0,0,65,67,5,19,0,0,66,68,3,4,2,0,67,66,1,0,0,0,67,68,1,0,0,0,68,
        69,1,0,0,0,69,78,3,6,3,0,70,71,3,4,2,0,71,73,5,19,0,0,72,74,3,4,
        2,0,73,72,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,76,3,6,3,0,76,78,
        1,0,0,0,77,65,1,0,0,0,77,70,1,0,0,0,78,3,1,0,0,0,79,80,5,1,0,0,80,
        81,3,16,8,0,81,5,1,0,0,0,82,86,5,2,0,0,83,85,3,22,11,0,84,83,1,0,
        0,0,85,88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,
        1,0,0,0,89,90,5,3,0,0,90,7,1,0,0,0,91,95,5,2,0,0,92,94,3,10,5,0,
        93,92,1,0,0,0,94,97,1,0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,
        0,0,0,97,95,1,0,0,0,98,99,5,3,0,0,99,9,1,0,0,0,100,105,3,12,6,0,
        101,102,5,22,0,0,102,104,3,12,6,0,103,101,1,0,0,0,104,107,1,0,0,
        0,105,103,1,0,0,0,105,106,1,0,0,0,106,11,1,0,0,0,107,105,1,0,0,0,
        108,109,3,32,16,0,109,110,5,22,0,0,110,111,3,32,16,0,111,13,1,0,
        0,0,112,113,3,34,17,0,113,114,5,4,0,0,114,115,3,32,16,0,115,15,1,
        0,0,0,116,117,5,26,0,0,117,17,1,0,0,0,118,119,3,34,17,0,119,120,
        5,20,0,0,120,121,3,32,16,0,121,19,1,0,0,0,122,126,5,13,0,0,123,124,
        5,13,0,0,124,126,3,32,16,0,125,122,1,0,0,0,125,123,1,0,0,0,126,21,
        1,0,0,0,127,136,3,24,12,0,128,136,3,14,7,0,129,136,3,18,9,0,130,
        136,3,32,16,0,131,136,3,2,1,0,132,136,3,28,14,0,133,136,3,26,13,
        0,134,136,3,20,10,0,135,127,1,0,0,0,135,128,1,0,0,0,135,129,1,0,
        0,0,135,130,1,0,0,0,135,131,1,0,0,0,135,132,1,0,0,0,135,133,1,0,
        0,0,135,134,1,0,0,0,136,23,1,0,0,0,137,138,5,18,0,0,138,139,3,16,
        8,0,139,140,5,20,0,0,140,141,5,5,0,0,141,146,3,16,8,0,142,143,5,
        6,0,0,143,145,3,16,8,0,144,142,1,0,0,0,145,148,1,0,0,0,146,144,1,
        0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,146,1,0,0,0,149,150,5,
        7,0,0,150,151,3,6,3,0,151,25,1,0,0,0,152,153,5,17,0,0,153,154,3,
        58,29,0,154,155,5,19,0,0,155,156,3,16,8,0,156,27,1,0,0,0,157,158,
        5,14,0,0,158,159,3,6,3,0,159,160,5,15,0,0,160,163,3,8,4,0,161,162,
        5,16,0,0,162,164,3,6,3,0,163,161,1,0,0,0,163,164,1,0,0,0,164,29,
        1,0,0,0,165,166,5,8,0,0,166,169,3,16,8,0,167,168,5,20,0,0,168,170,
        3,40,20,0,169,167,1,0,0,0,169,170,1,0,0,0,170,31,1,0,0,0,171,172,
        6,16,-1,0,172,182,3,54,27,0,173,182,3,34,17,0,174,182,3,30,15,0,
        175,182,3,44,22,0,176,182,3,46,23,0,177,178,5,5,0,0,178,179,3,32,
        16,0,179,180,5,7,0,0,180,182,1,0,0,0,181,171,1,0,0,0,181,173,1,0,
        0,0,181,174,1,0,0,0,181,175,1,0,0,0,181,176,1,0,0,0,181,177,1,0,
        0,0,182,191,1,0,0,0,183,184,10,1,0,0,184,185,5,21,0,0,185,190,3,
        32,16,2,186,187,10,2,0,0,187,188,5,20,0,0,188,190,3,40,20,0,189,
        183,1,0,0,0,189,186,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,
        192,1,0,0,0,192,33,1,0,0,0,193,191,1,0,0,0,194,195,6,17,-1,0,195,
        196,3,16,8,0,196,202,1,0,0,0,197,198,10,1,0,0,198,199,5,8,0,0,199,
        201,3,50,25,0,200,197,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,
        203,1,0,0,0,203,35,1,0,0,0,204,202,1,0,0,0,205,206,3,16,8,0,206,
        207,5,9,0,0,207,208,3,32,16,0,208,37,1,0,0,0,209,212,3,36,18,0,210,
        212,3,32,16,0,211,209,1,0,0,0,211,210,1,0,0,0,212,39,1,0,0,0,213,
        222,5,5,0,0,214,219,3,38,19,0,215,216,5,6,0,0,216,218,3,38,19,0,
        217,215,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,
        220,223,1,0,0,0,221,219,1,0,0,0,222,214,1,0,0,0,222,223,1,0,0,0,
        223,224,1,0,0,0,224,225,5,7,0,0,225,41,1,0,0,0,226,227,5,5,0,0,227,
        232,3,32,16,0,228,229,5,6,0,0,229,231,3,32,16,0,230,228,1,0,0,0,
        231,234,1,0,0,0,232,230,1,0,0,0,232,233,1,0,0,0,233,235,1,0,0,0,
        234,232,1,0,0,0,235,236,5,7,0,0,236,43,1,0,0,0,237,240,3,52,26,0,
        238,240,3,42,21,0,239,237,1,0,0,0,239,238,1,0,0,0,240,45,1,0,0,0,
        241,242,5,10,0,0,242,247,3,48,24,0,243,244,5,6,0,0,244,246,3,48,
        24,0,245,243,1,0,0,0,246,249,1,0,0,0,247,245,1,0,0,0,247,248,1,0,
        0,0,248,250,1,0,0,0,249,247,1,0,0,0,250,251,5,11,0,0,251,255,1,0,
        0,0,252,253,5,10,0,0,253,255,5,11,0,0,254,241,1,0,0,0,254,252,1,
        0,0,0,255,47,1,0,0,0,256,257,3,16,8,0,257,258,5,12,0,0,258,260,1,
        0,0,0,259,256,1,0,0,0,259,260,1,0,0,0,260,261,1,0,0,0,261,262,3,
        52,26,0,262,49,1,0,0,0,263,268,3,16,8,0,264,268,5,25,0,0,265,266,
        5,1,0,0,266,268,3,16,8,0,267,263,1,0,0,0,267,264,1,0,0,0,267,265,
        1,0,0,0,268,51,1,0,0,0,269,270,5,5,0,0,270,275,3,56,28,0,271,272,
        5,6,0,0,272,274,3,56,28,0,273,271,1,0,0,0,274,277,1,0,0,0,275,273,
        1,0,0,0,275,276,1,0,0,0,276,278,1,0,0,0,277,275,1,0,0,0,278,279,
        5,7,0,0,279,292,1,0,0,0,280,281,5,5,0,0,281,286,3,58,29,0,282,283,
        5,6,0,0,283,285,3,58,29,0,284,282,1,0,0,0,285,288,1,0,0,0,286,284,
        1,0,0,0,286,287,1,0,0,0,287,289,1,0,0,0,288,286,1,0,0,0,289,290,
        5,7,0,0,290,292,1,0,0,0,291,269,1,0,0,0,291,280,1,0,0,0,292,53,1,
        0,0,0,293,300,3,56,28,0,294,300,3,58,29,0,295,296,5,5,0,0,296,297,
        3,54,27,0,297,298,5,7,0,0,298,300,1,0,0,0,299,293,1,0,0,0,299,294,
        1,0,0,0,299,295,1,0,0,0,300,55,1,0,0,0,301,304,5,25,0,0,302,304,
        5,24,0,0,303,301,1,0,0,0,303,302,1,0,0,0,304,57,1,0,0,0,305,306,
        5,23,0,0,306,59,1,0,0,0,30,63,67,73,77,86,95,105,125,135,146,163,
        169,181,189,191,202,211,219,222,232,239,247,254,259,267,275,286,
        291,299,303
    ]

class AiLangParser ( Parser ):

    grammarFileName = "AiLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@'", "'{'", "'}'", "':='", "'('", "','", 
                     "')'", "'.'", "'='", "'['", "']'", "':'", "'return'", 
                     "'do'", "'if'", "'else'", "'from'", "'function'", "'->'", 
                     "'<-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "RETURN", "DO", "IF", "ELSE", "FROM", 
                      "FUNCTION", "ARR", "REF", "MATH_OP", "BOOL_OP", "STR", 
                      "FLOAT", "INT", "ID", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "NL", "WS" ]

    RULE_prog = 0
    RULE_block = 1
    RULE_label = 2
    RULE_context = 3
    RULE_bool_context = 4
    RULE_bool_group = 5
    RULE_bool_stat = 6
    RULE_assignment = 7
    RULE_id = 8
    RULE_ref_op = 9
    RULE_ret = 10
    RULE_stat = 11
    RULE_func_def = 12
    RULE_fromToData = 13
    RULE_doIfElse = 14
    RULE_func = 15
    RULE_expr = 16
    RULE_assignable = 17
    RULE_named_arg = 18
    RULE_arg = 19
    RULE_arg_list = 20
    RULE_generic_list = 21
    RULE_list = 22
    RULE_df = 23
    RULE_df_val = 24
    RULE_member = 25
    RULE_basic_list = 26
    RULE_basic_val = 27
    RULE_num = 28
    RULE_str = 29

    ruleNames =  [ "prog", "block", "label", "context", "bool_context", 
                   "bool_group", "bool_stat", "assignment", "id", "ref_op", 
                   "ret", "stat", "func_def", "fromToData", "doIfElse", 
                   "func", "expr", "assignable", "named_arg", "arg", "arg_list", 
                   "generic_list", "list", "df", "df_val", "member", "basic_list", 
                   "basic_val", "num", "str" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    RETURN=13
    DO=14
    IF=15
    ELSE=16
    FROM=17
    FUNCTION=18
    ARR=19
    REF=20
    MATH_OP=21
    BOOL_OP=22
    STR=23
    FLOAT=24
    INT=25
    ID=26
    LINE_COMMENT=27
    BLOCK_COMMENT=28
    NL=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.StatContext)
            else:
                return self.getTypedRuleContext(AiLangParser.StatContext,i)


        def getRuleIndex(self):
            return AiLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = AiLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.stat()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 126772514) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AiLangParser.RULE_block

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Label2BlockContext(BlockContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.BlockContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.LabelContext)
            else:
                return self.getTypedRuleContext(AiLangParser.LabelContext,i)

        def ARR(self):
            return self.getToken(AiLangParser.ARR, 0)
        def context(self):
            return self.getTypedRuleContext(AiLangParser.ContextContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel2Block" ):
                listener.enterLabel2Block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel2Block" ):
                listener.exitLabel2Block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel2Block" ):
                return visitor.visitLabel2Block(self)
            else:
                return visitor.visitChildren(self)


    class Block2BlockContext(BlockContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.BlockContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ARR(self):
            return self.getToken(AiLangParser.ARR, 0)
        def context(self):
            return self.getTypedRuleContext(AiLangParser.ContextContext,0)

        def label(self):
            return self.getTypedRuleContext(AiLangParser.LabelContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock2Block" ):
                listener.enterBlock2Block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock2Block" ):
                listener.exitBlock2Block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock2Block" ):
                return visitor.visitBlock2Block(self)
            else:
                return visitor.visitChildren(self)



    def block(self):

        localctx = AiLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = AiLangParser.Block2BlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.match(AiLangParser.ARR)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 66
                    self.label()


                self.state = 69
                self.context()
                pass
            elif token in [1]:
                localctx = AiLangParser.Label2BlockContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.label()
                self.state = 71
                self.match(AiLangParser.ARR)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 72
                    self.label()


                self.state = 75
                self.context()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


        def getRuleIndex(self):
            return AiLangParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = AiLangParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(AiLangParser.T__0)
            self.state = 80
            self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.StatContext)
            else:
                return self.getTypedRuleContext(AiLangParser.StatContext,i)


        def getRuleIndex(self):
            return AiLangParser.RULE_context

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContext" ):
                listener.enterContext(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContext" ):
                listener.exitContext(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContext" ):
                return visitor.visitContext(self)
            else:
                return visitor.visitChildren(self)




    def context(self):

        localctx = AiLangParser.ContextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_context)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(AiLangParser.T__1)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 126772514) != 0):
                self.state = 83
                self.stat()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(AiLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_contextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bool_group(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.Bool_groupContext)
            else:
                return self.getTypedRuleContext(AiLangParser.Bool_groupContext,i)


        def getRuleIndex(self):
            return AiLangParser.RULE_bool_context

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_context" ):
                listener.enterBool_context(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_context" ):
                listener.exitBool_context(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_context" ):
                return visitor.visitBool_context(self)
            else:
                return visitor.visitChildren(self)




    def bool_context(self):

        localctx = AiLangParser.Bool_contextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bool_context)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(AiLangParser.T__1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 125830432) != 0):
                self.state = 92
                self.bool_group()
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.match(AiLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_groupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bool_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.Bool_statContext)
            else:
                return self.getTypedRuleContext(AiLangParser.Bool_statContext,i)


        def BOOL_OP(self, i:int=None):
            if i is None:
                return self.getTokens(AiLangParser.BOOL_OP)
            else:
                return self.getToken(AiLangParser.BOOL_OP, i)

        def getRuleIndex(self):
            return AiLangParser.RULE_bool_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_group" ):
                listener.enterBool_group(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_group" ):
                listener.exitBool_group(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_group" ):
                return visitor.visitBool_group(self)
            else:
                return visitor.visitChildren(self)




    def bool_group(self):

        localctx = AiLangParser.Bool_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bool_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.bool_stat()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 101
                self.match(AiLangParser.BOOL_OP)
                self.state = 102
                self.bool_stat()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(AiLangParser.ExprContext,i)


        def BOOL_OP(self):
            return self.getToken(AiLangParser.BOOL_OP, 0)

        def getRuleIndex(self):
            return AiLangParser.RULE_bool_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_stat" ):
                listener.enterBool_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_stat" ):
                listener.exitBool_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_stat" ):
                return visitor.visitBool_stat(self)
            else:
                return visitor.visitChildren(self)




    def bool_stat(self):

        localctx = AiLangParser.Bool_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_bool_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.expr(0)
            self.state = 109
            self.match(AiLangParser.BOOL_OP)
            self.state = 110
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignable(self):
            return self.getTypedRuleContext(AiLangParser.AssignableContext,0)


        def expr(self):
            return self.getTypedRuleContext(AiLangParser.ExprContext,0)


        def getRuleIndex(self):
            return AiLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = AiLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.assignable(0)
            self.state = 113
            self.match(AiLangParser.T__3)
            self.state = 114
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(AiLangParser.ID, 0)

        def getRuleIndex(self):
            return AiLangParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)




    def id_(self):

        localctx = AiLangParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(AiLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ref_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignable(self):
            return self.getTypedRuleContext(AiLangParser.AssignableContext,0)


        def REF(self):
            return self.getToken(AiLangParser.REF, 0)

        def expr(self):
            return self.getTypedRuleContext(AiLangParser.ExprContext,0)


        def getRuleIndex(self):
            return AiLangParser.RULE_ref_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRef_op" ):
                listener.enterRef_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRef_op" ):
                listener.exitRef_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRef_op" ):
                return visitor.visitRef_op(self)
            else:
                return visitor.visitChildren(self)




    def ref_op(self):

        localctx = AiLangParser.Ref_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ref_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.assignable(0)
            self.state = 119
            self.match(AiLangParser.REF)
            self.state = 120
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AiLangParser.RULE_ret

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprReturnContext(RetContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.RetContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(AiLangParser.RETURN, 0)
        def expr(self):
            return self.getTypedRuleContext(AiLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprReturn" ):
                listener.enterExprReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprReturn" ):
                listener.exitExprReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprReturn" ):
                return visitor.visitExprReturn(self)
            else:
                return visitor.visitChildren(self)


    class NoneReturnContext(RetContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.RetContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def RETURN(self):
            return self.getToken(AiLangParser.RETURN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoneReturn" ):
                listener.enterNoneReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoneReturn" ):
                listener.exitNoneReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoneReturn" ):
                return visitor.visitNoneReturn(self)
            else:
                return visitor.visitChildren(self)



    def ret(self):

        localctx = AiLangParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ret)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = AiLangParser.NoneReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.match(AiLangParser.RETURN)
                pass

            elif la_ == 2:
                localctx = AiLangParser.ExprReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(AiLangParser.RETURN)
                self.state = 124
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AiLangParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReferenceContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ref_op(self):
            return self.getTypedRuleContext(AiLangParser.Ref_opContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReference" ):
                listener.enterReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReference" ):
                listener.exitReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReference" ):
                return visitor.visitReference(self)
            else:
                return visitor.visitChildren(self)


    class Do_if_elseContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def doIfElse(self):
            return self.getTypedRuleContext(AiLangParser.DoIfElseContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo_if_else" ):
                listener.enterDo_if_else(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo_if_else" ):
                listener.exitDo_if_else(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_if_else" ):
                return visitor.visitDo_if_else(self)
            else:
                return visitor.visitChildren(self)


    class FunctionDefContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func_def(self):
            return self.getTypedRuleContext(AiLangParser.Func_defContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDef" ):
                return visitor.visitFunctionDef(self)
            else:
                return visitor.visitChildren(self)


    class Block_statContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(AiLangParser.BlockContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_stat" ):
                listener.enterBlock_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_stat" ):
                listener.exitBlock_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stat" ):
                return visitor.visitBlock_stat(self)
            else:
                return visitor.visitChildren(self)


    class Load_opContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fromToData(self):
            return self.getTypedRuleContext(AiLangParser.FromToDataContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoad_op" ):
                listener.enterLoad_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoad_op" ):
                listener.exitLoad_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoad_op" ):
                return visitor.visitLoad_op(self)
            else:
                return visitor.visitChildren(self)


    class ReturnContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ret(self):
            return self.getTypedRuleContext(AiLangParser.RetContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(AiLangParser.AssignmentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AiLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = AiLangParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stat)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = AiLangParser.FunctionDefContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.func_def()
                pass

            elif la_ == 2:
                localctx = AiLangParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.assignment()
                pass

            elif la_ == 3:
                localctx = AiLangParser.ReferenceContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.ref_op()
                pass

            elif la_ == 4:
                localctx = AiLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = AiLangParser.Block_statContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 131
                self.block()
                pass

            elif la_ == 6:
                localctx = AiLangParser.Do_if_elseContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 132
                self.doIfElse()
                pass

            elif la_ == 7:
                localctx = AiLangParser.Load_opContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 133
                self.fromToData()
                pass

            elif la_ == 8:
                localctx = AiLangParser.ReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 134
                self.ret()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(AiLangParser.FUNCTION, 0)

        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.IdContext)
            else:
                return self.getTypedRuleContext(AiLangParser.IdContext,i)


        def REF(self):
            return self.getToken(AiLangParser.REF, 0)

        def context(self):
            return self.getTypedRuleContext(AiLangParser.ContextContext,0)


        def getRuleIndex(self):
            return AiLangParser.RULE_func_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_def" ):
                listener.enterFunc_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_def" ):
                listener.exitFunc_def(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_def" ):
                return visitor.visitFunc_def(self)
            else:
                return visitor.visitChildren(self)




    def func_def(self):

        localctx = AiLangParser.Func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.match(AiLangParser.FUNCTION)
            self.state = 138
            self.id_()
            self.state = 139
            self.match(AiLangParser.REF)
            self.state = 140
            self.match(AiLangParser.T__4)
            self.state = 141
            self.id_()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 142
                self.match(AiLangParser.T__5)
                self.state = 143
                self.id_()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 149
            self.match(AiLangParser.T__6)
            self.state = 150
            self.context()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FromToDataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(AiLangParser.FROM, 0)

        def str_(self):
            return self.getTypedRuleContext(AiLangParser.StrContext,0)


        def ARR(self):
            return self.getToken(AiLangParser.ARR, 0)

        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


        def getRuleIndex(self):
            return AiLangParser.RULE_fromToData

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFromToData" ):
                listener.enterFromToData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFromToData" ):
                listener.exitFromToData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFromToData" ):
                return visitor.visitFromToData(self)
            else:
                return visitor.visitChildren(self)




    def fromToData(self):

        localctx = AiLangParser.FromToDataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_fromToData)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(AiLangParser.FROM)
            self.state = 153
            self.str_()
            self.state = 154
            self.match(AiLangParser.ARR)
            self.state = 155
            self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoIfElseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(AiLangParser.DO, 0)

        def context(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.ContextContext)
            else:
                return self.getTypedRuleContext(AiLangParser.ContextContext,i)


        def IF(self):
            return self.getToken(AiLangParser.IF, 0)

        def bool_context(self):
            return self.getTypedRuleContext(AiLangParser.Bool_contextContext,0)


        def ELSE(self):
            return self.getToken(AiLangParser.ELSE, 0)

        def getRuleIndex(self):
            return AiLangParser.RULE_doIfElse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoIfElse" ):
                listener.enterDoIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoIfElse" ):
                listener.exitDoIfElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoIfElse" ):
                return visitor.visitDoIfElse(self)
            else:
                return visitor.visitChildren(self)




    def doIfElse(self):

        localctx = AiLangParser.DoIfElseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_doIfElse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(AiLangParser.DO)
            self.state = 158
            self.context()
            self.state = 159
            self.match(AiLangParser.IF)
            self.state = 160
            self.bool_context()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 161
                self.match(AiLangParser.ELSE)
                self.state = 162
                self.context()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


        def REF(self):
            return self.getToken(AiLangParser.REF, 0)

        def arg_list(self):
            return self.getTypedRuleContext(AiLangParser.Arg_listContext,0)


        def getRuleIndex(self):
            return AiLangParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = AiLangParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(AiLangParser.T__7)
            self.state = 166
            self.id_()
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 167
                self.match(AiLangParser.REF)
                self.state = 168
                self.arg_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AiLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MathOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(AiLangParser.ExprContext,i)

        def MATH_OP(self):
            return self.getToken(AiLangParser.MATH_OP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathOp" ):
                listener.enterMathOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathOp" ):
                listener.exitMathOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathOp" ):
                return visitor.visitMathOp(self)
            else:
                return visitor.visitChildren(self)


    class BasicValExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def basic_val(self):
            return self.getTypedRuleContext(AiLangParser.Basic_valContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasicValExpr" ):
                listener.enterBasicValExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasicValExpr" ):
                listener.exitBasicValExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicValExpr" ):
                return visitor.visitBasicValExpr(self)
            else:
                return visitor.visitChildren(self)


    class PathExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignable(self):
            return self.getTypedRuleContext(AiLangParser.AssignableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPathExpr" ):
                listener.enterPathExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPathExpr" ):
                listener.exitPathExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPathExpr" ):
                return visitor.visitPathExpr(self)
            else:
                return visitor.visitChildren(self)


    class FunctionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func(self):
            return self.getTypedRuleContext(AiLangParser.FuncContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)


    class ListValExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def list_(self):
            return self.getTypedRuleContext(AiLangParser.ListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListValExpr" ):
                listener.enterListValExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListValExpr" ):
                listener.exitListValExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListValExpr" ):
                return visitor.visitListValExpr(self)
            else:
                return visitor.visitChildren(self)


    class DataframeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def df(self):
            return self.getTypedRuleContext(AiLangParser.DfContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataframe" ):
                listener.enterDataframe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataframe" ):
                listener.exitDataframe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataframe" ):
                return visitor.visitDataframe(self)
            else:
                return visitor.visitChildren(self)


    class GroupContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AiLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup" ):
                listener.enterGroup(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup" ):
                listener.exitGroup(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroup" ):
                return visitor.visitGroup(self)
            else:
                return visitor.visitChildren(self)


    class MethodCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AiLangParser.ExprContext,0)

        def REF(self):
            return self.getToken(AiLangParser.REF, 0)
        def arg_list(self):
            return self.getTypedRuleContext(AiLangParser.Arg_listContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodCall" ):
                listener.enterMethodCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodCall" ):
                listener.exitMethodCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AiLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = AiLangParser.BasicValExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 172
                self.basic_val()
                pass

            elif la_ == 2:
                localctx = AiLangParser.PathExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 173
                self.assignable(0)
                pass

            elif la_ == 3:
                localctx = AiLangParser.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 174
                self.func()
                pass

            elif la_ == 4:
                localctx = AiLangParser.ListValExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 175
                self.list_()
                pass

            elif la_ == 5:
                localctx = AiLangParser.DataframeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 176
                self.df()
                pass

            elif la_ == 6:
                localctx = AiLangParser.GroupContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 177
                self.match(AiLangParser.T__4)
                self.state = 178
                self.expr(0)
                self.state = 179
                self.match(AiLangParser.T__6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 191
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 189
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = AiLangParser.MathOpContext(self, AiLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 183
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 184
                        self.match(AiLangParser.MATH_OP)
                        self.state = 185
                        self.expr(2)
                        pass

                    elif la_ == 2:
                        localctx = AiLangParser.MethodCallContext(self, AiLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 186
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 187
                        self.match(AiLangParser.REF)
                        self.state = 188
                        self.arg_list()
                        pass

             
                self.state = 193
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AiLangParser.RULE_assignable

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SimpleTargetContext(AssignableContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.AssignableContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleTarget" ):
                listener.enterSimpleTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleTarget" ):
                listener.exitSimpleTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleTarget" ):
                return visitor.visitSimpleTarget(self)
            else:
                return visitor.visitChildren(self)


    class MemberTargetContext(AssignableContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.AssignableContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignable(self):
            return self.getTypedRuleContext(AiLangParser.AssignableContext,0)

        def member(self):
            return self.getTypedRuleContext(AiLangParser.MemberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberTarget" ):
                listener.enterMemberTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberTarget" ):
                listener.exitMemberTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberTarget" ):
                return visitor.visitMemberTarget(self)
            else:
                return visitor.visitChildren(self)



    def assignable(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AiLangParser.AssignableContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_assignable, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AiLangParser.SimpleTargetContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 195
            self.id_()
            self._ctx.stop = self._input.LT(-1)
            self.state = 202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AiLangParser.MemberTargetContext(self, AiLangParser.AssignableContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable)
                    self.state = 197
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 198
                    self.match(AiLangParser.T__7)
                    self.state = 199
                    self.member() 
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Named_argContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


        def expr(self):
            return self.getTypedRuleContext(AiLangParser.ExprContext,0)


        def getRuleIndex(self):
            return AiLangParser.RULE_named_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamed_arg" ):
                listener.enterNamed_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamed_arg" ):
                listener.exitNamed_arg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamed_arg" ):
                return visitor.visitNamed_arg(self)
            else:
                return visitor.visitChildren(self)




    def named_arg(self):

        localctx = AiLangParser.Named_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_named_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.id_()
            self.state = 206
            self.match(AiLangParser.T__8)
            self.state = 207
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AiLangParser.RULE_arg

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprArgContext(ArgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ArgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AiLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprArg" ):
                listener.enterExprArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprArg" ):
                listener.exitExprArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprArg" ):
                return visitor.visitExprArg(self)
            else:
                return visitor.visitChildren(self)


    class NamedArgContext(ArgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ArgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def named_arg(self):
            return self.getTypedRuleContext(AiLangParser.Named_argContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamedArg" ):
                listener.enterNamedArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamedArg" ):
                listener.exitNamedArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNamedArg" ):
                return visitor.visitNamedArg(self)
            else:
                return visitor.visitChildren(self)



    def arg(self):

        localctx = AiLangParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_arg)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = AiLangParser.NamedArgContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.named_arg()
                pass

            elif la_ == 2:
                localctx = AiLangParser.ExprArgContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.ArgContext)
            else:
                return self.getTypedRuleContext(AiLangParser.ArgContext,i)


        def getRuleIndex(self):
            return AiLangParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_list" ):
                return visitor.visitArg_list(self)
            else:
                return visitor.visitChildren(self)




    def arg_list(self):

        localctx = AiLangParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(AiLangParser.T__4)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 125830432) != 0):
                self.state = 214
                self.arg()
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 215
                    self.match(AiLangParser.T__5)
                    self.state = 216
                    self.arg()
                    self.state = 221
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 224
            self.match(AiLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Generic_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(AiLangParser.ExprContext,i)


        def getRuleIndex(self):
            return AiLangParser.RULE_generic_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeneric_list" ):
                listener.enterGeneric_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeneric_list" ):
                listener.exitGeneric_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGeneric_list" ):
                return visitor.visitGeneric_list(self)
            else:
                return visitor.visitChildren(self)




    def generic_list(self):

        localctx = AiLangParser.Generic_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_generic_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(AiLangParser.T__4)
            self.state = 227
            self.expr(0)
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 228
                self.match(AiLangParser.T__5)
                self.state = 229
                self.expr(0)
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 235
            self.match(AiLangParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_list(self):
            return self.getTypedRuleContext(AiLangParser.Basic_listContext,0)


        def generic_list(self):
            return self.getTypedRuleContext(AiLangParser.Generic_listContext,0)


        def getRuleIndex(self):
            return AiLangParser.RULE_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList" ):
                listener.enterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList" ):
                listener.exitList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)




    def list_(self):

        localctx = AiLangParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.basic_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.generic_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AiLangParser.RULE_df

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EmptyDfContext(DfContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.DfContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyDf" ):
                listener.enterEmptyDf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyDf" ):
                listener.exitEmptyDf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyDf" ):
                return visitor.visitEmptyDf(self)
            else:
                return visitor.visitChildren(self)


    class NonEmptyDfContext(DfContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.DfContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def df_val(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.Df_valContext)
            else:
                return self.getTypedRuleContext(AiLangParser.Df_valContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonEmptyDf" ):
                listener.enterNonEmptyDf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonEmptyDf" ):
                listener.exitNonEmptyDf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonEmptyDf" ):
                return visitor.visitNonEmptyDf(self)
            else:
                return visitor.visitChildren(self)



    def df(self):

        localctx = AiLangParser.DfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_df)
        self._la = 0 # Token type
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = AiLangParser.NonEmptyDfContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(AiLangParser.T__9)
                self.state = 242
                self.df_val()
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 243
                    self.match(AiLangParser.T__5)
                    self.state = 244
                    self.df_val()
                    self.state = 249
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 250
                self.match(AiLangParser.T__10)
                pass

            elif la_ == 2:
                localctx = AiLangParser.EmptyDfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.match(AiLangParser.T__9)
                self.state = 253
                self.match(AiLangParser.T__10)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Df_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_list(self):
            return self.getTypedRuleContext(AiLangParser.Basic_listContext,0)


        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


        def getRuleIndex(self):
            return AiLangParser.RULE_df_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDf_val" ):
                listener.enterDf_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDf_val" ):
                listener.exitDf_val(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDf_val" ):
                return visitor.visitDf_val(self)
            else:
                return visitor.visitChildren(self)




    def df_val(self):

        localctx = AiLangParser.Df_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_df_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 256
                self.id_()
                self.state = 257
                self.match(AiLangParser.T__11)


            self.state = 261
            self.basic_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AiLangParser.RULE_member

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntIDMemberContext(MemberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.MemberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(AiLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntIDMember" ):
                listener.enterIntIDMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntIDMember" ):
                listener.exitIntIDMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntIDMember" ):
                return visitor.visitIntIDMember(self)
            else:
                return visitor.visitChildren(self)


    class ListIDMemberContext(MemberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.MemberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListIDMember" ):
                listener.enterListIDMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListIDMember" ):
                listener.exitListIDMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListIDMember" ):
                return visitor.visitListIDMember(self)
            else:
                return visitor.visitChildren(self)


    class BasicIDMemberContext(MemberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.MemberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBasicIDMember" ):
                listener.enterBasicIDMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBasicIDMember" ):
                listener.exitBasicIDMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicIDMember" ):
                return visitor.visitBasicIDMember(self)
            else:
                return visitor.visitChildren(self)



    def member(self):

        localctx = AiLangParser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_member)
        try:
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = AiLangParser.BasicIDMemberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.id_()
                pass
            elif token in [25]:
                localctx = AiLangParser.IntIDMemberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(AiLangParser.INT)
                pass
            elif token in [1]:
                localctx = AiLangParser.ListIDMemberContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.match(AiLangParser.T__0)
                self.state = 266
                self.id_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AiLangParser.RULE_basic_list

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StrListContext(Basic_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.Basic_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def str_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.StrContext)
            else:
                return self.getTypedRuleContext(AiLangParser.StrContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrList" ):
                listener.enterStrList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrList" ):
                listener.exitStrList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrList" ):
                return visitor.visitStrList(self)
            else:
                return visitor.visitChildren(self)


    class NumListContext(Basic_listContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.Basic_listContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.NumContext)
            else:
                return self.getTypedRuleContext(AiLangParser.NumContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumList" ):
                listener.enterNumList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumList" ):
                listener.exitNumList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumList" ):
                return visitor.visitNumList(self)
            else:
                return visitor.visitChildren(self)



    def basic_list(self):

        localctx = AiLangParser.Basic_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_basic_list)
        self._la = 0 # Token type
        try:
            self.state = 291
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                localctx = AiLangParser.NumListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(AiLangParser.T__4)
                self.state = 270
                self.num()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 271
                    self.match(AiLangParser.T__5)
                    self.state = 272
                    self.num()
                    self.state = 277
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 278
                self.match(AiLangParser.T__6)
                pass

            elif la_ == 2:
                localctx = AiLangParser.StrListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 280
                self.match(AiLangParser.T__4)
                self.state = 281
                self.str_()
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 282
                    self.match(AiLangParser.T__5)
                    self.state = 283
                    self.str_()
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 289
                self.match(AiLangParser.T__6)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AiLangParser.RULE_basic_val

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumberContext(Basic_valContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.Basic_valContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def num(self):
            return self.getTypedRuleContext(AiLangParser.NumContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(Basic_valContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.Basic_valContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def str_(self):
            return self.getTypedRuleContext(AiLangParser.StrContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class Group_basic_valContext(Basic_valContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.Basic_valContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def basic_val(self):
            return self.getTypedRuleContext(AiLangParser.Basic_valContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup_basic_val" ):
                listener.enterGroup_basic_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup_basic_val" ):
                listener.exitGroup_basic_val(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroup_basic_val" ):
                return visitor.visitGroup_basic_val(self)
            else:
                return visitor.visitChildren(self)



    def basic_val(self):

        localctx = AiLangParser.Basic_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_basic_val)
        try:
            self.state = 299
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24, 25]:
                localctx = AiLangParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.num()
                pass
            elif token in [23]:
                localctx = AiLangParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 294
                self.str_()
                pass
            elif token in [5]:
                localctx = AiLangParser.Group_basic_valContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.match(AiLangParser.T__4)
                self.state = 296
                self.basic_val()
                self.state = 297
                self.match(AiLangParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AiLangParser.RULE_num

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FloatLiteralContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(AiLangParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatLiteral" ):
                listener.enterFloatLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatLiteral" ):
                listener.exitFloatLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLiteral" ):
                return visitor.visitFloatLiteral(self)
            else:
                return visitor.visitChildren(self)


    class IntigerLiteralContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(AiLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntigerLiteral" ):
                listener.enterIntigerLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntigerLiteral" ):
                listener.exitIntigerLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntigerLiteral" ):
                return visitor.visitIntigerLiteral(self)
            else:
                return visitor.visitChildren(self)



    def num(self):

        localctx = AiLangParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_num)
        try:
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = AiLangParser.IntigerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.match(AiLangParser.INT)
                pass
            elif token in [24]:
                localctx = AiLangParser.FloatLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.match(AiLangParser.FLOAT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR(self):
            return self.getToken(AiLangParser.STR, 0)

        def getRuleIndex(self):
            return AiLangParser.RULE_str

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr" ):
                listener.enterStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr" ):
                listener.exitStr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr" ):
                return visitor.visitStr(self)
            else:
                return visitor.visitChildren(self)




    def str_(self):

        localctx = AiLangParser.StrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_str)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(AiLangParser.STR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[16] = self.expr_sempred
        self._predicates[17] = self.assignable_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def assignable_sempred(self, localctx:AssignableContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




