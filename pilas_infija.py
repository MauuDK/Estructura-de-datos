
import re

class ConvertidorJerarquico:
    def __init__(self, expresion):
        self.expresion = expresion.replace(" ", "")
        self.operadores = "+-*/^"
        self.prioridad = {'+':1, '-':1, '*':2, '/':2, '^':3}

    def tokenizar(self, expresion):
        return re.findall(r'\d+|\w+|[()+\-*/^]', expresion)

    def es_operando(self, token):
        return token.isalnum()

    def convertir(self, expresion):
        tokens = self.tokenizar(expresion)
        salida, pila = [], []
        for token in tokens:
            if self.es_operando(token):
                salida.append(token)
            elif token == '(':
                pila.append(token)
            elif token == ')':
                while pila and pila[-1] != '(':
                    salida.append(pila.pop())
                pila.pop()
            elif token in self.operadores:
                while pila and pila[-1] != '(' and (
                    self.prioridad[token] <= self.prioridad.get(pila[-1],0) and token != '^'
                ):
                    salida.append(pila.pop())
                pila.append(token)
        while pila:
            salida.append(pila.pop())
        return salida

    def a_posfija(self):
        return self.convertir(self.expresion)

    def a_prefija(self):
        tokens = self.tokenizar(self.expresion)
        invertida = []
        for token in reversed(tokens):
            if token == '(':
                invertida.append(')')
            elif token == ')':
                invertida.append('(')
            else:
                invertida.append(token)
        return list(reversed(self.convertir(' '.join(invertida))))

    def estilo_pila(self, tokens, modo):
        pila = []
        secuencia = tokens if modo=="posfija" else reversed(tokens)
        for t in secuencia:
            if self.es_operando(t):
                pila.append(t)
            else:
                a, b = pila.pop(), pila.pop()
                pila.append(f"{b} {a}{t}" if modo=="posfija" else f"{t}{a} {b}")
        return pila[0]

    def mostrar(self):
        posfija = self.a_posfija()
        prefija = self.a_prefija()
        print("Expresión original:", self.expresion)
        print("Posfija estilo pila:", self.estilo_pila(posfija, "posfija"))
        print("Prefija estilo pila:", self.estilo_pila(prefija, "prefija"))

if __name__ == "__main__":
    entrada = input("Ingresa una expresión infija: ")
    ConvertidorJerarquico(entrada).mostrar()
