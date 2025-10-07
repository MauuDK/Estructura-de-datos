from collections import deque

class MiCola:
    def __init__(self):
        self.datos = deque()

    def encolar(self, valor):
        self.datos.append(valor)

    def desencolar(self):
        return self.datos.popleft() if self.datos else None

    def vacia(self):
        return not self.datos

    def longitud(self):
        return len(self.datos)

    def mostrar(self):
        return list(self.datos)

def fusionar_colas(c1, c2):
    resultado = MiCola()
    while not c1.vacia() and not c2.vacia():
        suma = c1.desencolar() + c2.desencolar()
        resultado.encolar(suma)
    return resultado


if __name__ == "__main__":
    entrada_a = MiCola()
    entrada_b = MiCola()

    datos_a = [3, 4, 2, 8, 12]
    datos_b = [6, 2, 9, 11, 3]

    for x in datos_a:
        entrada_a.encolar(x)
    for y in datos_b:
        entrada_b.encolar(y)

    resultado_final = fusionar_colas(entrada_a, entrada_b)
    print("Resultado de la suma:", resultado_final.mostrar())