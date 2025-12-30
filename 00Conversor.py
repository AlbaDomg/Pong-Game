import tkinter as tk
from tkinter import ttk

def convertir():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        label_resultado.config(text=f"{celsius:.2f} °C")
    except ValueError:
        label_resultado.config(text="Entrada inválida")

ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("300x150")

# Widgets
label_celsius = ttk.Label(ventana, text="Fahrenheit:")
label_celsius.pack(pady=5)

entry_fahrenheit = ttk.Entry(ventana)
entry_fahrenheit.pack(pady=5)

boton_convertir = ttk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.pack(pady=10)

label_resultado = ttk.Label(ventana, text="Resultado:")
label_resultado.pack(pady=5)


def convertir2():
    try:
        celsius2 = float(entry_celsius2.get())
        fahrenheit2 = (celsius2 * 9/5) * 32
        label_resultado2.config(text=f"{fahrenheit2:.2f} °C")
    except ValueError:
        label_resultado2.config(text="Entrada inválida")

ventana2 = tk.Tk()
ventana2.title("Conversor de Temperatura")
ventana2.geometry("300x150")

# Widgets
label_fahrenheit2 = ttk.Label(ventana2, text="Celsius:")
label_fahrenheit2.pack(pady=5)

entry_celsius2 = ttk.Entry(ventana2)
entry_celsius2.pack(pady=5)

boton_convertir2 = ttk.Button(ventana2, text="Convertir", command=convertir)
boton_convertir2.pack(pady=10)

label_resultado2 = ttk.Label(ventana2, text="Resultado:")
label_resultado2.pack(pady=5)

ventana.mainloop()
ventana2.mainloop()
