
class Pila:
    def __init__(self, nombre):
        self.items = []
        self.nombre = nombre

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.esta_vacia() else None

    def peek(self):
        return self.items[-1] if not self.esta_vacia() else None

    def esta_vacia(self):
        return len(self.items) == 0

    def __str__(self):
        return f"{self.nombre}: {self.items}"


class TorreDeHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.origen = Pila("Origen")
        self.auxiliar = Pila("Auxiliar")
        self.destino = Pila("Destino")
        for disco in reversed(range(1, num_discos + 1)):
            self.origen.push(disco)

    def resolver(self):
        print("Estado inicial:")
        self.mostrar_estado()
        self._mover(self.num_discos, self.origen, self.destino, self.auxiliar)

    def _mover(self, n, origen, destino, auxiliar):
        if n == 1:
            disco = origen.pop()
            destino.push(disco)
            self.mostrar_movimiento(disco, origen, destino)
        else:
            self._mover(n - 1, origen, auxiliar, destino)
            self._mover(1, origen, destino, auxiliar)
            self._mover(n - 1, auxiliar, destino, origen)

    def mostrar_movimiento(self, disco, origen, destino):
        print(f"\nMover disco {disco} de {origen.nombre} a {destino.nombre}")
        self.mostrar_estado()

    def mostrar_estado(self):
        print(self.origen)
        print(self.auxiliar)
        print(self.destino)


if __name__ == "__main__":
    juego = TorreDeHanoi(num_discos=3)
    juego.resolver()