

class Nodo:
 
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class MyLinkedList:
   
    def __init__(self):
        self.inicio = None

    def agregar_al_final(self, valor):
        nuevo = Nodo(valor)
        if not self.inicio:
            self.inicio = nuevo
            return
        actual = self.inicio
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo

    def agregar_al_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.inicio
        self.inicio = nuevo

    def insertar_en_posicion(self, valor, posicion):
        if posicion == 0:
            self.agregar_al_inicio(valor)
            return
        nuevo = Nodo(valor)
        actual = self.inicio
        indice = 0
        while actual and indice < posicion - 1:
            actual = actual.siguiente
            indice += 1
        if not actual:
            raise IndexError("La posición no existe en la lista.")
        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    def eliminar_por_valor(self, valor):
        if not self.inicio:
            return
        if self.inicio.dato == valor:
            self.inicio = self.inicio.siguiente
            return
        actual = self.inicio
        while actual.siguiente:
            if actual.siguiente.dato == valor:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente

    def mostrar_lista(self):
        elementos = []
        actual = self.inicio
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    def buscar_valor(self, valor):
        actual = self.inicio
        while actual:
            if actual.dato == valor:
                return True
            actual = actual.siguiente
        return False

    def contar_elementos(self):
        cantidad = 0
        actual = self.inicio
        while actual:
            cantidad += 1
            actual = actual.siguiente
        return cantidad

