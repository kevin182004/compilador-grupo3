## Elaborado por:
    
- Yampaul Andres Chaux
- Kevin Alexander Niño
- Juan David Marulanda
  
# Compilador en Python

Este proyecto es un compilador construido con Python utilizando PLY (Lex-Yacc) y Tkinter. Su propósito es procesar un lenguaje simple que permite declarar variables, realizar operaciones aritméticas y mostrar resultados mediante `print`.

---

##  Fases del Compilador

1. **Análisis Léxico (`lexer.py`)**
   - Se encarga de dividir el código fuente en tokens.
   - Reconoce palabras clave (`int`, `float`, `print`), identificadores, números, operadores, paréntesis y puntos y coma.

2. **Análisis Sintáctico (`parser.py`)**
   - Define la gramática del lenguaje utilizando `ply.yacc`.
   - Permite declaraciones, expresiones y sentencias `print()`.

3. **Análisis Semántico**
   - Validación del tipo de datos (`int` y `float`).
   - Verificación del uso correcto de variables (declaración previa).
   - Manejo de errores semánticos como redeclaración o incompatibilidad de tipos.

4. **Interfaz Gráfica (`gui.py`)**
   - Implementada con Tkinter.
   - Permite al usuario ingresar código, ejecutarlo y visualizar tokens y análisis directamente desde la ventana gráfica.

---

##  Enfoque Técnico: Análisis Semántico

Este proyecto tiene como eje central el análisis semántico:

- Se construye una **tabla de símbolos** para almacenar variables y sus tipos.
- Se validan los tipos de expresiones y asignaciones.
- Se detectan y reportan errores como:
  - Uso de variables no declaradas
  - Asignación de `float` a `int`
  - Variables redeclaradas

---

##  Diagrama de Flujo del Compilador

```
+----------------------+
|    Código fuente     |
+----------------------+
           ↓
+----------------------+
|  Análisis Léxico     |
+----------------------+
           ↓
+----------------------+
|  Análisis Sintáctico |
+----------------------+
           ↓
+----------------------+
| Análisis Semántico   |
+----------------------+
           ↓
+----------------------+
|   Interfaz (Tkinter) |
+----------------------+
```

---

##  ¿Cómo Ejecutar?

### 1. Requisitos
- Python 3.10 o superior
- Instalar PLY:
```bash
pip install ply
```

### 2. Ejecución
Desde la carpeta del proyecto, ejecuta:

```bash
python gui.py
```

Se abrirá una ventana donde podrás escribir código y ejecutar el análisis.

---

##  Estructura del Proyecto

```
Compilador_Python/
├── gui.py         # Interfaz gráfica
├── lexer.py       # Análisis léxico
├── parser.py      # Análisis sintáctico y semántico
├── parsetab.py    # Tabla de análisis generada por PLY
```

---

##  Ejemplo de Código de Entrada

```c
int x = 5;
float y = x + 3.2;
print(y);
```

### Resultado Esperado

- Tokens generados correctamente
- Análisis semántico exitoso
- Salida:`✔ Declaración válida` `✔ Impresión válida`

---
