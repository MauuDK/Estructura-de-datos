

import tkinter as tk
from tkinter import messagebox, simpledialog
from collections import deque


class Nodo:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def esVacio(self):
        return self.raiz is None

    
    def insertar(self, clave):
        if self.raiz is None:
            self.raiz = Nodo(clave)
            return True
        return self._insertar_rec(self.raiz, clave)

    def _insertar_rec(self, nodo, clave):
        if clave == nodo.clave:
            return False
        elif clave < nodo.clave:
            if nodo.izq is None:
                nodo.izq = Nodo(clave)
                return True
            return self._insertar_rec(nodo.izq, clave)
        else:
            if nodo.der is None:
                nodo.der = Nodo(clave)
                return True
            return self._insertar_rec(nodo.der, clave)

    
    def buscar(self, clave):
        return self._buscar_rec(self.raiz, clave)

    def _buscar_rec(self, nodo, clave):
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo
        elif clave < nodo.clave:
            return self._buscar_rec(nodo.izq, clave)
        else:
            return self._buscar_rec(nodo.der, clave)

    
    def preorden(self):
        res = []
        self._pre(self.raiz, res)
        return res

    def _pre(self, n, res):
        if n:
            res.append(n.clave)
            self._pre(n.izq, res)
            self._pre(n.der, res)

    
    def inorden(self):
        res = []
        self._in(self.raiz, res)
        return res

    def _in(self, n, res):
        if n:
            self._in(n.izq, res)
            res.append(n.clave)
            self._in(n.der, res)

    
    def postorden(self):
        res = []
        self._post(self.raiz, res)
        return res

    def _post(self, n, res):
        if n:
            self._post(n.izq, res)
            self._post(n.der, res)
            res.append(n.clave)

    
    def por_niveles(self):
        res = []
        if not self.raiz:
            return res
        q = deque([self.raiz])
        while q:
            n = q.popleft()
            res.append(n.clave)
            if n.izq: q.append(n.izq)
            if n.der: q.append(n.der)
        return res

    
    def altura(self):
        return self._alt(self.raiz)

    def _alt(self, n):
        if n is None:
            return -1
        return 1 + max(self._alt(n.izq), self._alt(n.der))

    
    def cantidad_hojas(self):
        return self._hojas(self.raiz)

    def _hojas(self, n):
        if n is None: return 0
        if n.izq is None and n.der is None: return 1
        return self._hojas(n.izq) + self._hojas(n.der)

    
    def cantidad_nodos(self):
        return self._nodos(self.raiz)

    def _nodos(self, n):
        if n is None: return 0
        return 1 + self._nodos(n.izq) + self._nodos(n.der)

    
    def es_lleno(self):
        return self._lleno(self.raiz)

    def _lleno(self, n):
        if n is None: return True
        if (n.izq is None) and (n.der is None): return True
        if n.izq and n.der:
            return self._lleno(n.izq) and self._lleno(n.der)
        return False

    
    def es_completo(self):
        if self.raiz is None: return True
        q = deque([self.raiz])
        flag = False
        while q:
            n = q.popleft()
            if n.izq:
                if flag: return False
                q.append(n.izq)
            else:
                flag = True
            if n.der:
                if flag: return False
                q.append(n.der)
            else:
                flag = True
        return True

    
    def eliminar(self, clave, modo='predecesor'):
        self.raiz, eliminado = self._eliminar_rec(self.raiz, clave, modo)
        return eliminado

    def _eliminar_rec(self, nodo, clave, modo):
        if nodo is None:
            return nodo, False
        if clave < nodo.clave:
            nodo.izq, eliminado = self._eliminar_rec(nodo.izq, clave, modo)
            return nodo, eliminado
        elif clave > nodo.clave:
            nodo.der, eliminado = self._eliminar_rec(nodo.der, clave, modo)
            return nodo, eliminado
        else:
            
            if nodo.izq is None and nodo.der is None:
                return None, True
            if nodo.izq is None:
                return nodo.der, True
            if nodo.der is None:
                return nodo.izq, True
           
            if modo == 'predecesor':
                pred = nodo.izq
                while pred.der: pred = pred.der
                nodo.clave = pred.clave
                nodo.izq, _ = self._eliminar_rec(nodo.izq, pred.clave, modo)
            else:
                succ = nodo.der
                while succ.izq: succ = succ.izq
                nodo.clave = succ.clave
                nodo.der, _ = self._eliminar_rec(nodo.der, succ.clave, modo)
            return nodo, True

   
    def eliminar_arbol(self):
        self.raiz = None


