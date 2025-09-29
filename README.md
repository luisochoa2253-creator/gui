# Analizador Léxico y Sintáctico con PLY y Tkinter

Este proyecto es una herramienta académica para el análisis de código fuente, desarrollada en Python. Implementa un analizador léxico y sintáctico para un lenguaje de programación simple y presenta los resultados en una interfaz gráfica de usuario (GUI) amigable.



---
## Características

* **Interfaz Gráfica Interactiva:** Permite escribir o pegar código directamente en la aplicación para un análisis inmediato.
* **Análisis Léxico:** Descompone el código fuente en una tabla de tokens, identificando palabras clave, identificadores, números y operadores.
* **Análisis Sintáctico:** Valida la estructura del código según una gramática definida y reporta si la sintaxis es correcta.
* **Manejo Detallado de Errores:** Reporta errores léxicos (caracteres inválidos) y sintácticos (estructura incorrecta) de forma clara, indicando el token y la línea del problema.
* **Traza de Análisis:** Muestra una tabla con las reglas de la gramática que se van aplicando durante el análisis sintáctico, permitiendo visualizar el proceso de validación.

---
## Tecnologías Utilizadas

* **Python 3:** Como lenguaje principal de desarrollo.
* **PLY (Python Lex-Yacc):** Biblioteca para la construcción de analizadores léxicos y sintácticos.
* **Tkinter:** Biblioteca estándar de Python para la creación de la interfaz gráfica de usuario.

---
## Componentes del Sistema

El proyecto está organizado en tres módulos principales para una clara separación de responsabilidades:

1.  **`lexer_ply.py`:** Define los tokens del lenguaje (el vocabulario) y las reglas para identificarlos en el código fuente.
2.  **`parser_ply.py`:** Define la gramática del lenguaje (la estructura de las "oraciones") y la lógica para validar la secuencia de tokens.
3.  **`analizador_gui.py`:** Crea y gestiona la ventana de la aplicación, los campos de texto y el botón que une la lógica del analizador con la interacción del usuario.

---
## Requisitos

* Python 3.x
* Biblioteca `ply` (si no la tienes, instálala con `pip install ply`)

---
## Cómo Ejecutar

1.  Asegúrate de tener los tres archivos (`lexer_ply.py`, `parser_ply.py`, `analizador_gui.py`) en la misma carpeta.
2.  Abre una terminal o línea de comandos en esa carpeta.
3.  Ejecuta el siguiente comando:
    ```sh
    python analizador_gui.py
    ```
4.  Se abrirá la ventana de la aplicación. Escribe o pega el código que deseas analizar en el panel superior.
5.  Presiona el botón **"Analizar Código"** para ver los resultados en el panel inferior.
