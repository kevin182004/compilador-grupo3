"""
Parser para un lenguaje de programación simple implementado con PLY (Python Lex-Yacc)

Este módulo implementa las reglas sintácticas y semánticas para:
1. Declaración de variables con tipos (int/float)
2. Operaciones aritméticas básicas
3. Sentencias de impresión
4. Verificación de tipos y manejo de errores

Estructura principal:
- Tabla de símbolos para seguimiento de variables
- Reglas gramaticales con acciones semánticas
- Manejo de errores sintácticos y semánticos
"""
import ply.yacc as yacc
from lexer import tokens  # Importa los tokens definidos en el analizador léxico

# Tabla de símbolos global para almacenar variables y sus tipos
symbol_table = {}

# Definición de precedencia y asociatividad de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),  # Operadores con misma precedencia, asociatividad izquierda
)

# --- REGLAS GRAMATICALES ---

def p_program(p):
    """program : statement_list
    Regla inicial que define un programa como una lista de statements"""
    print("✔ Análisis sintáctico completado correctamente")

def p_statement_list(p):
    """statement_list : statement_list statement 
                     | statement
    Define una lista de statements como recursiva o un solo statement"""
    pass  # Sintaxis pura, no requiere acción

def p_statement_declaration(p):
    """statement : type ID EQUALS expression SEMI
    Maneja declaraciones de variables con asignación (ej: 'int x = 5;')"""
    var_name = p[2]  # Nombre de la variable
    var_type = p[1]   # Tipo declarado (int/float)
    
    # Verificación de variable ya declarada
    if var_name in symbol_table:
        print(f"✘ Error semántico: Variable '{var_name}' ya declarada")
        return
    
    # Determinación del tipo de la expresión
    expr_value = p[4]
    expr_type = 'float' if isinstance(expr_value, float) else 'int'
    
    # Validación de compatibilidad de tipos
    if var_type == 'int' and expr_type == 'float':
        print(f"✘ Error de tipos: No se puede asignar float a int en '{var_name}'")
    else:
        symbol_table[var_name] = var_type  # Almacenamiento en tabla de símbolos
        print(f"✔ Declaración válida: {var_name} como {var_type}")

def p_statement_print(p):
    """statement : PRINT LPAREN ID RPAREN SEMI
    Maneja sentencias de impresión (ej: 'print(variable);')"""
    var_name = p[3]
    if var_name not in symbol_table:
        print(f"✘ Error: Variable '{var_name}' no declarada")
    else:
        print(f"✔ Sentencia print válida para variable '{var_name}'")

def p_type(p):
    """type : INT 
           | FLOAT
    Define los tipos de datos soportados"""
    p[0] = p[1]  # Pasa el tipo (int/float) hacia arriba

def p_expression_binop(p):
    """expression : expression PLUS expression
                 | expression MINUS expression
    Maneja operaciones aritméticas binarias con conversión implícita"""
    # Promoción de tipo: si algún operando es float, resultado es float
    left_type = isinstance(p[1], float)
    right_type = isinstance(p[3], float)
    p[0] = float() if left_type or right_type else int()

def p_expression_number(p):
    """expression : NUMBER
    Maneja literales numéricos (enteros y flotantes)"""
    p[0] = p[1]  # Retorna el valor del número

def p_expression_id(p):
    """expression : ID
    Maneja referencias a variables identificadas"""
    var_name = p[1]
    if var_name not in symbol_table:
        print(f"✘ Error: Variable '{var_name}' no declarada")
    p[0] = 0  # Valor por defecto para continuar el análisis

def p_error(p):
    """Manejador de errores sintácticos"""
    if p:
        # Error en un token específico
        print(f"✘ Error de sintaxis en token '{p.value}' (tipo {p.type})")
    else:
        # Fin de archivo inesperado
        print("✘ Error de sintaxis: Fin de entrada inesperado")

# Construcción del parser
parser = yacc.yacc(debug=False)  # Se puede activar debug para troubleshooting
