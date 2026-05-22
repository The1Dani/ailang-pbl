# +#+#+#+# pylint: disable=invalid-name
import argparse
from antlr4 import FileStream, CommonTokenStream
from ailang.grammar.AiLangLexer import AiLangLexer
from ailang.grammar.AiLangParser import AiLangParser

import ailang.lib.AiLangLib as _

from ailang.engine.Interpreter import Interpreter


def main():
    parser = argparse.ArgumentParser(prog="ailang")
    parser.add_argument("file", help="AiLang source file")
    # Kept as single-dash flags to match existing usage.
    parser.add_argument(
        "--parse", dest="parse", action="store_true", help="Print parse tree"
    )
    parser.add_argument(
        "--proc-tree",
        dest="proc_tree",
        action="store_true",
        help="Print pipline tree",
    )
    args = parser.parse_args()

    input_stream = FileStream(args.file)

    lexer = AiLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    ailang_parser = AiLangParser(token_stream)
    tree = ailang_parser.prog()

    if args.parse:
        print(tree.toStringTree(recog=ailang_parser))

    Interpreter(tree).interp(print_tree=args.proc_tree)
    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)


if __name__ == "__main__":

    main()
