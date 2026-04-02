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
        4,1,29,310,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,4,0,64,8,0,11,0,12,0,
        65,1,1,1,1,3,1,70,8,1,1,1,1,1,1,1,1,1,3,1,76,8,1,1,1,1,1,3,1,80,
        8,1,1,2,1,2,1,2,1,3,1,3,5,3,87,8,3,10,3,12,3,90,9,3,1,3,1,3,1,4,
        1,4,5,4,96,8,4,10,4,12,4,99,9,4,1,4,1,4,1,5,1,5,1,5,5,5,106,8,5,
        10,5,12,5,109,9,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,
        9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,133,8,10,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,142,8,11,10,11,12,11,145,
        9,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,13,3,13,161,8,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,179,8,15,1,15,1,15,
        1,15,5,15,184,8,15,10,15,12,15,187,9,15,1,16,1,16,1,16,1,16,1,17,
        1,17,3,17,195,8,17,1,18,1,18,1,18,1,18,5,18,201,8,18,10,18,12,18,
        204,9,18,3,18,206,8,18,1,18,1,18,1,19,1,19,1,19,1,19,5,19,214,8,
        19,10,19,12,19,217,9,19,1,19,1,19,1,20,1,20,1,20,3,20,224,8,20,1,
        21,1,21,1,21,1,21,5,21,230,8,21,10,21,12,21,233,9,21,1,21,1,21,1,
        22,1,22,1,22,3,22,240,8,22,1,22,1,22,1,23,1,23,3,23,246,8,23,1,24,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,257,8,24,1,25,1,25,
        1,25,1,25,1,25,3,25,264,8,25,1,26,1,26,1,26,1,26,3,26,270,8,26,1,
        27,1,27,1,27,1,27,5,27,276,8,27,10,27,12,27,279,9,27,1,27,1,27,1,
        27,1,27,1,27,1,27,5,27,287,8,27,10,27,12,27,290,9,27,1,27,1,27,3,
        27,294,8,27,1,28,1,28,1,28,1,28,1,28,1,28,3,28,302,8,28,1,29,1,29,
        3,29,306,8,29,1,30,1,30,1,30,0,1,30,31,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,0,
        0,320,0,63,1,0,0,0,2,79,1,0,0,0,4,81,1,0,0,0,6,84,1,0,0,0,8,93,1,
        0,0,0,10,102,1,0,0,0,12,110,1,0,0,0,14,114,1,0,0,0,16,116,1,0,0,
        0,18,120,1,0,0,0,20,132,1,0,0,0,22,134,1,0,0,0,24,149,1,0,0,0,26,
        154,1,0,0,0,28,162,1,0,0,0,30,178,1,0,0,0,32,188,1,0,0,0,34,194,
        1,0,0,0,36,196,1,0,0,0,38,209,1,0,0,0,40,223,1,0,0,0,42,225,1,0,
        0,0,44,239,1,0,0,0,46,245,1,0,0,0,48,256,1,0,0,0,50,258,1,0,0,0,
        52,265,1,0,0,0,54,293,1,0,0,0,56,301,1,0,0,0,58,305,1,0,0,0,60,307,
        1,0,0,0,62,64,3,20,10,0,63,62,1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,
        0,65,66,1,0,0,0,66,1,1,0,0,0,67,69,5,18,0,0,68,70,3,4,2,0,69,68,
        1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,80,3,6,3,0,72,73,3,4,2,0,
        73,75,5,18,0,0,74,76,3,4,2,0,75,74,1,0,0,0,75,76,1,0,0,0,76,77,1,
        0,0,0,77,78,3,6,3,0,78,80,1,0,0,0,79,67,1,0,0,0,79,72,1,0,0,0,80,
        3,1,0,0,0,81,82,5,1,0,0,82,83,3,14,7,0,83,5,1,0,0,0,84,88,5,2,0,
        0,85,87,3,20,10,0,86,85,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,
        1,0,0,0,89,91,1,0,0,0,90,88,1,0,0,0,91,92,5,3,0,0,92,7,1,0,0,0,93,
        97,5,2,0,0,94,96,3,10,5,0,95,94,1,0,0,0,96,99,1,0,0,0,97,95,1,0,
        0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,101,5,3,0,0,101,
        9,1,0,0,0,102,107,3,28,14,0,103,104,5,21,0,0,104,106,3,28,14,0,105,
        103,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,
        11,1,0,0,0,109,107,1,0,0,0,110,111,3,14,7,0,111,112,5,4,0,0,112,
        113,3,30,15,0,113,13,1,0,0,0,114,115,5,25,0,0,115,15,1,0,0,0,116,
        117,3,14,7,0,117,118,5,19,0,0,118,119,3,30,15,0,119,17,1,0,0,0,120,
        121,3,48,24,0,121,122,5,19,0,0,122,123,3,30,15,0,123,19,1,0,0,0,
        124,133,3,22,11,0,125,133,3,12,6,0,126,133,3,16,8,0,127,133,3,18,
        9,0,128,133,3,30,15,0,129,133,3,2,1,0,130,133,3,26,13,0,131,133,
        3,24,12,0,132,124,1,0,0,0,132,125,1,0,0,0,132,126,1,0,0,0,132,127,
        1,0,0,0,132,128,1,0,0,0,132,129,1,0,0,0,132,130,1,0,0,0,132,131,
        1,0,0,0,133,21,1,0,0,0,134,135,5,17,0,0,135,136,3,14,7,0,136,137,
        5,19,0,0,137,138,5,5,0,0,138,143,3,14,7,0,139,140,5,6,0,0,140,142,
        3,14,7,0,141,139,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,
        1,0,0,0,144,146,1,0,0,0,145,143,1,0,0,0,146,147,5,7,0,0,147,148,
        3,6,3,0,148,23,1,0,0,0,149,150,5,16,0,0,150,151,5,22,0,0,151,152,
        5,18,0,0,152,153,3,14,7,0,153,25,1,0,0,0,154,155,5,13,0,0,155,156,
        3,6,3,0,156,157,5,14,0,0,157,160,3,8,4,0,158,159,5,15,0,0,159,161,
        3,6,3,0,160,158,1,0,0,0,160,161,1,0,0,0,161,27,1,0,0,0,162,163,3,
        30,15,0,163,164,5,21,0,0,164,165,3,30,15,0,165,29,1,0,0,0,166,167,
        6,15,-1,0,167,179,3,56,28,0,168,179,3,42,21,0,169,179,3,50,25,0,
        170,179,3,48,24,0,171,179,3,14,7,0,172,179,3,52,26,0,173,179,3,40,
        20,0,174,175,5,5,0,0,175,176,3,30,15,0,176,177,5,7,0,0,177,179,1,
        0,0,0,178,166,1,0,0,0,178,168,1,0,0,0,178,169,1,0,0,0,178,170,1,
        0,0,0,178,171,1,0,0,0,178,172,1,0,0,0,178,173,1,0,0,0,178,174,1,
        0,0,0,179,185,1,0,0,0,180,181,10,1,0,0,181,182,5,20,0,0,182,184,
        3,30,15,2,183,180,1,0,0,0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,
        1,0,0,0,186,31,1,0,0,0,187,185,1,0,0,0,188,189,3,14,7,0,189,190,
        5,8,0,0,190,191,3,30,15,0,191,33,1,0,0,0,192,195,3,32,16,0,193,195,
        3,30,15,0,194,192,1,0,0,0,194,193,1,0,0,0,195,35,1,0,0,0,196,205,
        5,5,0,0,197,202,3,34,17,0,198,199,5,6,0,0,199,201,3,34,17,0,200,
        198,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,
        206,1,0,0,0,204,202,1,0,0,0,205,197,1,0,0,0,205,206,1,0,0,0,206,
        207,1,0,0,0,207,208,5,7,0,0,208,37,1,0,0,0,209,210,5,5,0,0,210,215,
        3,30,15,0,211,212,5,6,0,0,212,214,3,30,15,0,213,211,1,0,0,0,214,
        217,1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,218,1,0,0,0,217,
        215,1,0,0,0,218,219,5,7,0,0,219,39,1,0,0,0,220,224,3,54,27,0,221,
        224,3,38,19,0,222,224,3,14,7,0,223,220,1,0,0,0,223,221,1,0,0,0,223,
        222,1,0,0,0,224,41,1,0,0,0,225,226,5,9,0,0,226,231,3,44,22,0,227,
        228,5,6,0,0,228,230,3,44,22,0,229,227,1,0,0,0,230,233,1,0,0,0,231,
        229,1,0,0,0,231,232,1,0,0,0,232,234,1,0,0,0,233,231,1,0,0,0,234,
        235,5,10,0,0,235,43,1,0,0,0,236,237,3,14,7,0,237,238,5,11,0,0,238,
        240,1,0,0,0,239,236,1,0,0,0,239,240,1,0,0,0,240,241,1,0,0,0,241,
        242,3,54,27,0,242,45,1,0,0,0,243,246,3,14,7,0,244,246,5,24,0,0,245,
        243,1,0,0,0,245,244,1,0,0,0,246,47,1,0,0,0,247,248,3,14,7,0,248,
        249,5,12,0,0,249,250,3,46,23,0,250,257,1,0,0,0,251,252,3,14,7,0,
        252,253,5,12,0,0,253,254,5,1,0,0,254,255,3,14,7,0,255,257,1,0,0,
        0,256,247,1,0,0,0,256,251,1,0,0,0,257,49,1,0,0,0,258,259,3,48,24,
        0,259,260,5,12,0,0,260,263,3,14,7,0,261,262,5,19,0,0,262,264,3,36,
        18,0,263,261,1,0,0,0,263,264,1,0,0,0,264,51,1,0,0,0,265,266,5,12,
        0,0,266,269,3,14,7,0,267,268,5,19,0,0,268,270,3,36,18,0,269,267,
        1,0,0,0,269,270,1,0,0,0,270,53,1,0,0,0,271,272,5,5,0,0,272,277,3,
        58,29,0,273,274,5,6,0,0,274,276,3,58,29,0,275,273,1,0,0,0,276,279,
        1,0,0,0,277,275,1,0,0,0,277,278,1,0,0,0,278,280,1,0,0,0,279,277,
        1,0,0,0,280,281,5,7,0,0,281,294,1,0,0,0,282,283,5,5,0,0,283,288,
        3,60,30,0,284,285,5,6,0,0,285,287,3,60,30,0,286,284,1,0,0,0,287,
        290,1,0,0,0,288,286,1,0,0,0,288,289,1,0,0,0,289,291,1,0,0,0,290,
        288,1,0,0,0,291,292,5,7,0,0,292,294,1,0,0,0,293,271,1,0,0,0,293,
        282,1,0,0,0,294,55,1,0,0,0,295,302,3,58,29,0,296,302,3,60,30,0,297,
        298,5,5,0,0,298,299,3,56,28,0,299,300,5,7,0,0,300,302,1,0,0,0,301,
        295,1,0,0,0,301,296,1,0,0,0,301,297,1,0,0,0,302,57,1,0,0,0,303,306,
        5,24,0,0,304,306,5,23,0,0,305,303,1,0,0,0,305,304,1,0,0,0,306,59,
        1,0,0,0,307,308,5,22,0,0,308,61,1,0,0,0,28,65,69,75,79,88,97,107,
        132,143,160,178,185,194,202,205,215,223,231,239,245,256,263,269,
        277,288,293,301,305
    ]

