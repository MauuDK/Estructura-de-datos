
class BuscarPalindromo:
    def __init__(self, palabras):
        self.palabras = palabras

    def verificar_palindromo(self, palabra):
        palabra = palabra.lower()
        return palabra == palabra[::-1]

    def extraer_palindromo(self):
        palindromos = []
        for palabra in self.palabras:
            if self.verificar_palindromo(palabra):
                palindromos.append(palabra)
        return palindromos

    def imprimir_palindromos(self):
        palindromos = self.extraer_palindromo()
        if palindromos:
            print("\nLas Palabras palíndromas que se encontraron fueron:")
            for palabra in palindromos:
                print(f"--> {palabra}")
        else:
            print("\nNo se encontró ninguna palabra palíndroma")

def main():
    palabras = []
    print(" Ingresa una lista de palabras una por una (cuando quieras terminar escribe 'fin'):")

    while True:
        palabra = input("> ")
        if palabra.lower().strip() == "fin":
            break
        palabras.append(palabra.strip())

    detector = BuscarPalindromo(palabras)
    detector.imprimir_palindromos()

if __name__ == "__main__":
    main()
