# pylint: disable=invalid-name
import sys
import os
from pathlib import Path
from typing import Any
from antlr4.ParserRuleContext import TerminalNodeImpl
from antlr4.Token import Token
from antlr4 import ParserRuleContext
import pandas as pd
from grammar.AiLangParser import AiLangParser


def getTerminalSymbol(child: Any) -> str:
    if isinstance(child, Token):
        return child.text
    if isinstance(child, TerminalNodeImpl):
        return child.symbol.text
    return getTerminalSymbol(child.getChild(0))


def getAllIds(node: ParserRuleContext) -> list[str]:
    ids = node.getTypedRuleContexts(AiLangParser.IdContext)
    result: list[str] = []
    for ident in ids:
        result.append(getTerminalSymbol(ident))
    return result


def tf2d(filename: str) -> pd.DataFrame:
    try:
        f = Path(filename).resolve()
        _, ext = os.path.splitext(f)
        if ext == ".csv":
            return pd.read_csv(f)
    except Exception as e:
        print(e)
        sys.exit(1)
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
