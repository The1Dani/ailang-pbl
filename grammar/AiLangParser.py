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
        4,1,29,297,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,1,0,4,0,60,8,0,11,0,12,0,61,1,1,1,1,3,1,66,8,
        1,1,1,1,1,1,1,1,1,3,1,72,8,1,1,1,1,1,3,1,76,8,1,1,2,1,2,1,2,1,3,
        1,3,5,3,83,8,3,10,3,12,3,86,9,3,1,3,1,3,1,4,1,4,5,4,92,8,4,10,4,
        12,4,95,9,4,1,4,1,4,1,5,1,5,1,5,5,5,102,8,5,10,5,12,5,105,9,5,1,
        6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,3,10,128,8,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,5,11,137,8,11,10,11,12,11,140,9,11,1,11,1,11,1,11,1,12,
        1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,156,8,13,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,168,8,14,
        1,14,1,14,1,14,1,14,1,14,1,14,5,14,176,8,14,10,14,12,14,179,9,14,
        1,15,1,15,1,15,1,15,1,15,1,15,5,15,187,8,15,10,15,12,15,190,9,15,
        1,16,1,16,1,16,1,16,1,17,1,17,3,17,198,8,17,1,18,1,18,1,18,1,18,
        5,18,204,8,18,10,18,12,18,207,9,18,3,18,209,8,18,1,18,1,18,1,19,
        1,19,1,19,1,19,5,19,217,8,19,10,19,12,19,220,9,19,1,19,1,19,1,20,
        1,20,1,20,3,20,227,8,20,1,21,1,21,1,21,1,21,5,21,233,8,21,10,21,
        12,21,236,9,21,1,21,1,21,1,22,1,22,1,22,3,22,243,8,22,1,22,1,22,
        1,23,1,23,1,23,1,23,3,23,251,8,23,1,24,1,24,1,24,1,24,3,24,257,8,
        24,1,25,1,25,1,25,1,25,5,25,263,8,25,10,25,12,25,266,9,25,1,25,1,
        25,1,25,1,25,1,25,1,25,5,25,274,8,25,10,25,12,25,277,9,25,1,25,1,
        25,3,25,281,8,25,1,26,1,26,1,26,1,26,1,26,1,26,3,26,289,8,26,1,27,
        1,27,3,27,293,8,27,1,28,1,28,1,28,0,2,28,30,29,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,0,
        0,307,0,59,1,0,0,0,2,75,1,0,0,0,4,77,1,0,0,0,6,80,1,0,0,0,8,89,1,
        0,0,0,10,98,1,0,0,0,12,106,1,0,0,0,14,110,1,0,0,0,16,114,1,0,0,0,
        18,116,1,0,0,0,20,127,1,0,0,0,22,129,1,0,0,0,24,144,1,0,0,0,26,149,
        1,0,0,0,28,167,1,0,0,0,30,180,1,0,0,0,32,191,1,0,0,0,34,197,1,0,
        0,0,36,199,1,0,0,0,38,212,1,0,0,0,40,226,1,0,0,0,42,228,1,0,0,0,
        44,242,1,0,0,0,46,250,1,0,0,0,48,252,1,0,0,0,50,280,1,0,0,0,52,288,
        1,0,0,0,54,292,1,0,0,0,56,294,1,0,0,0,58,60,3,20,10,0,59,58,1,0,
        0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,1,1,0,0,0,63,65,
        5,18,0,0,64,66,3,4,2,0,65,64,1,0,0,0,65,66,1,0,0,0,66,67,1,0,0,0,
        67,76,3,6,3,0,68,69,3,4,2,0,69,71,5,18,0,0,70,72,3,4,2,0,71,70,1,
        0,0,0,71,72,1,0,0,0,72,73,1,0,0,0,73,74,3,6,3,0,74,76,1,0,0,0,75,
        63,1,0,0,0,75,68,1,0,0,0,76,3,1,0,0,0,77,78,5,1,0,0,78,79,3,16,8,
        0,79,5,1,0,0,0,80,84,5,2,0,0,81,83,3,20,10,0,82,81,1,0,0,0,83,86,
        1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,84,1,0,0,0,
        87,88,5,3,0,0,88,7,1,0,0,0,89,93,5,2,0,0,90,92,3,10,5,0,91,90,1,
        0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,
        93,1,0,0,0,96,97,5,3,0,0,97,9,1,0,0,0,98,103,3,12,6,0,99,100,5,21,
        0,0,100,102,3,12,6,0,101,99,1,0,0,0,102,105,1,0,0,0,103,101,1,0,
        0,0,103,104,1,0,0,0,104,11,1,0,0,0,105,103,1,0,0,0,106,107,3,28,
        14,0,107,108,5,21,0,0,108,109,3,28,14,0,109,13,1,0,0,0,110,111,3,
        30,15,0,111,112,5,4,0,0,112,113,3,28,14,0,113,15,1,0,0,0,114,115,
        5,25,0,0,115,17,1,0,0,0,116,117,3,30,15,0,117,118,5,19,0,0,118,119,
        3,28,14,0,119,19,1,0,0,0,120,128,3,22,11,0,121,128,3,14,7,0,122,
        128,3,18,9,0,123,128,3,28,14,0,124,128,3,2,1,0,125,128,3,26,13,0,
        126,128,3,24,12,0,127,120,1,0,0,0,127,121,1,0,0,0,127,122,1,0,0,
        0,127,123,1,0,0,0,127,124,1,0,0,0,127,125,1,0,0,0,127,126,1,0,0,
        0,128,21,1,0,0,0,129,130,5,17,0,0,130,131,3,16,8,0,131,132,5,19,
        0,0,132,133,5,5,0,0,133,138,3,16,8,0,134,135,5,6,0,0,135,137,3,16,
        8,0,136,134,1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,1,0,
        0,0,139,141,1,0,0,0,140,138,1,0,0,0,141,142,5,7,0,0,142,143,3,6,
        3,0,143,23,1,0,0,0,144,145,5,16,0,0,145,146,3,56,28,0,146,147,5,
        18,0,0,147,148,3,16,8,0,148,25,1,0,0,0,149,150,5,13,0,0,150,151,
        3,6,3,0,151,152,5,14,0,0,152,155,3,8,4,0,153,154,5,15,0,0,154,156,
        3,6,3,0,155,153,1,0,0,0,155,156,1,0,0,0,156,27,1,0,0,0,157,158,6,
        14,-1,0,158,168,3,52,26,0,159,168,3,30,15,0,160,168,3,48,24,0,161,
        168,3,40,20,0,162,168,3,42,21,0,163,164,5,5,0,0,164,165,3,28,14,
        0,165,166,5,7,0,0,166,168,1,0,0,0,167,157,1,0,0,0,167,159,1,0,0,
        0,167,160,1,0,0,0,167,161,1,0,0,0,167,162,1,0,0,0,167,163,1,0,0,
        0,168,177,1,0,0,0,169,170,10,1,0,0,170,171,5,20,0,0,171,176,3,28,
        14,2,172,173,10,2,0,0,173,174,5,19,0,0,174,176,3,36,18,0,175,169,
        1,0,0,0,175,172,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,178,
        1,0,0,0,178,29,1,0,0,0,179,177,1,0,0,0,180,181,6,15,-1,0,181,182,
        3,16,8,0,182,188,1,0,0,0,183,184,10,1,0,0,184,185,5,8,0,0,185,187,
        3,46,23,0,186,183,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,
        1,0,0,0,189,31,1,0,0,0,190,188,1,0,0,0,191,192,3,16,8,0,192,193,
        5,9,0,0,193,194,3,28,14,0,194,33,1,0,0,0,195,198,3,32,16,0,196,198,
        3,28,14,0,197,195,1,0,0,0,197,196,1,0,0,0,198,35,1,0,0,0,199,208,
        5,5,0,0,200,205,3,34,17,0,201,202,5,6,0,0,202,204,3,34,17,0,203,
        201,1,0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,
        209,1,0,0,0,207,205,1,0,0,0,208,200,1,0,0,0,208,209,1,0,0,0,209,
        210,1,0,0,0,210,211,5,7,0,0,211,37,1,0,0,0,212,213,5,5,0,0,213,218,
        3,28,14,0,214,215,5,6,0,0,215,217,3,28,14,0,216,214,1,0,0,0,217,
        220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,221,1,0,0,0,220,
        218,1,0,0,0,221,222,5,7,0,0,222,39,1,0,0,0,223,227,3,50,25,0,224,
        227,3,38,19,0,225,227,3,16,8,0,226,223,1,0,0,0,226,224,1,0,0,0,226,
        225,1,0,0,0,227,41,1,0,0,0,228,229,5,10,0,0,229,234,3,44,22,0,230,
        231,5,6,0,0,231,233,3,44,22,0,232,230,1,0,0,0,233,236,1,0,0,0,234,
        232,1,0,0,0,234,235,1,0,0,0,235,237,1,0,0,0,236,234,1,0,0,0,237,
        238,5,11,0,0,238,43,1,0,0,0,239,240,3,16,8,0,240,241,5,12,0,0,241,
        243,1,0,0,0,242,239,1,0,0,0,242,243,1,0,0,0,243,244,1,0,0,0,244,
        245,3,50,25,0,245,45,1,0,0,0,246,251,3,16,8,0,247,251,5,24,0,0,248,
        249,5,1,0,0,249,251,3,16,8,0,250,246,1,0,0,0,250,247,1,0,0,0,250,
        248,1,0,0,0,251,47,1,0,0,0,252,253,5,8,0,0,253,256,3,16,8,0,254,
        255,5,19,0,0,255,257,3,36,18,0,256,254,1,0,0,0,256,257,1,0,0,0,257,
        49,1,0,0,0,258,259,5,5,0,0,259,264,3,54,27,0,260,261,5,6,0,0,261,
        263,3,54,27,0,262,260,1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,264,
        265,1,0,0,0,265,267,1,0,0,0,266,264,1,0,0,0,267,268,5,7,0,0,268,
        281,1,0,0,0,269,270,5,5,0,0,270,275,3,56,28,0,271,272,5,6,0,0,272,
        274,3,56,28,0,273,271,1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,
        276,1,0,0,0,276,278,1,0,0,0,277,275,1,0,0,0,278,279,5,7,0,0,279,
        281,1,0,0,0,280,258,1,0,0,0,280,269,1,0,0,0,281,51,1,0,0,0,282,289,
        3,54,27,0,283,289,3,56,28,0,284,285,5,5,0,0,285,286,3,52,26,0,286,
        287,5,7,0,0,287,289,1,0,0,0,288,282,1,0,0,0,288,283,1,0,0,0,288,
        284,1,0,0,0,289,53,1,0,0,0,290,293,5,24,0,0,291,293,5,23,0,0,292,
        290,1,0,0,0,292,291,1,0,0,0,293,55,1,0,0,0,294,295,5,22,0,0,295,
        57,1,0,0,0,28,61,65,71,75,84,93,103,127,138,155,167,175,177,188,
        197,205,208,218,226,234,242,250,256,264,275,280,288,292
    ]

