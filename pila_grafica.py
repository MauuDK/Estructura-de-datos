
import tkinter as tk
from tkinter import simpledialog
import time

class PilaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📦 Simulador de Pila")
        self.root.geometry("500x650")
        self.root.configure(bg="#f5f7fa")
        self.items = []

        tk.Label(root, text="Simulador de Pila", font=("Segoe UI", 20, "bold"),
                 bg="#f5f7fa", fg="#333").pack(pady=10)

        self.canvas = tk.Canvas(root, width=400, height=450, bg="#ffffff",
                                bd=0, highlightthickness=1, highlightbackground="#ccc")
        self.canvas.pack(pady=10)

        self.label_estado = tk.Label(root, text="", font=("Segoe UI", 12),
                                     bg="#f5f7fa", fg="#555")
        self.label_estado.pack()

        boton_frame = tk.Frame(root, bg="#f5f7fa")
        boton_frame.pack(pady=20)

        self.btn_apilar = tk.Button(boton_frame, text="🟩 Apilar", font=("Segoe UI", 11),
                                    bg="#d1e7dd", fg="#000", width=12, command=self.apilar)
        self.btn_apilar.grid(row=0, column=0, padx=10)

        self.btn_desapilar = tk.Button(boton_frame, text="🟥 Desapilar", font=("Segoe UI", 11),
                                       bg="#f8d7da", fg="#000", width=12, command=self.desapilar)
        self.btn_desapilar.grid(row=0, column=1, padx=10)

        self.btn_cima = tk.Button(boton_frame, text="🔍 Ver cima", font=("Segoe UI", 11),
                                  bg="#cfe2f3", fg="#000", width=12, command=self.ver_cima)
        self.btn_cima.grid(row=0, column=2, padx=10)

        self.dibujar_pila()

    def dibujar_pila(self):
        self.canvas.delete("all")
        altura = 60
        espacio = 10
        total_altura = len(self.items) * (altura + espacio)
        inicio_y = max(20, 450 - total_altura)

        for i, elemento in enumerate(reversed(self.items)):
            y = inicio_y + i * (altura + espacio)
            self.canvas.create_rectangle(80, y, 320, y + altura, fill="#b6d7a8", outline="#333", width=2)
            self.canvas.create_text(200, y + altura / 2, text=elemento, font=("Segoe UI", 14, "bold"), fill="#000")

        if self.items:
            self.canvas.create_text(200, inicio_y - 10, text=f"↑ Tope: {self.items[-1]}", font=("Segoe UI", 11), fill="#666")
        else:
            self.canvas.create_text(200, 20, text="⚠ Pila vacía", font=("Segoe UI", 11), fill="#666")

    def apilar(self):
        elemento = simpledialog.askstring("Apilar", "Ingresa el elemento:")
        if elemento:
            self.items.append(elemento)
            self.label_estado.config(text=f"✓ Apilado: {elemento}", fg="#198754")
            self.dibujar_pila()

    def desapilar(self):
        if self.items:
            elemento = self.items[-1]
            self.label_estado.config(text=f"✗ Desapilando: {elemento}", fg="#dc3545")
            self.root.update()
            time.sleep(0.5)
            self.items.pop()
            self.dibujar_pila()
        else:
            self.label_estado.config(text="⚠ La pila está vacía", fg="#dc3545")

    def ver_cima(self):
        if self.items:
            cima = self.items[-1]
            self.label_estado.config(text=f"🔝 Cima: {cima}", fg="#0d6efd")
        else:
            self.label_estado.config(text="⚠ Pila vacía", fg="#dc3545")

if __name__ == "__main__":
    root = tk.Tk()
    app = PilaGUI(root)
    root.mainloop()