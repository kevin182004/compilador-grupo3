"""
Interfaz gráfica para un mini-compilador Python usando Tkinter

Esta aplicación permite:
1. Ingresar código en un lenguaje simple
2. Realizar análisis léxico (tokenización)
3. Ejecutar análisis sintáctico y semántico
4. Mostrar resultados en tiempo real
"""

import tkinter as tk
from lexer import lexer  # Importa el analizador léxico
from parser import parser, symbol_table  # Importa el parser y tabla de símbolos
import sys
import io

def run_compiler():
    """
    Función principal que ejecuta el proceso de compilación:
    1. Obtiene el código del área de texto
    2. Realiza el análisis léxico
    3. Ejecuta el análisis sintáctico/semántico
    4. Muestra los resultados en el área de salida
    """
    # Obtiene el código ingresado por el usuario
    code = text_input.get("1.0", tk.END)
    
    # Configura el lexer con el código de entrada
    lexer.input(code)
    
    # Limpia el área de salida
    output.delete("1.0", tk.END)
    
    # --- ANÁLISIS LÉXICO ---
    output.insert(tk.END, "Tokens generados:\n")
    while True:
        tok = lexer.token()
        if not tok:  # Fin de los tokens
            break
        # Muestra cada token encontrado (tipo y valor)
        output.insert(tk.END, f"{tok.type}: {tok.value}\n")

    # --- ANÁLISIS SINTÁCTICO/SEMÁNTICO ---
    output.insert(tk.END, "\nAnalisis semantico y sintactico\n")
    
    # Limpia la tabla de símbolos para nueva ejecución
    symbol_table.clear()
    
    # Redirige la salida estándar a un buffer para capturarla
    buffer = io.StringIO()
    sys.stdout = buffer
    
    try:
        # Ejecuta el parser sobre el código
        parser.parse(code)
    except Exception as e:
        # Captura cualquier error durante el análisis
        print(f"✘ Error en compilación: {e}")
    finally:
        # Restaura la salida estándar
        sys.stdout = sys.__stdout__
    
    # Muestra los resultados del análisis
    output.insert(tk.END, buffer.getvalue())

# --- INTERFAZ GRÁFICA ---
root = tk.Tk()
root.title("Mini Compilador")

# Área de entrada de código
text_input = tk.Text(root, height=10, font=("Consolas", 12))
text_input.insert("1.0", "int x = 5;\nfloat y = x + 3.2;\nprint(y);")  # Código de ejemplo
text_input.pack(padx=10, pady=10)

# Botón de ejecución
run_button = tk.Button(root, text="Compilar", command=run_compiler)
run_button.pack(pady=5)

# Área de salida de resultados
output = tk.Text(root, height=15, font=("Consolas", 11))
output.pack(padx=10, pady=10)

# Inicia el bucle principal de la aplicación
root.mainloop()