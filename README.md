# Language Translator from Python to C</h1>
### [ANTLR4 as a tool for lexer/parser auto generation](https://github.com/antlr/antlr4). Getting started</h3>

```console
pip3 install antlr4-python3-runtime
```

Write your grammar to `*.g4` file and run on of the following commands to see antlr4 in work:

*output is a tree in text form:*

```console
antlr4-parse Mygrammar.g4 prog -tree < input
```

*Following command is useful for debugging and shows you the tokens were parsed:*
```console
antlr4-parse Expr.g4 prog -tokens -trace < input
```

*This command renders a beautiful picture with [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree)*
```console
antlr4-parse Expr.g4 prog -gui < input
```

For instance your grammar name is MyGrammar, then the following command helps you to generate code for lexer, parser and visitor.
```console
antlr4 -Dlanguage=Python3 MyGrammar.g4 -visitor -o Generated
```
Actually you can specify one of the other languages which are supported by antr4, but by default it is Java.    

Now you have an opportunity to inherit your own visitor from MyGrammarVisitor and do whatever you want with your AST.
For instance you can implement Language translator from Python to C
