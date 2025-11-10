
class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def agregar_arista(self, u, v, peso):
        self.grafo.append([u, v, peso])

    def buscar(self, padre, i):
        if padre[i] == i:
            return i
        return self.buscar(padre, padre[i])

    def union(self, padre, rango, x, y):
        xraiz = self.buscar(padre, x)
        yraiz = self.buscar(padre, y)
        if rango[xraiz] < rango[yraiz]:
            padre[xraiz] = yraiz
        elif rango[xraiz] > rango[yraiz]:
            padre[yraiz] = xraiz
        else:
            padre[yraiz] = xraiz
            rango[xraiz] += 1

    def kruskal(self):
        resultado = []
        i = 0
        e = 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2])
        padre = []
        rango = []

        for nodo in range(self.V):
            padre.append(nodo)
            rango.append(0)

        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i += 1
            x = self.buscar(padre, u)
            y = self.buscar(padre, v)

            if x != y:
                e += 1
                resultado.append([u, v, w])
                self.union(padre, rango, x, y)

        print("Aristas del árbol de expansión mínima:")
        for u, v, peso in resultado:
            print(f"{u} -- {v} == {peso}")


g = Grafo(4)
g.agregar_arista(0, 1, 10)
g.agregar_arista(0, 2, 6)
g.agregar_arista(0, 3, 5)
g.agregar_arista(1, 3, 15)
g.agregar_arista(2, 3, 4)
g.kruskal()
