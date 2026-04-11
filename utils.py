from antlr4.ParserRuleContext import TerminalNodeImpl
from antlr4.Token import Token
from antlr4 import ParserRuleContext

from grammar.AiLangParser import AiLangParser


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
