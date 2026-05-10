# pylint: disable=invalid-name
import sys
from antlr4 import FileStream, CommonTokenStream
from ailang.grammar.AiLangLexer import AiLangLexer
from ailang.grammar.AiLangParser import AiLangParser

import ailang.lib.AiLangLib as _

from ailang.engine.Interpreter import Interpreter

# TODO: add argparser library to make everything simpler

def main():
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        print("provide file")
        sys.exit(1)

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


if __name__ == "__main__":

    main()
