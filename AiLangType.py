from __future__ import annotations

from antlr4 import ParserRuleContext

from grammar.AiLangParser import AiLangParser as ap
from typing import Any, override
from enum import StrEnum, auto
import utils
import pandas as pd
from abc import ABC


class NumTypes(StrEnum):
    INT = auto()
    FLOAT = auto()


class AiLangType:
    def __init__(self, val):
        self.val = val

    def get(self) -> Any:
        return self.val

    @staticmethod
    def make(node) -> AiLangType:
        return NoneType()


class BasicValType(AiLangType):
    def __init__(self, val):
        super().__init__(val)

    @staticmethod
    def make(node: ParserRuleContext) -> BasicValType:
        numCtx = node.getTypedRuleContext(ap.NumContext, 0)
        if numCtx is not None:
            return NumType.make(numCtx)

        strCtx = node.getTypedRuleContext(ap.StrContext, 0)
        if strCtx is not None:
            return StrType.make(strCtx)

        basicValCtx = node.getTypedRuleContext(ap.Basic_valContext, 0)
        if basicValCtx is not None:
            return BasicValType.make(basicValCtx)

        raise ValueError("NonImplemented type")


class NumType(BasicValType):
    def __init__(self, val, type):
        super().__init__(val)
        self.type = type

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
    def __init__(self, val):
        super().__init__(val)

    @staticmethod
    @override
    def make(node: ParserRuleContext) -> BasicValType:
        string = utils.getTerminalSymbol(node.getChild(0))[1:-1]
        return StrType(string)


class DfItem(AiLangType):
    def __init__(self, df: pd.DataFrame, item: str):
        self.df = df
        self.item = item

    def get(self):
        if self.item not in self.df:
            self.df[self.item] = pd.Series()
        return ListType(list(self.df[self.item]))


class DfType(AiLangType):
    def __init__(self, val):
        super().__init__(val)

    @staticmethod
    def make(node):
        if not isinstance(node, ap.DfContext):
            raise ValueError()

        if isinstance(node, ap.EmptyDfContext):
            return DfType(pd.DataFrame())

        data = {}
        i = 0
        for ch in node.getTypedRuleContexts(ap.Df_valContext):
            id = ch.getTypedRuleContext(ap.IdContext, 0)
            id = utils.getTerminalSymbol(id) if id else i
            l_val = BasicListType.make(
                ch.getTypedRuleContext(ap.Basic_listContext, 0)
            ).get()
            data[str(id)] = l_val
            i += 1
        return DfType(pd.DataFrame.from_dict(data))


class ListType(AiLangType):
    def __init__(self, val):
        super().__init__(val)

    @staticmethod
    def make(node) -> AiLangType:

        if isinstance(node, ap.Basic_listContext):
            return BasicListType.make(node)

        raise ValueError()


class BasicListType(ListType):
    def __init__(self, val):
        super().__init__(val)

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
    def __init__(self, val):
        super().__init__(val)


class NoneType(AiLangType, metaclass=utils.Singleton):
    def __init__(self):
        super().__init__(None)
