from lexer import lexer
from parser import parser
from generator import Generator

# =========================
# LER CÓDIGO
# =========================

with open("programa.mini", "r", encoding="utf-8") as file:

    code = file.read()

# =========================
# LEXER
# =========================

lexer.input(code)

print("TOKENS:")

for token in lexer:

    print(token)

# =========================
# PARSER
# =========================

ast = parser.parse(code)

print("\nAST:")
print(ast)

# =========================
# GENERATOR
# =========================

generator = Generator()

python_code = generator.generate(ast)

print("\nPYTHON GERADO:")
print(python_code)

# =========================
# SALVAR OUTPUT
# =========================

with open("output.py", "w", encoding="utf-8") as file:

    file.write(python_code)

print("\nArquivo output.py gerado com sucesso!")