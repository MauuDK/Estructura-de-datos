
import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib
import os

def calcular_hash(ruta_archivo):
    sha256 = hashlib.sha256()
    with open(ruta_archivo, "rb") as f:
        for bloque in iter(lambda: f.read(4096), b""):
            sha256.update(bloque)
    return sha256.hexdigest()

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    if not carpeta:
        return
    text_widget.delete("1.0", tk.END)

    archivos = os.listdir(carpeta)
    if not archivos:
        text_widget.insert(tk.END, "Carpeta vacía.\n")
        return

    text_widget.insert(tk.END, f"Carpeta seleccionada:\n{carpeta}\n\n")

    for archivo in archivos:
        ruta = os.path.join(carpeta, archivo)
        if os.path.isfile(ruta):
            hash_archivo = calcular_hash(ruta)
            text_widget.insert(tk.END, f"{archivo}\nHASH: {hash_archivo}\n\n")

root = tk.Tk()
root.title("HASH de Archivos")
root.geometry("700x500")

tk.Button(root, text="Seleccionar Carpeta", font=("Arial", 14),
          command=seleccionar_carpeta).pack(pady=10)

text_widget = tk.Text(root, height=20, width=80, font=("Consolas", 11))
text_widget.pack(pady=10)

root.mainloop()
