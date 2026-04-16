import os
from typing import Any, Type, TypeGuard, TypeVar
from antlr4.ParserRuleContext import TerminalNodeImpl
from antlr4.Token import Token
from antlr4 import ParserRuleContext

from grammar.AiLangParser import AiLangParser
import pandas as pd
from pathlib import Path


        def fromDFtoObj(df):
            if not isinstance(df, pd.DataFrame):
                raise ValueError()
            for col, ser in df.items():
                colObj = AiLangObj(col, ListType(ser))
                obj.setMember(colObj)

def getTerminalSymbol(child) -> str:
    if isinstance(child, Token):
        return child.text
    if isinstance(child, TerminalNodeImpl):
        return child.symbol.text
    return getTerminalSymbol(child.getChild(0))


def getAllIds(node: ParserRuleContext) -> list[str]:
    ids = node.getTypedRuleContexts(AiLangParser.IdContext)
    result: list[str] = []
    for id in ids:
        result.append(getTerminalSymbol(id))
    return result


def tf2d(filename: str) -> pd.DataFrame:
    try:
        f = Path(filename).resolve()
        _, ext = os.path.splitext(f)
        if ext == ".csv":
            return pd.read_csv(f)
    except Exception as e:
        print(e)
        exit(1)
    return pd.DataFrame()


class Singleton(type):
    """
    Singleton metaclass implementation
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
