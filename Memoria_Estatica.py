
import tkinter as tk
from tkinter import simpledialog, messagebox

class MemoriaEstatica:
    def __init__(self):
        self.calificaciones = [0] * 5  

    def capturar_calificaciones(self):
       
        root = tk.Tk()
        root.withdraw()

        for i in range(5):
            self.calificaciones[i] = int(
                simpledialog.askstring("Entrada de datos", f"Captura la calificación {i+1}:")
            )

    def mostrar_resultado(self):
        resultado = "Calificaciones capturadas:\n"
        for i in range(5):
            resultado += f"Calificación {i+1}: {self.calificaciones[i]}\n"
        messagebox.showinfo("Resultado", resultado)


if __name__ == "__main__":
    programa = MemoriaEstatica()
    programa.capturar_calificaciones()
    programa.mostrar_resultado()
