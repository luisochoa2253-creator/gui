# parser_ply.py (Versión con recolección de traza)

import ply.yacc as yacc
from lexer_ply import tokens

# --- Definición de la Gramática ---
def p_Programa(p):
    'Programa : Sentencias'
    p[0] = "Análisis finalizado: ¡La sintaxis del programa es correcta! ✅"

def p_Sentencias(p):
    '''Sentencias : Sentencia
                  | Sentencias Sentencia'''
    pass

def p_Sentencia(p):
    '''Sentencia : Declaracion
                 | Asignacion
                 | EstructuraControl
                 | SentenciaPrint'''
    pass

def p_Declaracion(p):
    'Declaracion : TIPO ID SEMICOLON'
    parser.parse_trace.append( ('Declaracion -> TIPO ID ;', f'tipo:{p[1]}, id:{p[2]}') )

def p_Asignacion(p):
    'Asignacion : ID ASIGN Expresion SEMICOLON'
    parser.parse_trace.append( ('Asignacion -> ID = Expresion ;', f'id:{p[1]}') )

def p_EstructuraControl_if(p):
    'EstructuraControl : IF LPAREN Expresion RPAREN LBRACE Sentencias RBRACE'
    parser.parse_trace.append( ('EstructuraControl -> if (...)', '...') )

def p_EstructuraControl_ifelse(p):
    'EstructuraControl : IF LPAREN Expresion RPAREN LBRACE Sentencias RBRACE ELSE LBRACE Sentencias RBRACE'
    parser.parse_trace.append( ('EstructuraControl -> if-else (...)', '...') )

def p_EstructuraControl_while(p):
    'EstructuraControl : WHILE LPAREN Expresion RPAREN LBRACE Sentencias RBRACE'
    parser.parse_trace.append( ('EstructuraControl -> while (...)', '...') )

def p_SentenciaPrint(p):
    'SentenciaPrint : PRINT ID SEMICOLON'
    parser.parse_trace.append( ('SentenciaPrint -> print ID ;', f'id:{p[2]}') )

def p_Expresion(p):
    '''Expresion : Termino
                 | Expresion OP_SUMA Termino
                 | Expresion OP_REL Termino'''
    parser.parse_trace.append( ('Expresion', f'Detectada Expresion con {len(p)-1} parte(s)') )

def p_Termino(p):
    '''Termino : Factor
               | Termino OP_MUL Factor'''
    parser.parse_trace.append( ('Termino', f'Detectado Termino con {len(p)-1} parte(s)') )

def p_Factor(p):
    '''Factor : ID
              | NUM
              | LPAREN Expresion RPAREN'''
    parser.parse_trace.append( ('Factor', f'valor: {p[1]}') )

def p_error(p):
    if p:
        error_message = f"Error de Sintaxis: Token inesperado '{p.value}' (tipo: {p.type}) en línea {p.lineno}\n"
    else:
        error_message = "Error de Sintaxis: Fin de archivo inesperado\n"
    
    if not hasattr(parser, 'syntax_errors'):
        parser.syntax_errors = []
    parser.syntax_errors.append(error_message)

# Construir el parser
parser = yacc.yacc(errorlog=yacc.NullLogger())