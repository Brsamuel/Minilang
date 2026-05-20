from lexer import Lexer
from parser import Parser
from generator import Generator

with open("programa.mini", "r", encoding="utf-8") as file:

    code = file.read()

# LEXER
lexer = Lexer()

tokens = lexer.tokenize(code)

print("TOKENS:")
print(tokens)

# PARSER
parser = Parser()

ast = parser.parse(tokens)

print("\nAST:")
print(ast)

# GENERATOR
generator = Generator()

python_code = generator.generate(ast)

print("\nPYTHON GERADO:")
print(python_code)

# SALVAR ARQUIVO
with open("output.py", "w", encoding="utf-8") as file:

    file.write(python_code)

print("\nArquivo output.py gerado com sucesso!")