import tkinter as tk

def on_button_click():

    print("¡Botón clicado!")

root = tk.Tk()

root.title("Mi Aplicación")

root.geometry("400x300")

label = tk.Label(root, text="¡Hola, Mundo!")

label.pack(pady=10)

button = tk.Button(root, text="Haz clic aquí", command=on_button_click)

button.pack(pady=20)

root.mainloop()

