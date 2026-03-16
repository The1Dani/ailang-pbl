import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from grammar.AiLangLexer import AiLangLexer
from grammar.AiLangParser import AiLangParser

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = AiLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = AiLangParser(token_stream)
    tree = parser.prog()

    lisp_tree_str = tree
    print(lisp_tree_str)