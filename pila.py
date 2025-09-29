
class Pila:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def apilar(self, elemento):
        self.elementos.append(elemento)
        print(f"Elemento '{elemento}' apilado.")

    def desapilar(self):
        if self.esta_vacia():
            print("Error: la pila está vacía.")
            return None
        return self.elementos.pop()

    def ver_tope(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return None
        return self.elementos[-1]

    def mostrar(self):
        print("Elementos de la pila (de abajo hacia arriba):")
        for i, elemento in enumerate(self.elementos):
            print(f"[{i}] → {elemento}")

if __name__ == "__main__":
    pila1 = Pila()
    pila1.apilar("1")
    pila1.apilar("2")
    pila1.apilar("3")
    pila1.apilar("4")
    pila1.mostrar()

    print("Tope actual:", pila1.ver_tope())
    print("Desapilando:", pila1.desapilar())
    
    print("Tope actual:", pila1.ver_tope())
    
    pila1.mostrar()