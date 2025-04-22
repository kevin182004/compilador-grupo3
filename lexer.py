import ply.lex as lex

tokens = [
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'EQUALS',
    'LPAREN', 'RPAREN', 'SEMI',
    'INT', 'FLOAT', 'PRINT'
]

reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'print': 'PRINT'
}

t_PLUS = r'\+'
t_MINUS = r'-'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
