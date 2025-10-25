import tkinter as tk
from math import *

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("PyCalculator")
        self.window.resizable(False, False)
        self.entry = tk.Entry(self.window, width=20, font=('Arial', 16), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipady=10)
        self.create_buttons()
        self.current_input = ""
        self.result = 0
        self.operation = None

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('√', 5, 1), ('x²', 5, 2), ('%', 5, 3)
        ]
        
        for (text, row, col) in buttons:
            btn = tk.Button(
                self.window,
                text=text,
                font=('Arial', 14),
                command=lambda t=text: self.button_click(t)
            )
            btn.grid(row=row, column=col, sticky='nsew', padx=2, pady=2, ipadx=10, ipady=10)

    def button_click(self, symbol):
        if symbol.isdigit() or symbol == '.':
            self.current_input += symbol
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.current_input)
        
        elif symbol in ['+', '-', '*', '/']:
            if self.current_input:
                self.result = float(self.current_input)
                self.operation = symbol
                self.current_input = ""
        
        elif symbol == '=':
            if self.operation and self.current_input:
                try:
                    if self.operation == '+':
                        self.result += float(self.current_input)
                    elif self.operation == '-':
                        self.result -= float(self.current_input)
                    elif self.operation == '*':
                        self.result *= float(self.current_input)
                    elif self.operation == '/':
                        self.result /= float(self.current_input)
                    
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, str(self.result))
                    self.current_input = ""
                    self.operation = None
                except ZeroDivisionError:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, "Ошибка")
        
        elif symbol == 'C':
            self.current_input = ""
            self.result = 0
            self.operation = None
            self.entry.delete(0, tk.END)
        
        elif symbol == '√':
            if self.current_input:
                try:
                    self.result = sqrt(float(self.current_input))
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, str(self.result))
                    self.current_input = ""
                except ValueError:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, "Ошибка")
        
        elif symbol == 'x²':
            if self.current_input:
                self.result = float(self.current_input) ** 2
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(self.result))
                self.current_input = ""
        
        elif symbol == '%':
            if self.current_input:
                try:
                    self.result = float(self.current_input) / 100
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, str(self.result))
                    self.current_input = ""
                except ValueError:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, "Ошибка")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()