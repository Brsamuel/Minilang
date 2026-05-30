import ply.lex as lex

reserved = {
    'LET': 'LET',
    'PRINT': 'PRINT',
    'IF': 'IF',
    'ELIF': 'ELIF',
    'ELSE': 'ELSE',
    'FOR': 'FOR',
    'WHILE': 'WHILE',
    'END': 'END',
    'TO': 'TO'
}

tokens = [
    'ID',
    'NUMBER',
    'STRING',
    'EQUALS',
    'GREATER',
    'LESS',
    'GREATER_EQUAL',
    'LESS_EQUAL',
    'EQUAL_EQUAL',
    'NOT_EQUAL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE'
] + list(reserved.values())

t_GREATER_EQUAL = r'>='
t_LESS_EQUAL    = r'<='
t_EQUAL_EQUAL   = r'=='
t_NOT_EQUAL     = r'!='
t_GREATER       = r'>'
t_LESS          = r'<'
t_EQUALS        = r'='
t_PLUS          = r'\+'
t_MINUS         = r'-'
t_TIMES         = r'\*'
t_DIVIDE        = r'/'

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value.replace('"', '')
    return t

def t_NUMBER(t):
    r'-?\d+(\.\d+)?'
    if '.' in t.value:
        t.value = float(t.value)
    else:
        t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f'Caractere invÃ¡lido: {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()