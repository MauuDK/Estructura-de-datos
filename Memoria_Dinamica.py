
class MemoriaDinamica:
    def __init__(self):
        self.frutas = []

    def ejecutar(self):
        self.frutas.append("Mango")
        self.frutas.append("Manzana")
        self.frutas.append("Banana")
        self.frutas.append("Uvas")

        print(self.frutas)

        self.frutas.pop(0)  
        
        self.frutas.pop(1)  

        self.frutas.append("Sandía")

        print(self.frutas)



programa = MemoriaDinamica()
programa.ejecutar()