class Visualizador:
    NODE_R = 22
    VSEP = 90
    HSEP_MIN = 30

    
    FILL_LEAF = "#C9F7C9"
    FILL_INTERNAL = "#DDEEFF"
    BORDER = "#2E6FA7"
    HIGHLIGHT = "#FFD47D"
    PATH_COLOR = "#FFA07A"
    LINE_COLOR = "#9AA7B2"

    def __init__(self, arbol, canvas, root):
        self.arbol = arbol
        self.canvas = canvas
        self.root = root
        self.node_pos = {}   
        self.node_items = {} 

        
        self.canvas.bind("<Configure>", lambda e: self._request_redraw())

        self._redraw_pending = False

    def _request_redraw(self):
       
        if self._redraw_pending: return
        self._redraw_pending = True
        self.root.after(50, self._do_redraw)

    def _do_redraw(self):
        self._redraw_pending = False
        self.dibujar(rotated=False)

    def dibujar(self, rotated=False):
        
        self.canvas.delete("all")
        self.node_pos.clear()
        self.node_items.clear()
        if self.arbol.raiz is None:
            return

        w = max(400, self.canvas.winfo_width())
        h = max(300, self.canvas.winfo_height())

        if rotated:
            
            positions = {}
            index = [0]
            def dfs(n, depth=0):
                if not n: return
                dfs(n.izq, depth+1)
                y = 30 + index[0] * (self.NODE_R*2 + 18)
                x = 60 + depth * 120
                positions[n] = (x, y)
                index[0] += 1
                dfs(n.der, depth+1)
            dfs(self.arbol.raiz)
        else:
            
            positions = {}
            x_index = [0]
            def inorder(n, depth=0):
                if not n: return
                inorder(n.izq, depth+1)
                x = x_index[0]
                positions[n] = (x, depth)
                x_index[0] += 1
                inorder(n.der, depth+1)
            inorder(self.arbol.raiz)
            max_x = max((p[0] for p in positions.values()), default=0)
          
            total_w = max(1, max_x+1)
            hsep = max(self.HSEP_MIN, (w - 100) / total_w)
            positions2 = {}
            for n, (xi, depth) in positions.items():
                x = 50 + xi * hsep + (w - (50 + total_w*hsep)) / 2
                y = 30 + depth * self.VSEP
                positions2[n] = (x, y)
            positions = positions2

      
        for n, (x,y) in positions.items():
            if n.izq:
                x2,y2 = positions[n.izq]
                self.canvas.create_line(x, y, x2, y2, width=2, fill=self.LINE_COLOR)
            if n.der:
                x2,y2 = positions[n.der]
                self.canvas.create_line(x, y, x2, y2, width=2, fill=self.LINE_COLOR)

        
        for n, (x,y) in positions.items():
            if n.izq is None and n.der is None:
                fill = self.FILL_LEAF
            else:
                fill = self.FILL_INTERNAL
            oid = self.canvas.create_oval(x-self.NODE_R, y-self.NODE_R, x+self.NODE_R, y+self.NODE_R,
                                          fill=fill, outline=self.BORDER, width=2)
            tid = self.canvas.create_text(x, y, text=str(n.clave), font=("Helvetica", 10, "bold"))
            self.node_pos[n] = (x,y)
            self.node_items[n] = (oid, tid)
        self.canvas.update()

    
    def _color_node(self, nodo, fill=None, outline=None):
        if nodo not in self.node_items: return
        oid, tid = self.node_items[nodo]
        if fill is not None:
            self.canvas.itemconfig(oid, fill=fill)
        if outline is not None:
            self.canvas.itemconfig(oid, outline=outline)
        self.canvas.update()

    def resaltar_lista_step(self, nodos, color=None, outline=None, delay_ms=400):
       
        if color is None: color = self.HIGHLIGHT
        seq = list(nodos)
        i = 0
        def step():
            nonlocal i
            if i >= len(seq):
                return
            n = seq[i]
            
            self._color_node(n, fill=color, outline=outline or "#FF8C00")
            i += 1
            self.root.after(delay_ms, step)
        step()

    def resaltar_lista_instant(self, nodos, color=None, outline=None):
        color = color or self.HIGHLIGHT
        for n in nodos:
            self._color_node(n, fill=color, outline=outline or "#FF8C00")

    def buscar_nodo_por_valor(self, valor):
       
        return self.arbol.buscar(valor)

    def nodos_hojas(self):
        res = []
        def dfs(n):
            if not n: return
            if n.izq is None and n.der is None:
                res.append(n)
            else:
                dfs(n.izq); dfs(n.der)
        dfs(self.arbol.raiz)
        return res

    def todos_nodos(self):
        return list(self.node_items.keys())

    def camino_altura(self):
     
        best = []
        def dfs(n):
            if not n: return []
            left = dfs(n.izq)
            right = dfs(n.der)
            if len(left) >= len(right):
                return [n] + left
            else:
                return [n] + right
        return dfs(self.arbol.raiz)


