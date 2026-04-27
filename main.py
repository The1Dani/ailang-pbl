# pylint: disable=invalid-name
import sys
from antlr4 import FileStream, CommonTokenStream
from antlr4.InputStream import InputStream
from grammar.AiLangLexer import AiLangLexer
from grammar.AiLangParser import AiLangParser
from Interpreter import Interpreter

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = AiLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = AiLangParser(token_stream)
    tree = parser.prog()
    if len(sys.argv) >= 3 and sys.argv[2] == "-parse":
        print(tree.toStringTree(recog=parser))
        # sys.exit(0)
    Interpreter(tree).interp()
    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)
