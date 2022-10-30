import sys

from antlr4 import *

from PythonStatementsVisitor import PythonStatementsVisitor
from parseLibrary.PythonLexer import PythonLexer
from parseLibrary.PythonParser import PythonParser


def main(argv):
    if len(argv) != 3:
        print(
            "Invalid usage. python main.py <input with python code> <output for c code>",
            file=sys.stderr
        )
        return

    with open(argv[1], 'r') as pythonScript:
        data = InputStream(''.join(pythonScript.readlines()))
        lexer = PythonLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = PythonParser(stream)
        tree = parser.prog()
        # evaluator
        visitor = PythonStatementsVisitor()
        output = visitor(tree)
        with open(argv[2], 'w') as f:
            f.write(output)


if __name__ == '__main__':
    main(sys.argv)