class App:
    def __init__(self, root):
        self.root = root
        root.title("Árbol Binario - Visualizador (Completo)")
        root.geometry("1200x720")
        self.arbol = ArbolBinarioBusqueda()

        
        left = tk.Frame(root, width=320, bg="#f0f4f8")
        left.pack(side="left", fill="y")

        right = tk.Frame(root)
        right.pack(side="right", fill="both", expand=True)

        
        tk.Label(left, text="Árbol Binario Visual", bg="#f0f4f8",
                 font=("Helvetica", 14, "bold")).pack(pady=(12,6))

        tk.Label(left, text="Valor entero:", bg="#f0f4f8").pack(anchor="w", padx=10)
        self.entry = tk.Entry(left, font=("Helvetica", 12))
        self.entry.pack(padx=10, pady=(0,8), fill="x")

        tk.Label(left, text="Velocidad animación (ms):", bg="#f0f4f8").pack(anchor="w", padx=10)
        self.vel_scale = tk.Scale(left, from_=100, to=1200, orient="horizontal", length=260, bg="#f0f4f8")
        self.vel_scale.set(400)
        self.vel_scale.pack(padx=10, pady=(0,12))

       
        btn_frame = tk.Frame(left, bg="#f0f4f8")
        btn_frame.pack(padx=10, pady=4, fill="x")

        def btn(text, cmd, bg="#2E86AB"):
            b = tk.Button(btn_frame, text=text, command=cmd, bg=bg, fg="white",
                          font=("Helvetica", 10, "bold"))
            return b

        
        r = 0
        b = btn("[1] Insertar", self.cmd_insertar, bg="#2E86AB"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1
        b = btn("[4] Buscar", self.cmd_buscar, bg="#2EA86E"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1
        b = btn("[8] Eliminar (PREDECESOR)", lambda: self.cmd_eliminar('predecesor'), bg="#D9534F"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1
        b = btn("[9] Eliminar (SUCESOR)", lambda: self.cmd_eliminar('sucesor'), bg="#D9534F"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1
        b = btn("[17] Eliminar árbol", self.cmd_eliminar_arbol, bg="#8B1E3F"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1

       
        b = btn("[3] Graficar (raíz arriba)", lambda: self.cmd_graficar(rotated=False), bg="#5B8FB9"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1
        b = btn("[2] Mostrar acostado (raíz izquierda)", lambda: self.cmd_graficar(rotated=True), bg="#5B8FB9"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1

     
        b = btn("[5] Recorrer PreOrden", lambda: self.cmd_recorrido('pre'), bg="#6C5CE7"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1
        b = btn("[6] Recorrer InOrden", lambda: self.cmd_recorrido('in'), bg="#6C5CE7"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1
        b = btn("[7] Recorrer PostOrden", lambda: self.cmd_recorrido('post'), bg="#6C5CE7"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1
        b = btn("[10] Recorrer por niveles", self.cmd_recorrido_niveles, bg="#6C5CE7"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1

        
        b = btn("[11] Altura", self.cmd_altura, bg="#FAB857"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1
        b = btn("[12] Cantidad de hojas", self.cmd_hojas, bg="#4BB543"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1
        b = btn("[13] Cantidad de nodos", self.cmd_nodos, bg="#4BB543"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1

       
        b = btn("[15] ¿Es completo?", self.cmd_es_completo, bg="#8AAAE5"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1
        b = btn("[16] ¿Es lleno?", self.cmd_es_lleno, bg="#8AAAE5"); b.grid(row=r, column=0, sticky="we", pady=4); r+=1

      
        self.status_var = tk.StringVar(value="Árbol vacío")
        tk.Label(left, textvariable=self.status_var, bg="#f0f4f8", fg="#333").pack(padx=10, pady=(8,2))

    
        self.canvas = tk.Canvas(right, bg="white")
        self.canvas.pack(fill="both", expand=True)

        
        bottom = tk.Frame(root, bg="#f0f4f8", height=120)
        bottom.pack(side="bottom", fill="x")
        tk.Label(bottom, text="Salida / Recorridos:", bg="#f0f4f8").pack(anchor="w", padx=8)
        self.output = tk.Text(bottom, height=4)
        self.output.pack(fill="x", padx=8, pady=4)

       
        self.visual = Visualizador(self.arbol, self.canvas, root)

       
        self.visual.dibujar(rotated=False)

   
    def _leer_valor(self):
        s = self.entry.get().strip()
        if s == "":
            messagebox.showwarning("Aviso", "Introduce un valor entero en la caja de texto.")
            return None
        try:
            v = int(s)
            return v
        except:
            messagebox.showerror("Error", "Valor inválido. Introduce un entero.")
            return None

    def _vel_ms(self):
        return int(self.vel_scale.get())

   
    def cmd_insertar(self):
        v = self._leer_valor()
        if v is None: return
        ok = self.arbol.insertar(v)
        if not ok:
            messagebox.showinfo("Insertar", f"El valor {v} ya existe.")
        else:
            self.status_var.set(f"Insertado {v}")
        self.visual.dibujar(rotated=False)

    def cmd_buscar(self):
        v = self._leer_valor()
        if v is None: return
        nodo = self.arbol.buscar(v)
        if nodo:
            self.status_var.set(f"Encontrado: {v}")
            self.visual.dibujar(rotated=False)
            # resaltar nodo encontrado (instantáneo)
            self.visual.resaltar_lista_instant([nodo], color="#90EE90")
        else:
            messagebox.showinfo("Buscar", f"Elemento {v} no encontrado.")
            self.status_var.set(f"No encontrado: {v}")

    def cmd_eliminar(self, modo='predecesor'):
        v = self._leer_valor()
        if v is None: return
        eliminado = self.arbol.eliminar(v, modo=modo)
        if eliminado:
            messagebox.showinfo("Eliminar", f"Elemento {v} eliminado ({modo}).")
            self.status_var.set(f"Eliminado {v} ({modo})")
        else:
            messagebox.showinfo("Eliminar", f"Elemento {v} no existe.")
            self.status_var.set(f"No existe {v}")
        self.visual.dibujar(rotated=False)

    def cmd_eliminar_arbol(self):
        if messagebox.askyesno("Confirmar", "¿Eliminar todo el árbol?"):
            self.arbol.eliminar_arbol()
            self.status_var.set("Árbol eliminado")
            self.canvas.delete("all")

    def cmd_graficar(self, rotated=False):
        self.visual.dibujar(rotated=rotated)
        self.status_var.set("Grafico actualizado (rotated=%s)" % rotated)

    def cmd_recorrido(self, tipo):
        if tipo == 'pre':
            vals = self.arbol.preorden()
            title = "PreOrden"
        elif tipo == 'in':
            vals = self.arbol.inorden()
            title = "InOrden"
        else:
            vals = self.arbol.postorden()
            title = "PostOrden"
        self.output.delete("1.0", "end")
        self.output.insert("end", f"{title}: {vals}\n")
        self.status_var.set(f"{title} mostrado")
        if vals:
           
            nodos = [ self.arbol.buscar(v) for v in vals ]
          
            nodos = [n for n in nodos if n is not None]
            self.visual.dibujar(rotated=False)
            
            self.visual.resaltar_lista_step(nodos, color=self.visual.HIGHLIGHT, delay_ms=self._vel_ms())

    def cmd_recorrido_niveles(self):
        vals = self.arbol.por_niveles()
        self.output.delete("1.0", "end")
        self.output.insert("end", f"Por niveles: {vals}\n")
        self.status_var.set("Recorrido por niveles mostrado")
        if vals:
            nodos = [ self.arbol.buscar(v) for v in vals ]
            nodos = [n for n in nodos if n is not None]
            self.visual.dibujar(rotated=False)
            self.visual.resaltar_lista_step(nodos, color="#FFD47D", delay_ms=self._vel_ms())

    def cmd_altura(self):
        h = self.arbol.altura()
        self.output.delete("1.0", "end")
        self.output.insert("end", f"Altura (aristas): {h}\n")
        self.status_var.set(f"Altura = {h}")
        camino = self.visual.camino_altura()
        if camino:
            self.visual.dibujar(rotated=False)
            self.visual.resaltar_lista_step(camino, color=self.visual.PATH_COLOR, delay_ms=self._vel_ms())

    def cmd_hojas(self):
        c = self.arbol.cantidad_hojas()
        hojas = self.visual.nodos_hojas()
        self.output.delete("1.0", "end")
        self.output.insert("end", f"Hojas: {c}\n")
        self.status_var.set(f"Hojas = {c}")
        if hojas:
            self.visual.dibujar(rotated=False)
            self.visual.resaltar_lista_step(hojas, color=self.visual.FILL_LEAF, delay_ms=self._vel_ms())

    def cmd_nodos(self):
        c = self.arbol.cantidad_nodos()
        todos = self.visual.todos_nodos()
        self.output.delete("1.0", "end")
        self.output.insert("end", f"Nodos: {c}\n")
        self.status_var.set(f"Nodos = {c}")
        if todos:
            self.visual.dibujar(rotated=False)
            self.visual.resaltar_lista_instant(todos, color="#D2EEFF")

    def cmd_es_completo(self):
        ok = self.arbol.es_completo()
        self.output.delete("1.0", "end")
        self.output.insert("end", f"¿Es completo? {ok}\n")
        self.status_var.set(f"Es completo: {ok}")
        self.visual.dibujar(rotated=False)
        if ok:
            self.visual.resaltar_lista_instant(self.visual.todos_nodos(), color="#CDE7FF")

    def cmd_es_lleno(self):
        ok = self.arbol.es_lleno()
        self.output.delete("1.0", "end")
        self.output.insert("end", f"¿Es lleno? {ok}\n")
        self.status_var.set(f"Es lleno: {ok}")
        self.visual.dibujar(rotated=False)
        if ok:
            self.visual.resaltar_lista_instant(self.visual.todos_nodos(), color="#E6F8DD")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