class AiLangParser ( Parser ):

    grammarFileName = "AiLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@'", "'{'", "'}'", "':='", "'('", "','", 
                     "')'", "'='", "'['", "']'", "':'", "'.'", "'do'", "'if'", 
                     "'else'", "'from'", "'function'", "'->'", "'<-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "DO", "IF", "ELSE", "FROM", "FUNCTION", 
                      "ARR", "REF", "MATH_OP", "BOOL_OP", "STR", "FLOAT", 
                      "INT", "ID", "LINE_COMMENT", "BLOCK_COMMENT", "NL", 
                      "WS" ]

    RULE_prog = 0
    RULE_block = 1
    RULE_label = 2
    RULE_context = 3
    RULE_bool_context = 4
    RULE_bool_group = 5
    RULE_assignment = 6
    RULE_id = 7
    RULE_ref_op = 8
    RULE_column_ref_op = 9
    RULE_stat = 10
    RULE_func_def = 11
    RULE_fromToData = 12
    RULE_doIfElse = 13
    RULE_bool_stat = 14
    RULE_expr = 15
    RULE_named_arg = 16
    RULE_arg = 17
    RULE_arg_list = 18
    RULE_generic_list = 19
    RULE_list = 20
    RULE_df = 21
    RULE_df_val = 22
    RULE_column_id = 23
    RULE_column = 24
    RULE_column_method = 25
    RULE_func = 26
    RULE_basic_list = 27
    RULE_basic_val = 28
    RULE_num = 29
    RULE_str = 30

    ruleNames =  [ "prog", "block", "label", "context", "bool_context", 
                   "bool_group", "assignment", "id", "ref_op", "column_ref_op", 
                   "stat", "func_def", "fromToData", "doIfElse", "bool_stat", 
                   "expr", "named_arg", "arg", "arg_list", "generic_list", 
                   "list", "df", "df_val", "column_id", "column", "column_method", 
                   "func", "basic_list", "basic_val", "num", "str" ]

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
    DO=13
    IF=14
    ELSE=15
    FROM=16
    FUNCTION=17
    ARR=18
    REF=19
    MATH_OP=20
    BOOL_OP=21
    STR=22
    FLOAT=23
    INT=24
    ID=25
    LINE_COMMENT=26
    BLOCK_COMMENT=27
    NL=28
    WS=29

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
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.stat()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 63386146) != 0)):
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
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = AiLangParser.Block2BlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(AiLangParser.ARR)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 68
                    self.label()


                self.state = 71
                self.context()
                pass
            elif token in [1]:
                localctx = AiLangParser.Label2BlockContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.label()
                self.state = 73
                self.match(AiLangParser.ARR)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 74
                    self.label()


                self.state = 77
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
            self.state = 81
            self.match(AiLangParser.T__0)
            self.state = 82
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
            self.state = 84
            self.match(AiLangParser.T__1)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 63386146) != 0):
                self.state = 85
                self.stat()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
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
            self.state = 93
            self.match(AiLangParser.T__1)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 62919200) != 0):
                self.state = 94
                self.bool_group()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
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
            self.state = 102
            self.bool_stat()
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 103
                self.match(AiLangParser.BOOL_OP)
                self.state = 104
                self.bool_stat()
                self.state = 109
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


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
        self.enterRule(localctx, 12, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.id_()
            self.state = 111
            self.match(AiLangParser.T__3)
            self.state = 112
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
        self.enterRule(localctx, 14, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
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

        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


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
        self.enterRule(localctx, 16, self.RULE_ref_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.id_()
            self.state = 117
            self.match(AiLangParser.REF)
            self.state = 118
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_ref_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(AiLangParser.ColumnContext,0)


        def REF(self):
            return self.getToken(AiLangParser.REF, 0)

        def expr(self):
            return self.getTypedRuleContext(AiLangParser.ExprContext,0)


        def getRuleIndex(self):
            return AiLangParser.RULE_column_ref_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_ref_op" ):
                listener.enterColumn_ref_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_ref_op" ):
                listener.exitColumn_ref_op(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_ref_op" ):
                return visitor.visitColumn_ref_op(self)
            else:
                return visitor.visitChildren(self)




    def column_ref_op(self):

        localctx = AiLangParser.Column_ref_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_column_ref_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.column()
            self.state = 121
            self.match(AiLangParser.REF)
            self.state = 122
            self.expr(0)
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


    class Column_referenceContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def column_ref_op(self):
            return self.getTypedRuleContext(AiLangParser.Column_ref_opContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_reference" ):
                listener.enterColumn_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_reference" ):
                listener.exitColumn_reference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_reference" ):
                return visitor.visitColumn_reference(self)
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
        self.enterRule(localctx, 20, self.RULE_stat)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = AiLangParser.FunctionDefContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.func_def()
                pass

            elif la_ == 2:
                localctx = AiLangParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.assignment()
                pass

            elif la_ == 3:
                localctx = AiLangParser.ReferenceContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.ref_op()
                pass

            elif la_ == 4:
                localctx = AiLangParser.Column_referenceContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 127
                self.column_ref_op()
                pass

            elif la_ == 5:
                localctx = AiLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 128
                self.expr(0)
                pass

            elif la_ == 6:
                localctx = AiLangParser.Block_statContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 129
                self.block()
                pass

            elif la_ == 7:
                localctx = AiLangParser.Do_if_elseContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 130
                self.doIfElse()
                pass

            elif la_ == 8:
                localctx = AiLangParser.Load_opContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 131
                self.fromToData()
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
        self.enterRule(localctx, 22, self.RULE_func_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(AiLangParser.FUNCTION)
            self.state = 135
            self.id_()
            self.state = 136
            self.match(AiLangParser.REF)
            self.state = 137
            self.match(AiLangParser.T__4)
            self.state = 138
            self.id_()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 139
                self.match(AiLangParser.T__5)
                self.state = 140
                self.id_()
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 146
            self.match(AiLangParser.T__6)
            self.state = 147
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

        def STR(self):
            return self.getToken(AiLangParser.STR, 0)

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
        self.enterRule(localctx, 24, self.RULE_fromToData)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(AiLangParser.FROM)
            self.state = 150
            self.match(AiLangParser.STR)
            self.state = 151
            self.match(AiLangParser.ARR)
            self.state = 152
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
        self.enterRule(localctx, 26, self.RULE_doIfElse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(AiLangParser.DO)
            self.state = 155
            self.context()
            self.state = 156
            self.match(AiLangParser.IF)
            self.state = 157
            self.bool_context()
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 158
                self.match(AiLangParser.ELSE)
                self.state = 159
                self.context()


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
        self.enterRule(localctx, 28, self.RULE_bool_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.expr(0)
            self.state = 163
            self.match(AiLangParser.BOOL_OP)
            self.state = 164
            self.expr(0)
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


    class ColumnMethodContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def column_method(self):
            return self.getTypedRuleContext(AiLangParser.Column_methodContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnMethod" ):
                listener.enterColumnMethod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnMethod" ):
                listener.exitColumnMethod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnMethod" ):
                return visitor.visitColumnMethod(self)
            else:
                return visitor.visitChildren(self)


    class IdValContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdVal" ):
                listener.enterIdVal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdVal" ):
                listener.exitIdVal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdVal" ):
                return visitor.visitIdVal(self)
            else:
                return visitor.visitChildren(self)


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


    class ColumnIDContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def column(self):
            return self.getTypedRuleContext(AiLangParser.ColumnContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnID" ):
                listener.enterColumnID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnID" ):
                listener.exitColumnID(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnID" ):
                return visitor.visitColumnID(self)
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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AiLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = AiLangParser.BasicValExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 167
                self.basic_val()
                pass

            elif la_ == 2:
                localctx = AiLangParser.DataframeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 168
                self.df()
                pass

            elif la_ == 3:
                localctx = AiLangParser.ColumnMethodContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 169
                self.column_method()
                pass

            elif la_ == 4:
                localctx = AiLangParser.ColumnIDContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 170
                self.column()
                pass

            elif la_ == 5:
                localctx = AiLangParser.IdValContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 171
                self.id_()
                pass

            elif la_ == 6:
                localctx = AiLangParser.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 172
                self.func()
                pass

            elif la_ == 7:
                localctx = AiLangParser.ListValExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 173
                self.list_()
                pass

            elif la_ == 8:
                localctx = AiLangParser.GroupContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 174
                self.match(AiLangParser.T__4)
                self.state = 175
                self.expr(0)
                self.state = 176
                self.match(AiLangParser.T__6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AiLangParser.MathOpContext(self, AiLangParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 180
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 181
                    self.match(AiLangParser.MATH_OP)
                    self.state = 182
                    self.expr(2) 
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_named_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.id_()
            self.state = 189
            self.match(AiLangParser.T__7)
            self.state = 190
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

        def named_arg(self):
            return self.getTypedRuleContext(AiLangParser.Named_argContext,0)


        def expr(self):
            return self.getTypedRuleContext(AiLangParser.ExprContext,0)


        def getRuleIndex(self):
            return AiLangParser.RULE_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg" ):
                listener.enterArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg" ):
                listener.exitArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = AiLangParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arg)
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.named_arg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
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
        self.enterRule(localctx, 36, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(AiLangParser.T__4)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 62919200) != 0):
                self.state = 197
                self.arg()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 198
                    self.match(AiLangParser.T__5)
                    self.state = 199
                    self.arg()
                    self.state = 204
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 207
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
        self.enterRule(localctx, 38, self.RULE_generic_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(AiLangParser.T__4)
            self.state = 210
            self.expr(0)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 211
                self.match(AiLangParser.T__5)
                self.state = 212
                self.expr(0)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
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


        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


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
        self.enterRule(localctx, 40, self.RULE_list)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.basic_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.generic_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.id_()
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

        def df_val(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.Df_valContext)
            else:
                return self.getTypedRuleContext(AiLangParser.Df_valContext,i)


        def getRuleIndex(self):
            return AiLangParser.RULE_df

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDf" ):
                listener.enterDf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDf" ):
                listener.exitDf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDf" ):
                return visitor.visitDf(self)
            else:
                return visitor.visitChildren(self)




    def df(self):

        localctx = AiLangParser.DfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_df)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(AiLangParser.T__8)
            self.state = 226
            self.df_val()
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 227
                self.match(AiLangParser.T__5)
                self.state = 228
                self.df_val()
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 234
            self.match(AiLangParser.T__9)
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
        self.enterRule(localctx, 44, self.RULE_df_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 236
                self.id_()
                self.state = 237
                self.match(AiLangParser.T__10)


            self.state = 241
            self.basic_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


        def INT(self):
            return self.getToken(AiLangParser.INT, 0)

        def getRuleIndex(self):
            return AiLangParser.RULE_column_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_id" ):
                listener.enterColumn_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_id" ):
                listener.exitColumn_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_id" ):
                return visitor.visitColumn_id(self)
            else:
                return visitor.visitChildren(self)




    def column_id(self):

        localctx = AiLangParser.Column_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_column_id)
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.id_()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(AiLangParser.INT)
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


    class ColumnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AiLangParser.RULE_column

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleColumnContext(ColumnContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ColumnContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)

        def column_id(self):
            return self.getTypedRuleContext(AiLangParser.Column_idContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleColumn" ):
                listener.enterSimpleColumn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleColumn" ):
                listener.exitSimpleColumn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleColumn" ):
                return visitor.visitSimpleColumn(self)
            else:
                return visitor.visitChildren(self)


    class ColumnSetContext(ColumnContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AiLangParser.ColumnContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AiLangParser.IdContext)
            else:
                return self.getTypedRuleContext(AiLangParser.IdContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnSet" ):
                listener.enterColumnSet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnSet" ):
                listener.exitColumnSet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnSet" ):
                return visitor.visitColumnSet(self)
            else:
                return visitor.visitChildren(self)



    def column(self):

        localctx = AiLangParser.ColumnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_column)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                localctx = AiLangParser.SimpleColumnContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.id_()
                self.state = 248
                self.match(AiLangParser.T__11)
                self.state = 249
                self.column_id()
                pass

            elif la_ == 2:
                localctx = AiLangParser.ColumnSetContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.id_()
                self.state = 252
                self.match(AiLangParser.T__11)
                self.state = 253
                self.match(AiLangParser.T__0)
                self.state = 254
                self.id_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column(self):
            return self.getTypedRuleContext(AiLangParser.ColumnContext,0)


        def id_(self):
            return self.getTypedRuleContext(AiLangParser.IdContext,0)


        def REF(self):
            return self.getToken(AiLangParser.REF, 0)

        def arg_list(self):
            return self.getTypedRuleContext(AiLangParser.Arg_listContext,0)


        def getRuleIndex(self):
            return AiLangParser.RULE_column_method

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_method" ):
                listener.enterColumn_method(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_method" ):
                listener.exitColumn_method(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumn_method" ):
                return visitor.visitColumn_method(self)
            else:
                return visitor.visitChildren(self)




    def column_method(self):

        localctx = AiLangParser.Column_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_column_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.column()
            self.state = 259
            self.match(AiLangParser.T__11)
            self.state = 260
            self.id_()
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 261
                self.match(AiLangParser.REF)
                self.state = 262
                self.arg_list()


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
        self.enterRule(localctx, 52, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(AiLangParser.T__11)
            self.state = 266
            self.id_()
            self.state = 269
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 267
                self.match(AiLangParser.REF)
                self.state = 268
                self.arg_list()


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
        self.enterRule(localctx, 54, self.RULE_basic_list)
        self._la = 0 # Token type
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = AiLangParser.NumListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.match(AiLangParser.T__4)
                self.state = 272
                self.num()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 273
                    self.match(AiLangParser.T__5)
                    self.state = 274
                    self.num()
                    self.state = 279
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 280
                self.match(AiLangParser.T__6)
                pass

            elif la_ == 2:
                localctx = AiLangParser.StrListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(AiLangParser.T__4)
                self.state = 283
                self.str_()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 284
                    self.match(AiLangParser.T__5)
                    self.state = 285
                    self.str_()
                    self.state = 290
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 291
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
        self.enterRule(localctx, 56, self.RULE_basic_val)
        try:
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24]:
                localctx = AiLangParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.num()
                pass
            elif token in [22]:
                localctx = AiLangParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.str_()
                pass
            elif token in [5]:
                localctx = AiLangParser.Group_basic_valContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 297
                self.match(AiLangParser.T__4)
                self.state = 298
                self.basic_val()
                self.state = 299
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
        self.enterRule(localctx, 58, self.RULE_num)
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                localctx = AiLangParser.IntigerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(AiLangParser.INT)
                pass
            elif token in [23]:
                localctx = AiLangParser.FloatLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 304
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
        self.enterRule(localctx, 60, self.RULE_str)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
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
        self._predicates[15] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




