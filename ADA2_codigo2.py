
from collections import deque
import re

class cola_servicio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cola_servicio = deque()
        self.turno_actual = 1

    def llegada_cliente(self):
        ticket = f"{self.nombre}-{self.turno_actual}"
        self.cola_servicio.append(ticket)
        self.turno_actual += 1
        return ticket

    def atender_cliente(self):
        if self.cola_servicio:
            return self.cola_servicio.popleft()
        return None

servicios = {
    1: cola_servicio("MED"),
    2: cola_servicio("VIA"),
    3: cola_servicio("AUT"),
}

def procesar_entrada(texto):
    match = re.match(r'^([cCaA])\s?(\d+)$', texto.strip())
    if not match:
        print("Entrada incorrecta. Usa formato: C <servicio> o A <servicio>")
        return

    accion = match.group(1).upper()
    codigo = int(match.group(2))

    if codigo not in servicios:
        print(f"Servicio {codigo} no registrado.")
        return

    servicio = servicios[codigo]

    if accion == "C":
        ticket = servicio.llegada_cliente()
        print(f"Cliente registrado en '{servicio.nombre}'. Ticket: {ticket}")
    elif accion == "A":
        llamado = servicio.atender_cliente()
        if llamado:
            print(f"Atendiendo al cliente con ticket: {llamado}")
        else:
            print(f"No hay clientes en la cola_servicio de '{servicio.nombre}'")

if __name__ == "__main__":
    print("Sistema de atención - Seguros Merida")
    print("\nServicios: \n1=Seguro Médico \n2=Seguro De Viajes \n3=Seguro de Automóvil\n")
    print("Comandos: Utiliza 'C' o 'A' de la sig forma:\n \nC <num de servicio> (ej: C1) para llegada. \nA <num servicio> (ej: A1) para atención.")

    while True:
        entrada = input("-> ")
        if entrada.lower() in ["salir", "exit"]:
            print("Sistema finalizado.")
            break
        procesar_entrada(entrada)