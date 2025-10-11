
class Cliente:
    def __init__(self, nombre, edad, discapacidad, ticket):
        self.nombre = nombre
        self.edad = edad
        self.discapacidad = discapacidad
        self.tipo = self.definir_tipo()
        self.ticket = ticket 

    def definir_tipo(self):
        return "Prioritario" if self.edad >= 60 or self.discapacidad else "Normal"

    def __str__(self):
        return f"Ticket #{self.ticket} - {self.nombre} ({self.tipo})"

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, cliente):
        self.items.append(cliente)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        for cliente in self.items:
            print(f"  - {cliente}")

class SistemaBanco:
    def __init__(self):
        self.cola_prioritarios = Cola()
        self.cola_normales = Cola()
        self.secuencia_atendidos = []
        self.contador_tickets = 1  

    def registrar_cliente(self, nombre, edad, discapacidad):
        cliente = Cliente(nombre, edad, discapacidad, self.contador_tickets)
        self.contador_tickets += 1

        if cliente.tipo == "Prioritario":
            self.cola_prioritarios.encolar(cliente)
        else:
            self.cola_normales.encolar(cliente)

        print(f">> Cliente registrado: {cliente}")

    def atender_cliente(self):
        if not self.cola_prioritarios.esta_vacia():
            cliente = self.cola_prioritarios.desencolar()
        elif not self.cola_normales.esta_vacia():
            cliente = self.cola_normales.desencolar()
        else:
            cliente = None

        if cliente:
            self.secuencia_atendidos.append(cliente)
            print(f"✅ Atendiendo: {cliente}")
        else:
            print("⏳ No hay clientes en espera.")

    def mostrar_secuencia_final(self):
        print("\n>> Secuencia final de atención:")
        for i, cliente in enumerate(self.secuencia_atendidos, start=1):
            print(f"{i}. {cliente}")

if __name__ == "__main__":
    banco = SistemaBanco()

    clientes_simulados = [
       ("Mauricio", 35, False),    
    ("Alex", 42, False),        
    ("Arielote", 50, False),        
    ("Johansen", 28, False),     
    ("Emir", 45, False),         
    ("Iñaki", 72, False),       
    ("Patricio", 66, False),     
    ("Federico", 33, True),      
    ("Rodrigo", 61, False),      
    ("Santiago", 29, True)    

    ]

    for nombre, edad, discapacidad in clientes_simulados:
        banco.registrar_cliente(nombre, edad, discapacidad)

    print("\n🔔 Iniciando atención a clientes...\n")
    for _ in range(10):
        banco.atender_cliente()

    banco.mostrar_secuencia_final()