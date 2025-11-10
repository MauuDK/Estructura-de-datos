

import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import math

class GrafoInteractivo:
    def __init__(self, master):
        self.master = master
        self.master.title("🗺️ Grafo Interactivo - Estados de México")
        self.master.geometry("1000x750")
        self.canvas = tk.Canvas(self.master, width=1000, height=700)
        self.canvas.pack()
        try:
            self.mapa = Image.open("mapa_mexico.png")
            self.mapa = self.mapa.resize((1000, 700))
            self.mapa_tk = ImageTk.PhotoImage(self.mapa)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.mapa_tk)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el mapa: {e}")
            return
        self.estados = {}
        self.aristas = []
        self.nodo_seleccionado = None
        self.modo = None
        self._crear_botones()
        self.canvas.bind("<Button-1>", self._click_canvas)

    def _crear_botones(self):
        frame = tk.Frame(self.master)
        frame.pack(pady=10)
        tk.Button(frame, text="Agregar Estado", bg="#8ae68a", command=self._modo_agregar_estado).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Agregar Conexión", bg="#a3c4f3", command=self._modo_agregar_arista).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Eliminar Todo", bg="#f08080", command=self._limpiar_todo).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Mostrar Relaciones", bg="#f2d17a", command=self._mostrar_relaciones).grid(row=0, column=3, padx=5)

    def _modo_agregar_estado(self):
        self.modo = "nodo"
        messagebox.showinfo("Modo activo", "🟢 Da clic en el mapa para agregar un estado.")

    def _modo_agregar_arista(self):
        self.modo = "arista"
        self.nodo_seleccionado = None
        messagebox.showinfo("Modo activo", "🔵 Da clic en dos estados para conectarlos y asignar un costo.")

    def _click_canvas(self, event):
        if self.modo == "nodo":
            nombre = simpledialog.askstring("Nuevo Estado", "Ingresa el nombre del estado:")
            if nombre:
                self.estados[nombre] = (event.x, event.y)
                self._dibujar_estado(nombre, event.x, event.y)
        elif self.modo == "arista":
            estado_clic = self._buscar_estado_cercano(event.x, event.y)
            if not estado_clic:
                messagebox.showwarning("Aviso", "Haz clic sobre un estado existente.")
                return
            if self.nodo_seleccionado is None:
                self.nodo_seleccionado = estado_clic
                self._resaltar_estado(estado_clic)
            else:
                destino = estado_clic
                if destino == self.nodo_seleccionado:
                    messagebox.showwarning("Aviso", "Selecciona un estado diferente.")
                    return
                costo = simpledialog.askinteger("Costo", f"Costo de traslado entre {self.nodo_seleccionado} y {destino}:")
                if costo is not None:
                    self.aristas.append((self.nodo_seleccionado, destino, costo))
                    self._dibujar_arista(self.nodo_seleccionado, destino, costo)
                self.nodo_seleccionado = None
                self.dibujar_grafo()

    def _dibujar_estado(self, nombre, x, y):
        self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightgreen", outline="black", width=2, tags="estado")
        self.canvas.create_text(x, y, text=nombre, font=("Arial", 10, "bold"))

    def _dibujar_arista(self, u, v, costo):
        x1, y1 = self.estados[u]
        x2, y2 = self.estados[v]
        self.canvas.create_line(x1, y1, x2, y2, width=2, fill="blue")
        xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
        self.canvas.create_text(xm, ym, text=str(costo), fill="black", font=("Arial", 10, "bold"))

    def _resaltar_estado(self, nombre):
        x, y = self.estados[nombre]
        self.canvas.create_oval(x-25, y-25, x+25, y+25, outline="red", width=3, tags="resaltado")

    def _buscar_estado_cercano(self, x, y):
        for nombre, (ex, ey) in self.estados.items():
            if math.hypot(ex - x, ey - y) < 25:
                return nombre
        return None

    def dibujar_grafo(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.mapa_tk)
        for (u, v, c) in self.aristas:
            self._dibujar_arista(u, v, c)
        for estado, (x, y) in self.estados.items():
            self._dibujar_estado(estado, x, y)

    def _mostrar_relaciones(self):
        if not self.aristas:
            messagebox.showinfo("Relaciones", "No hay conexiones aún.")
            return
        texto = "Relaciones:\n\n"
        for u, v, c in self.aristas:
            texto += f"{u} ↔ {v} | Costo: {c}\n"
        messagebox.showinfo("Relaciones", texto)

    def _limpiar_todo(self):
        if messagebox.askyesno("Confirmar", "¿Deseas eliminar todos los estados y conexiones?"):
            self.estados.clear()
            self.aristas.clear()
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.mapa_tk)
            messagebox.showinfo("Limpieza", "Grafo eliminado correctamente.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GrafoInteractivo(root)
    root.mainloop()
    
