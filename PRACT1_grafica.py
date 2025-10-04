

import tkinter as tk
import time

class PilaGrafica:
    def __init__(self, capacidad=8):
        self.capacidad = capacidad
        self.elementos = []
        self.ventana = tk.Tk()
        self.ventana.title("Simulación de Pila")
        self.canvas = tk.Canvas(self.ventana, width=200, height=420, bg="white")
        self.canvas.pack()
        self.ventana.update()

    def insertar(self, valor):
        if len(self.elementos) < self.capacidad:
            self.elementos.append(valor)
            self.dibujar_pila(f"Insertado: {valor}")
        else:
            self.dibujar_pila(f"⚠️ Desbordamiento: {valor}")

    def eliminar(self, etiqueta):
        if self.elementos:
            eliminado = self.elementos.pop()
            self.dibujar_pila(f"Eliminado ({etiqueta}): {eliminado}")
        else:
            self.dibujar_pila(f"⚠️ Subdesbordamiento ({etiqueta})")

    def dibujar_pila(self, mensaje):
        self.canvas.delete("all")
        self.canvas.create_text(100, 20, text=mensaje, font=("Arial", 10), fill="black")
        for i, valor in enumerate(reversed(self.elementos)):
            y = 60 + i * 40
            self.canvas.create_rectangle(50, y, 150, y + 30, fill="lightblue")
            self.canvas.create_text(100, y + 15, text=valor, font=("Arial", 12))
        if self.elementos:
            y_tope = 60 - 25
            self.canvas.create_text(100, y_tope, text="TOPE ↓", font=("Arial", 10), fill="red")
        self.ventana.update()
        time.sleep(1.2)

pila = PilaGrafica()
pila.insertar("X")
pila.insertar("Y")
pila.eliminar("Z")
pila.eliminar("T")
pila.eliminar("U")
pila.insertar("V")
pila.insertar("W")
pila.eliminar("p")
pila.insertar("R")

pila.ventana.mainloop()