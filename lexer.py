"""
Analizador Léxico (Lexer) para un lenguaje de programación simple implementado con PLY

Este módulo define:
1. Los tokens del lenguaje
2. Las expresiones regulares para reconocer cada token
3. Las reglas para manejar identificadores, números y errores
"""

import ply.lex as lex  # Importa el módulo lex de PLY

# --- DEFINICIÓN DE TOKENS ---

# Lista de nombres de tokens (requerido por PLY)
tokens = [
    'ID', 'NUMBER',        # Identificadores y números
    'PLUS', 'MINUS',       # Operadores aritméticos
    'EQUALS',              # Operador de asignación  
    'LPAREN', 'RPAREN',    # Paréntesis
    'SEMI',                # Punto y coma
    'INT', 'FLOAT',        # Palabras reservadas para tipos
    'PRINT'                # Palabra reservada para impresión
]

# Diccionario de palabras reservadas y sus tokens correspondientes
reserved = {
    'int': 'INT',      # Tipo entero
    'float': 'FLOAT',  # Tipo flotante
    'print': 'PRINT'   # Sentencia de impresión
}

# --- EXPRESIONES REGULARES PARA TOKENS SIMPLES ---

# Operadores y símbolos (definidos como cadenas regulares)
t_PLUS = r'\+'     # Operador suma
t_MINUS = r'-'     # Operador resta
t_EQUALS = r'='    # Operador asignación
t_LPAREN = r'\('   # Paréntesis izquierdo
t_RPAREN = r'\)'   # Paréntesis derecho
t_SEMI = r';'      # Punto y coma (fin de sentencia)

# Caracteres a ignorar (espacios y tabs)
t_ignore = ' \t'

# --- FUNCIONES DE TOKENS COMPLEJOS ---

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'  # Regex para identificadores
    """
    Maneja identificadores:
    - Primero verifica si es palabra reservada
    - Si no, lo clasifica como ID normal
    """
    t.type = reserved.get(t.value, 'ID')  # Busca en palabras reservadas
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'  # Regex para enteros y flotantes
    """
    Maneja literales numéricos:
    - Convierte a float si tiene punto decimal
    - Mantiene como int si es entero
    """
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_newline(t):
    r'\n+'  # Regex para saltos de línea
    """
    Maneja saltos de línea:
    - Incrementa el contador de líneas del lexer
    """
    t.lexer.lineno += len(t.value)

def t_error(t):
    """
    Maneja caracteres no reconocidos:
    - Muestra mensaje de error
    - Avanza una posición para continuar el análisis
    """
    print(f"Caracter ilegal: '{t.value[0]}'")
    t.lexer.skip(1)

# Construye el lexer
lexer = lex.lex()

"""
Características principales:
1. Distingue entre identificadores normales y palabras reservadas
2. Convierte automáticamente números a su tipo correcto (int/float)
3. Lleva registro del número de línea para mensajes de error
4. Ignora espacios en blanco innecesarios
5. Proporciona mensajes de error para caracteres inválidos
"""

