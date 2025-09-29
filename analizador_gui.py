# analizador_gui.py (Versión con tabla de traza sintáctica)

import tkinter as tk
from tkinter import scrolledtext, font

from lexer_ply import lexer
from parser_ply import parser

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico y Sintáctico")
        self.root.geometry("800x700") # Aumentamos un poco la altura
        default_font = font.Font(family="Consolas", size=12)
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        input_frame = tk.LabelFrame(main_frame, text="Código Fuente", padx=5, pady=5)
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
        self.input_text = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, font=default_font)
        self.input_text.pack(fill=tk.BOTH, expand=True)
        self.analyze_button = tk.Button(main_frame, text="Analizar Código", command=self.analizar_codigo, font=("Arial", 12, "bold"))
        self.analyze_button.pack(fill=tk.X, pady=5)
        output_frame = tk.LabelFrame(main_frame, text="Resultados del Análisis", padx=5, pady=5)
        output_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        self.output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, font=default_font, state='disabled', bg='#f0f0f0')
        self.output_text.pack(fill=tk.BOTH, expand=True)
        # Ajustamos las tabulaciones para las dos tablas
        self.output_text.config(tabs=(250, 450))

    def analizar_codigo(self):
        source_code = self.input_text.get("1.0", tk.END)
        
        # Reiniciar estado del lexer y parser para cada análisis
        lexer.lineno = 1
        lexer.lex_errors = []
        parser.syntax_errors = []
        parser.parse_trace = [] # Importante: inicializar la lista de traza

        # FASE LÉXICA
        tokens_encontrados = []
        lexer.input(source_code)
        while True:
            tok = lexer.token()
            if not tok:
                break
            tokens_encontrados.append(tok)

        # FASE SINTÁCTICA
        resultado_sintactico = parser.parse(source_code, lexer=lexer)
        
        # --- MOSTRAR RESULTADOS ---
        self.output_text.config(state='normal')
        self.output_text.delete("1.0", tk.END)

        # 1. ERRORES LÉXICOS (SI HAY)
        if lexer.lex_errors:
            self.output_text.insert(tk.END, "--- ERRORES LÉXICOS ---\n", 'error')
            for error in lexer.lex_errors: self.output_text.insert(tk.END, error)
            self.output_text.insert(tk.END, "\n")
        
        # 2. TABLA DE TOKENS
        self.output_text.insert(tk.END, "--- TABLA DE TOKENS ---\n", 'header')
        header = "LEXEMA\tTOKEN\t[Línea, Pos]\n"
        self.output_text.insert(tk.END, header, 'subheader')
        self.output_text.insert(tk.END, "="*60 + "\n")
        for token in tokens_encontrados:
            fila = f"{token.value}\t{token.type}\t[{token.lineno},{token.lexpos}]\n"
            self.output_text.insert(tk.END, fila)
        self.output_text.insert(tk.END, "\n")
        
        # 3. NUEVO: TABLA DE TRAZA SINTÁCTICA
        if parser.parse_trace and not parser.syntax_errors:
             self.output_text.insert(tk.END, "--- TRAZA DEL ANÁLISIS SINTÁCTICO ---\n", 'header')
             header = "REGLA APLICADA\tVALORES\n"
             self.output_text.insert(tk.END, header, 'subheader')
             self.output_text.insert(tk.END, "="*60 + "\n")
             for rule, values in parser.parse_trace:
                 fila = f"{rule}\t{values}\n"
                 self.output_text.insert(tk.END, fila)
             self.output_text.insert(tk.END, "\n")

        # 4. ERRORES SINTÁCTICOS O RESULTADO FINAL
        if parser.syntax_errors:
            self.output_text.insert(tk.END, "--- ERRORES SINTÁCTICOS ---\n", 'error')
            for error in parser.syntax_errors: self.output_text.insert(tk.END, error)
        elif resultado_sintactico and not lexer.lex_errors:
            self.output_text.insert(tk.END, "--- RESULTADO SINTÁCTICO ---\n", 'header')
            self.output_text.insert(tk.END, resultado_sintactico)
        
        self.output_text.tag_config('header', foreground='#00008B', font=("Arial", 11, "bold"))
        self.output_text.tag_config('subheader', foreground='#4F4F4F', font=("Consolas", 12, "bold"))
        self.output_text.tag_config('error', foreground='#DC143C', font=("Arial", 11, "bold"))
        
        self.output_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()