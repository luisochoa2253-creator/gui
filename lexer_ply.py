# lexer_ply.py (Versión Verificada)

import ply.lex as lex

# Lista de palabras reservadas
reserved = {
   'if': 'IF', 'else': 'ELSE', 'while': 'WHILE', 'print': 'PRINT',
   'int': 'TIPO', 'float': 'TIPO'
}

# Lista de tokens
tokens = [
    'ID', 'NUM', 'ASIGN', 'OP_SUMA', 'OP_MUL', 'OP_REL',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON'
] + list(reserved.values())

# Expresiones regulares para tokens simples
t_ASIGN   = r'='
t_OP_SUMA = r'\+|-'
t_OP_MUL  = r'\*|/'
t_OP_REL  = r'==|!=|<=|>=|<|>'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMICOLON = r';'

# Regla para identificadores
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Regla para números
def t_NUM(t):
    r'\d+(\.\d*)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Regla para rastrear los números de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

# Función para manejar errores léxicos
def t_error(t):
    error_message = f"Error Léxico: Caracter ilegal '{t.value[0]}' en línea {t.lexer.lineno}\n"
    if not hasattr(t.lexer, 'lex_errors'):
        t.lexer.lex_errors = []
    t.lexer.lex_errors.append(error_message)
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()