class AiLangParser ( Parser ):

    grammarFileName = "AiLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@'", "'{'", "'}'", "':='", "'('", "','", 
                     "')'", "'.'", "'='", "'['", "']'", "':'", "'do'", "'if'", 
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
    RULE_bool_stat = 6
    RULE_assignment = 7
    RULE_id = 8
    RULE_ref_op = 9
    RULE_stat = 10
    RULE_func_def = 11
    RULE_fromToData = 12
    RULE_doIfElse = 13
    RULE_expr = 14
    RULE_assignable = 15
    RULE_named_arg = 16
    RULE_arg = 17
    RULE_arg_list = 18
    RULE_generic_list = 19
    RULE_list = 20
    RULE_df = 21
    RULE_df_val = 22
    RULE_member = 23
    RULE_func = 24
    RULE_basic_list = 25
    RULE_basic_val = 26
    RULE_num = 27
    RULE_str = 28

    ruleNames =  [ "prog", "block", "label", "context", "bool_context", 
                   "bool_group", "bool_stat", "assignment", "id", "ref_op", 
                   "stat", "func_def", "fromToData", "doIfElse", "expr", 
                   "assignable", "named_arg", "arg", "arg_list", "generic_list", 
                   "list", "df", "df_val", "member", "func", "basic_list", 
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
            self.state = 59 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 58
                self.stat()
                self.state = 61 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 63382818) != 0)):
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
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                localctx = AiLangParser.Block2BlockContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(AiLangParser.ARR)
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 64
                    self.label()


                self.state = 67
                self.context()
                pass
            elif token in [1]:
                localctx = AiLangParser.Label2BlockContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.label()
                self.state = 69
                self.match(AiLangParser.ARR)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 70
                    self.label()


                self.state = 73
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
            self.state = 77
            self.match(AiLangParser.T__0)
            self.state = 78
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
            self.state = 80
            self.match(AiLangParser.T__1)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 63382818) != 0):
                self.state = 81
                self.stat()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
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
            self.state = 89
            self.match(AiLangParser.T__1)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 62915872) != 0):
                self.state = 90
                self.bool_group()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
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
            self.state = 98
            self.bool_stat()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 99
                self.match(AiLangParser.BOOL_OP)
                self.state = 100
                self.bool_stat()
                self.state = 105
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
            self.state = 106
            self.expr(0)
            self.state = 107
            self.match(AiLangParser.BOOL_OP)
            self.state = 108
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
            self.state = 110
            self.assignable(0)
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
        self.enterRule(localctx, 16, self.RULE_id)
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
            self.state = 116
            self.assignable(0)
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
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = AiLangParser.FunctionDefContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.func_def()
                pass

            elif la_ == 2:
                localctx = AiLangParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.assignment()
                pass

            elif la_ == 3:
                localctx = AiLangParser.ReferenceContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.ref_op()
                pass

            elif la_ == 4:
                localctx = AiLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.expr(0)
                pass

            elif la_ == 5:
                localctx = AiLangParser.Block_statContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.block()
                pass

            elif la_ == 6:
                localctx = AiLangParser.Do_if_elseContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 125
                self.doIfElse()
                pass

            elif la_ == 7:
                localctx = AiLangParser.Load_opContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 126
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
            self.state = 129
            self.match(AiLangParser.FUNCTION)
            self.state = 130
            self.id_()
            self.state = 131
            self.match(AiLangParser.REF)
            self.state = 132
            self.match(AiLangParser.T__4)
            self.state = 133
            self.id_()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 134
                self.match(AiLangParser.T__5)
                self.state = 135
                self.id_()
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            self.match(AiLangParser.T__6)
            self.state = 142
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
        self.enterRule(localctx, 24, self.RULE_fromToData)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(AiLangParser.FROM)
            self.state = 145
            self.str_()
            self.state = 146
            self.match(AiLangParser.ARR)
            self.state = 147
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
            self.state = 149
            self.match(AiLangParser.DO)
            self.state = 150
            self.context()
            self.state = 151
            self.match(AiLangParser.IF)
            self.state = 152
            self.bool_context()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 153
                self.match(AiLangParser.ELSE)
                self.state = 154
                self.context()


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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = AiLangParser.BasicValExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 158
                self.basic_val()
                pass

            elif la_ == 2:
                localctx = AiLangParser.PathExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 159
                self.assignable(0)
                pass

            elif la_ == 3:
                localctx = AiLangParser.FunctionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 160
                self.func()
                pass

            elif la_ == 4:
                localctx = AiLangParser.ListValExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 161
                self.list_()
                pass

            elif la_ == 5:
                localctx = AiLangParser.DataframeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 162
                self.df()
                pass

            elif la_ == 6:
                localctx = AiLangParser.GroupContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 163
                self.match(AiLangParser.T__4)
                self.state = 164
                self.expr(0)
                self.state = 165
                self.match(AiLangParser.T__6)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 177
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 175
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = AiLangParser.MathOpContext(self, AiLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 169
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 170
                        self.match(AiLangParser.MATH_OP)
                        self.state = 171
                        self.expr(2)
                        pass

                    elif la_ == 2:
                        localctx = AiLangParser.MethodCallContext(self, AiLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 172
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 173
                        self.match(AiLangParser.REF)
                        self.state = 174
                        self.arg_list()
                        pass

             
                self.state = 179
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_assignable, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AiLangParser.SimpleTargetContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 181
            self.id_()
            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AiLangParser.MemberTargetContext(self, AiLangParser.AssignableContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_assignable)
                    self.state = 183
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 184
                    self.match(AiLangParser.T__7)
                    self.state = 185
                    self.member() 
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
            self.state = 191
            self.id_()
            self.state = 192
            self.match(AiLangParser.T__8)
            self.state = 193
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
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.named_arg()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
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
            self.state = 199
            self.match(AiLangParser.T__4)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 62915872) != 0):
                self.state = 200
                self.arg()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 201
                    self.match(AiLangParser.T__5)
                    self.state = 202
                    self.arg()
                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 210
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
            self.state = 212
            self.match(AiLangParser.T__4)
            self.state = 213
            self.expr(0)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 214
                self.match(AiLangParser.T__5)
                self.state = 215
                self.expr(0)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 221
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
            self.state = 226
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.basic_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.generic_list()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
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
            self.state = 228
            self.match(AiLangParser.T__9)
            self.state = 229
            self.df_val()
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 230
                self.match(AiLangParser.T__5)
                self.state = 231
                self.df_val()
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 237
            self.match(AiLangParser.T__10)
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
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 239
                self.id_()
                self.state = 240
                self.match(AiLangParser.T__11)


            self.state = 244
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
        self.enterRule(localctx, 46, self.RULE_member)
        try:
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = AiLangParser.BasicIDMemberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.id_()
                pass
            elif token in [24]:
                localctx = AiLangParser.IntIDMemberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.match(AiLangParser.INT)
                pass
            elif token in [1]:
                localctx = AiLangParser.ListIDMemberContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.match(AiLangParser.T__0)
                self.state = 249
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
        self.enterRule(localctx, 48, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(AiLangParser.T__7)
            self.state = 253
            self.id_()
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 254
                self.match(AiLangParser.REF)
                self.state = 255
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
        self.enterRule(localctx, 50, self.RULE_basic_list)
        self._la = 0 # Token type
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = AiLangParser.NumListContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(AiLangParser.T__4)
                self.state = 259
                self.num()
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 260
                    self.match(AiLangParser.T__5)
                    self.state = 261
                    self.num()
                    self.state = 266
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 267
                self.match(AiLangParser.T__6)
                pass

            elif la_ == 2:
                localctx = AiLangParser.StrListContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.match(AiLangParser.T__4)
                self.state = 270
                self.str_()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 271
                    self.match(AiLangParser.T__5)
                    self.state = 272
                    self.str_()
                    self.state = 277
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 278
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
        self.enterRule(localctx, 52, self.RULE_basic_val)
        try:
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23, 24]:
                localctx = AiLangParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.num()
                pass
            elif token in [22]:
                localctx = AiLangParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.str_()
                pass
            elif token in [5]:
                localctx = AiLangParser.Group_basic_valContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 284
                self.match(AiLangParser.T__4)
                self.state = 285
                self.basic_val()
                self.state = 286
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
        self.enterRule(localctx, 54, self.RULE_num)
        try:
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                localctx = AiLangParser.IntigerLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(AiLangParser.INT)
                pass
            elif token in [23]:
                localctx = AiLangParser.FloatLiteralContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 291
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
        self.enterRule(localctx, 56, self.RULE_str)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
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
        self._predicates[14] = self.expr_sempred
        self._predicates[15] = self.assignable_sempred
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
         




