import ply.yacc as yacc
from lexer import tokens

# =========================
# PRECEDÊNCIA
# =========================

precedence = (

    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# =========================
# PROGRAMA
# =========================

def p_program(p):

    '''
    program : statements
    '''

    p[0] = p[1]

# =========================
# MÚLTIPLOS COMANDOS
# =========================

def p_statements_multiple(p):

    '''
    statements : statements statement
    '''

    p[0] = p[1] + [p[2]]

# =========================
# UM COMANDO
# =========================

def p_statements_single(p):

    '''
    statements : statement
    '''

    p[0] = [p[1]]

# =========================
# EXPRESSÕES MATEMÁTICAS
# =========================

def p_expression_binop(p):

    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
    '''

    p[0] = {

        "type": "BINARY_OP",

        "left": p[1],

        "operator": p[2],

        "right": p[3]
    }

# =========================
# NÚMERO
# =========================

def p_expression_number(p):

    '''
    expression : NUMBER
    '''

    p[0] = p[1]

# =========================
# VARIÁVEL
# =========================

def p_expression_id(p):

    '''
    expression : ID
    '''

    p[0] = p[1]

# =========================
# CONDIÇÕES
# =========================

def p_condition(p):

    '''
    condition : expression GREATER expression
              | expression LESS expression
              | expression EQUAL_EQUAL expression
    '''

    p[0] = {

        "left": p[1],

        "operator": p[2],

        "right": p[3]
    }

# =========================
# PRINT STRING
# =========================

def p_statement_print_string(p):

    '''
    statement : PRINT STRING
    '''

    p[0] = {

        "type": "PRINT",

        "value": p[2],

        "value_type": "STRING"
    }

# =========================
# PRINT VARIÁVEL
# =========================

def p_statement_print_variable(p):

    '''
    statement : PRINT ID
    '''

    p[0] = {

        "type": "PRINT",

        "value": p[2],

        "value_type": "VARIABLE"
    }

# =========================
# LET EXPRESSÃO
# =========================

def p_statement_let_expression(p):

    '''
    statement : LET ID EQUALS expression
    '''

    p[0] = {

        "type": "LET",

        "name": p[2],

        "value": p[4]
    }

# =========================
# LET STRING
# =========================

def p_statement_let_string(p):

    '''
    statement : LET ID EQUALS STRING
    '''

    p[0] = {

        "type": "LET",

        "name": p[2],

        "value": p[4]
    }

# =========================
# IF SIMPLES
# =========================

def p_statement_if(p):

    '''
    statement : IF condition statements END
    '''

    p[0] = {

        "type": "IF",

        "left": p[2]["left"],

        "operator": p[2]["operator"],

        "right": p[2]["right"],

        "body": p[3],

        "elifs": [],

        "else": None
    }

# =========================
# IF + ELSE
# =========================

def p_statement_if_else(p):

    '''
    statement : IF condition statements ELSE statements END
    '''

    p[0] = {

        "type": "IF",

        "left": p[2]["left"],

        "operator": p[2]["operator"],

        "right": p[2]["right"],

        "body": p[3],

        "elifs": [],

        "else": p[5]
    }

# =========================
# IF + ELIF
# =========================

def p_statement_if_elif(p):

    '''
    statement : IF condition statements ELIF condition statements END
    '''

    p[0] = {

        "type": "IF",

        "left": p[2]["left"],

        "operator": p[2]["operator"],

        "right": p[2]["right"],

        "body": p[3],

        "elifs": [

            {

                "left": p[5]["left"],

                "operator": p[5]["operator"],

                "right": p[5]["right"],

                "body": p[6]
            }
        ],

        "else": None
    }

# =========================
# IF + ELIF + ELSE
# =========================

def p_statement_if_elif_else(p):

    '''
    statement : IF condition statements ELIF condition statements ELSE statements END
    '''

    p[0] = {

        "type": "IF",

        "left": p[2]["left"],

        "operator": p[2]["operator"],

        "right": p[2]["right"],

        "body": p[3],

        "elifs": [

            {

                "left": p[5]["left"],

                "operator": p[5]["operator"],

                "right": p[5]["right"],

                "body": p[6]
            }
        ],

        "else": p[8]
    }

# =========================
# FOR
# =========================

def p_statement_for(p):

    '''
    statement : FOR ID EQUALS expression TO expression statements END
    '''

    p[0] = {

        "type": "FOR",

        "variable": p[2],

        "start": p[4],

        "end": p[6],

        "body": p[7]
    }

# =========================
# ERRO
# =========================

def p_error(p):

    print("Erro de sintaxe!")

# =========================
# CRIAR PARSER
# =========================

parser = yacc.yacc()