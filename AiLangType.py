from __future__ import annotations

from typing import Any, override
from enum import StrEnum, auto

from antlr4 import ParserRuleContext
import pandas as pd

from grammar.AiLangParser import AiLangParser as ap
import utils


class NumTypes(StrEnum):
    """Enum for available Numerical types in BasicValType"""

    INT = auto()
    FLOAT = auto()


class AiLangType:
    """Type Implementation for AiLang, Types are wrappers for the actual values"""

    def __init__(self, val):
        self.val = val

    def get(self) -> Any:
        return self.val

    @staticmethod
    def make(node) -> AiLangType:
        _ = node
        return NoneType()


class BasicValType(AiLangType):
    """Basic Value Type in AiLang it is parent class for Num and Str Types"""

    @staticmethod
    def make(node: ParserRuleContext) -> BasicValType:
        num_ctx = node.getTypedRuleContext(ap.NumContext, 0)
        if num_ctx is not None:
            return NumType.make(num_ctx)

        str_ctx = node.getTypedRuleContext(ap.StrContext, 0)
        if str_ctx is not None:
            return StrType.make(str_ctx)

        basic_val_ctx = node.getTypedRuleContext(ap.Basic_valContext, 0)
        if basic_val_ctx is not None:
            return BasicValType.make(basic_val_ctx)

        raise ValueError("NonImplemented type")


class NumType(BasicValType):
    """Num Type"""

    def __init__(self, val, numerical_type: NumTypes):
        super().__init__(val)
        self.type = numerical_type

    @staticmethod
    @override
    def make(node) -> NumType:
        number = utils.getTerminalSymbol(node)
        if isinstance(node, ap.IntigerLiteralContext):
            return NumType(int(number), NumTypes.INT)
        if isinstance(node, ap.FloatLiteralContext):
            num = float(".".join(map(lambda x: str(int(x)), number.split("."))))
            return NumType(num, NumTypes.FLOAT)
        raise ValueError()


class StrType(BasicValType):
    """Str Type"""

    @staticmethod
    @override
    def make(node: ParserRuleContext) -> BasicValType:
        string = utils.getTerminalSymbol(node.getChild(0))[1:-1]
        return StrType(string)


class DfItem(AiLangType):
    """Df Item type is a field of a DataFrameType and it ussually stores pd.Series as a value"""

    # TODO: add a setter that will update the parent Dataframe Type as well


class DfType(AiLangType):
    """DataFrame Type of AiLang stores Dataframes"""

    @staticmethod
    def make(node):
        if not isinstance(node, ap.DfContext):
            raise ValueError()

        if isinstance(node, ap.EmptyDfContext):
            return DfType(pd.DataFrame())

        data = {}
        i = 0
        for ch in node.getTypedRuleContexts(ap.Df_valContext):
            ident = ch.getTypedRuleContext(ap.IdContext, 0)
            ident = utils.getTerminalSymbol(ident) if ident else i
            l_val = BasicListType.make(
                ch.getTypedRuleContext(ap.Basic_listContext, 0)
            ).get()
            data[str(ident)] = l_val
            i += 1
        return DfType(pd.DataFrame.from_dict(data))


class ListType(AiLangType):
    """List Type"""

    @staticmethod
    def make(node) -> AiLangType:

        if isinstance(node, ap.Basic_listContext):
            return BasicListType.make(node)

        raise ValueError()


class BasicListType(ListType):
    """Basic List Type, lists of basic values"""

    @staticmethod
    def make(node) -> AiLangType:
        l_val: list | None = None
        if isinstance(node, ap.NumListContext):
            l_val = []
            # Add float and boolean
            for ch in node.getTypedRuleContexts(ap.IntigerLiteralContext):
                l_val.append(NumType.make(ch).get())
        if isinstance(node, ap.StrListContext):
            l_val = []
            for ch in node.getTypedRuleContexts(ap.StrContext):
                l_val.append(StrType.make(ch).get())

        if l_val is not None:
            return BasicListType(l_val)

        raise ValueError()


class BoolType(AiLangType):
    """Implement me!"""


class NoneType(AiLangType, metaclass=utils.Singleton):
    """None Type"""

    def __init__(self):
        super().__init__(None)
