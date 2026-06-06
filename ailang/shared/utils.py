# pylint: disable=invalid-name
import sys
import os
import urllib.request
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from antlr4.ParserRuleContext import TerminalNodeImpl
from antlr4.Token import Token
from antlr4 import ParserRuleContext
import pandas as pd
from ailang.grammar.AiLangParser import AiLangParser

_AILANG_DATA_DIR = Path(os.environ.get("AILANG_DATA_DIR", ".ailang/data"))


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


def _ensureDataDir() -> None:
    _AILANG_DATA_DIR.mkdir(parents=True, exist_ok=True)


def _loadFromUrl(url: str) -> pd.DataFrame:
    _ensureDataDir()
    filename = Path(urlparse(url).path).name
    if not filename.endswith(".csv"):
        print(f"Only .csv files can be loaded from a URL: {url}")
        sys.exit(1)
    dest = _AILANG_DATA_DIR / filename
    if not dest.exists():
        urllib.request.urlretrieve(url, dest)
        print(f"Downloaded {url} -> {dest}")
    return pd.read_csv(dest)


def tf2d(filename: str) -> pd.DataFrame:
    _ensureDataDir()

    if filename.startswith(("http://", "https://")):
        return _loadFromUrl(filename)

    f = Path(filename)
    if f.suffix != ".csv":
        print(f"Only .csv files are supported: {filename}")
        sys.exit(1)

    if f.exists():
        return pd.read_csv(f)

    data_fallback = _AILANG_DATA_DIR / f.name
    if data_fallback.exists():
        return pd.read_csv(data_fallback)

    print(f"File not found: {filename}")
    sys.exit(1)


def ensureDataDir() -> Path:
    """Public helper so other modules can also store files in the data dir."""
    _ensureDataDir()
    return _AILANG_DATA_DIR


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
