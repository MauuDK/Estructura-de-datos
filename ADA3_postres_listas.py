import tkinter as tk
from tkinter import messagebox

class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class Postre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = None

class ListaPostres:
    def __init__(self):
        self.postres = []

    def buscar_postre(self, nombre):
        for postre in self.postres:
            if postre.nombre.lower() == nombre.lower():
                return postre
        return None

def alta_postre(lista, nombre, ingredientes):
    nuevo = Postre(nombre)
    cabeza = None
    for ing in reversed(ingredientes):
        nodo = NodoIngrediente(ing)
        nodo.siguiente = cabeza
        cabeza = nodo
    nuevo.ingredientes = cabeza
    lista.postres.append(nuevo)
    lista.postres.sort(key=lambda p: p.nombre.lower())
    return True

def baja_postre(lista, nombre):
    for i, p in enumerate(lista.postres):
        if p.nombre.lower() == nombre.lower():
            del lista.postres[i]
            return True
    return False

def insertar_ingrediente(postre, nombre_ingrediente):
    nuevo = NodoIngrediente(nombre_ingrediente)
    if not postre.ingredientes:
        postre.ingredientes = nuevo
    else:
        actual = postre.ingredientes
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

def eliminar_ingrediente(postre, nombre_ingrediente):
    actual = postre.ingredientes
    anterior = None
    while actual:
        if actual.nombre.lower() == nombre_ingrediente.lower():
            if anterior:
                anterior.siguiente = actual.siguiente
            else:
                postre.ingredientes = actual.siguiente
            return True
        anterior = actual
        actual = actual.siguiente
    return False

def obtener_ingredientes(postre):
    ingredientes = []
    actual = postre.ingredientes
    while actual:
        ingredientes.append(actual.nombre)
        actual = actual.siguiente
    return ingredientes

#subprograma
def eliminar_ingredientes_repetidos(lista_postres):
    for postre in lista_postres.postres:
        vistos = set()
        actual = postre.ingredientes
        anterior = None
        while actual:
            nombre = actual.nombre.lower().strip()
            if nombre in vistos:
                anterior.siguiente = actual.siguiente
                actual = actual.siguiente
            else:
                vistos.add(nombre)
                anterior = actual
                actual = actual.siguiente

postres = ListaPostres()

def dibujar_estructura():
    canvas.delete("all")
    x = 20
    y = 20
    canvas.create_text(x, y, text="POSTRES", anchor="nw", font=("Arial", 12, "bold"))
    y += 40
    for postre in postres.postres:
        canvas.create_rectangle(x, y, x+120, y+30, fill="#cce5ff")
        canvas.create_text(x+60, y+15, text=postre.nombre, font=("Arial", 10))
        canvas.create_line(x+120, y+15, x+150, y+15, arrow=tk.LAST)
        actual = postre.ingredientes
        x_ing = x + 150
        while actual:
            canvas.create_rectangle(x_ing, y, x_ing+100, y+30, fill="#d4edda")
            canvas.create_text(x_ing+50, y+15, text=actual.nombre, font=("Arial", 10))
            canvas.create_line(x_ing+100, y+15, x_ing+130, y+15, arrow=tk.LAST)
            x_ing += 130
            actual = actual.siguiente
        canvas.create_text(x_ing, y+15, text="NIL", font=("Arial", 10))
        y += 50

def actualizar_menu():
    menu_postres['menu'].delete(0, 'end')
    for nombre in [p.nombre for p in postres.postres]:
        menu_postres['menu'].add_command(label=nombre, command=tk._setit(var_postre, nombre))
    if postres.postres:
        var_postre.set(postres.postres[0].nombre)
    else:
        var_postre.set("")

def alta_postre_gui():
    nombre = entry_nuevo_postre.get().strip()
    ingredientes = entry_lista_ingredientes.get().strip().split(",")
    ingredientes = [i.strip() for i in ingredientes if i.strip()]
    if not nombre or not ingredientes:
        messagebox.showwarning("⚠️", "Completa nombre y lista de ingredientes.")
        return
    alta_postre(postres, nombre, ingredientes)
    entry_nuevo_postre.delete(0, tk.END)
    entry_lista_ingredientes.delete(0, tk.END)
    actualizar_menu()
    dibujar_estructura()

