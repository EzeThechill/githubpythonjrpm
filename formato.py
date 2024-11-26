import tkinter as tk
from tkinter import ttk

class CustomMenuApp(tk.Tk):
    def __init__(self, options):
        super().__init__()
        self.title("Menú Personalizable")
        self.geometry("300x200")
        self.options = options
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Selecciona una opción:")
        label.pack(pady=10)

        self.option_var = tk.StringVar(self)
        self.option_var.set(self.options[0])  # Valor por defecto

        option_menu = ttk.OptionMenu(self, self.option_var, *self.options)
        option_menu.pack(pady=10)

        button = ttk.Button(self, text="Mostrar Opción Seleccionada", command=self.show_selection)
        button.pack(pady=10)

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)

    def show_selection(self):
        selected_option = self.option_var.get()
        self.result_label.config(text=f"Opción seleccionada: {selected_option}")

if __name__ == "__main__":
    opciones = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]
    app = CustomMenuApp(opciones)
    app.mainloop()