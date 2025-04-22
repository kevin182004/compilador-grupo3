import ply.yacc as yacc
from lexer import tokens

symbol_table = {}

precedence = (
    ('left', 'PLUS', 'MINUS'),
)

def p_program(p):
    'program : statement_list'
    print("✔ El parser fue ejecutado correctamente.")

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    pass

def p_statement_declaration(p):
    'statement : type ID EQUALS expression SEMI'
    if p[2] in symbol_table:
        print(f"✘ Error: variable '{p[2]}' ya declarada")
    else:
        expr_type = 'float' if isinstance(p[4], float) else 'int'
        if p[1] == 'int' and expr_type == 'float':
            print(f"✘ Error: no se puede asignar float a int en '{p[2]}'")
        else:
            symbol_table[p[2]] = p[1]
            print(f"✔ Declaración válida: {p[2]} de tipo {p[1]}")

def p_statement_print(p):
    'statement : PRINT LPAREN ID RPAREN SEMI'
    if p[3] not in symbol_table:
        print(f"✘ Error: variable '{p[3]}' no declarada")
    else:
        print(f"✔ Impresión válida: {p[3]}")

def p_type(p):
    '''type : INT
            | FLOAT'''
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression'''
    if isinstance(p[1], float) or isinstance(p[3], float):
        p[0] = float()
    else:
        p[0] = int()

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    if p[1] not in symbol_table:
        print(f"✘ Error: variable '{p[1]}' no declarada")
    p[0] = 0

def p_error(p):
    if p:
        print(f"✘ Error de sintaxis en: '{p.value}'")
    else:
        print("✘ Error de sintaxis: entrada incompleta (EOF)")

parser = yacc.yacc()