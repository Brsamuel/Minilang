import ply.lex as lex

# RESERVED WORDS
reserved = {

    'LET': 'LET',
    'PRINT': 'PRINT',
    'IF': 'IF',
    'ELIF': 'ELIF',
    'ELSE': 'ELSE',
    'FOR': 'FOR',
    'END': 'END',
    'TO': 'TO'
}

# TOKENS
tokens = [

    'ID',
    'NUMBER',
    'STRING',

    'EQUALS',

    'GREATER',
    'LESS',
    'EQUAL_EQUAL',

    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE'

] + list(reserved.values())

# =========================
# OPERADORES
# =========================

t_EQUALS = r'='
t_GREATER = r'>'
t_LESS = r'<'
t_EQUAL_EQUAL = r'=='

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# =========================
# STRING
# =========================

def t_STRING(t):

    r'"[^"]*"'

    t.value = t.value.replace('"', '')

    return t

# =========================
# NUMBER
# =========================

def t_NUMBER(t):

    r'-?\d+(\.\d+)?'

    if '.' in t.value:

        t.value = float(t.value)

    else:

        t.value = int(t.value)

    return t

# =========================
# IDENTIFICADOR
# =========================

def t_ID(t):

    r'[a-zA-Z_][a-zA-Z0-9_]*'

    t.type = reserved.get(t.value, 'ID')

    return t

# =========================
# IGNORAR ESPAÇOS
# =========================

t_ignore = ' \t'

# =========================
# NOVA LINHA
# =========================

def t_newline(t):

    r'\n+'

    t.lexer.lineno += len(t.value)

# =========================
# ERRO
# =========================

def t_error(t):

    print(f'Caractere inválido: {t.value[0]}')

    t.lexer.skip(1)

# =========================
# CRIAR LEXER
# =========================

lexer = lex.lex()