def baja_postre_gui():
    nombre = var_postre.get()
    if baja_postre(postres, nombre):
        actualizar_menu()
        dibujar_estructura()
        messagebox.showinfo("✅", f"Postre '{nombre}' eliminado.")
    else:
        messagebox.showwarning("⚠️", f"El postre '{nombre}' no existe.")

def agregar_ingrediente_gui():
    nombre = var_postre.get()
    ing = entry_ingrediente.get().strip()
    if not ing:
        messagebox.showwarning("⚠️", "Escribe un ingrediente.")
        return
    p = postres.buscar_postre(nombre)
    if p:
        insertar_ingrediente(p, ing)
        entry_ingrediente.delete(0, tk.END)
        dibujar_estructura()

def eliminar_ingrediente_gui():
    nombre = var_postre.get()
    ing = entry_ingrediente.get().strip()
    p = postres.buscar_postre(nombre)
    if p and eliminar_ingrediente(p, ing):
        entry_ingrediente.delete(0, tk.END)
        dibujar_estructura()
    else:
        messagebox.showinfo("Info", f"Ingrediente '{ing}' no encontrado.")

def imprimir_ingredientes_gui():
    nombre = var_postre.get()
    p = postres.buscar_postre(nombre)
    if p:
        ingredientes = obtener_ingredientes(p)
        messagebox.showinfo("Ingredientes", f"{nombre} lleva:\n" + "\n".join(ingredientes))
    else:
        messagebox.showwarning("⚠️", f"El postre '{nombre}' no existe.")

def eliminar_repetidos_gui():
    eliminar_ingredientes_repetidos(postres)
    dibujar_estructura()
    messagebox.showinfo("✅", "Ingredientes repetidos eliminados.")

root = tk.Tk()
root.title("🍰 Visualizador de POSTRES")
root.geometry("1100x650")

canvas = tk.Canvas(root, width=1050, height=300, bg="white", relief="sunken", bd=2)
canvas.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Selecciona un postre:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
var_postre = tk.StringVar()
menu_postres = tk.OptionMenu(frame, var_postre, "")
menu_postres.grid(row=0, column=1, sticky="w", padx=5)
actualizar_menu()

tk.Label(frame, text="Ingrediente:").grid(row=1, column=0, sticky="e", padx=5)
entry_ingrediente = tk.Entry(frame, width=30)
entry_ingrediente.grid(row=1, column=1, padx=5)
tk.Button(frame, text="Agregar ingrediente", command=agregar_ingrediente_gui).grid(row=1, column=2, padx=5)
tk.Button(frame, text="Eliminar ingrediente", command=eliminar_ingrediente_gui).grid(row=1, column=3, padx=5)
tk.Button(frame, text="Imprimir ingredientes", command=imprimir_ingredientes_gui).grid(row=1, column=4, padx=5)

tk.Label(frame, text="Nuevo postre:").grid(row=2, column=0, sticky="e", padx=5)
entry_nuevo_postre = tk.Entry(frame, width=30)
entry_nuevo_postre.grid(row=2, column=1, padx=5)
tk.Label(frame, text="Ingredientes (coma):").grid(row=2, column=2, sticky="e", padx=5)
entry_lista_ingredientes = tk.Entry(frame, width=30)
entry_lista_ingredientes.grid(row=2, column=3, padx=5)
tk.Button(frame, text="Alta postre", command=alta_postre_gui).grid(row=2, column=4, padx=5)

tk.Button(frame, text="Baja postre", command=baja_postre_gui, width=20).grid(row=3, column=1, pady=15)
tk.Button(frame, text="Eliminar ingredientes repetidos", command=eliminar_repetidos_gui, width=30).grid(row=3, column=2, columnspan=2, pady=15)

root.mainloop()
