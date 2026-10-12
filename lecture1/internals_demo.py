"""How CPython reads a line of code: tokens, syntax tree, bytecode (Lecture 1)."""

import ast
import dis
import io
import tokenize

code = "x = 5 + 3"

print("== Tokens ==")
for token in tokenize.generate_tokens(io.StringIO(code).readline):
    print(token)

print("== Abstract syntax tree ==")
print(ast.dump(ast.parse(code), indent=2))


def example():
    x = 5 + 3
    return x


print("== Bytecode ==")
dis.dis(example)
