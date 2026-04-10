from antlr4.ParserRuleContext import TerminalNodeImpl
from antlr4.Token import Token

def getTerminalSymbol(child) -> str:
    if isinstance(child, Token):
        return child.text
    if isinstance(child, TerminalNodeImpl):
        return child.symbol.text
    return getTerminalSymbol(child.getChild(0))
