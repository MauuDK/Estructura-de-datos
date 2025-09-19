
class Ventas_Men:
    def __init__(self):
        self.ventas = [[0.0 for _ in range(3)] for _ in range(12)]

    def insertar_venta(self, mes, dpto, monto_m):
        if 0 <= mes < 12 and 0 <= dpto < 3:
            self.ventas[mes][dpto] = monto_m
        else:
            print(" El Mes o departamento esta fuera de rango.")

    def buscar_venta(self, mes, dpto):
        if 0 <= mes < 12 and 0 <= dpto < 3:
            return self.ventas[mes][dpto]
        else:
            print("Consulta inválida, consulta dentro del rango de la matriz.")
            return None

    def eliminar_venta(self, mes, dpto):
        if 0 <= mes < 12 and 0 <= dpto < 3:
            self.ventas[mes][dpto] = 0.0
        else:
            print(" No se puede eliminar, ya que el índice esta fuera de rango.")

    def mostrar_ventas(self):
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        dptos = ["Ropa", "Deportes", "Juguetería"]

        print(f"{'Mes':12} | {dptos[0]:10} | {dptos[1]:10} | {dptos[2]:12}")
        print("-" * 53)

        for i, fila in enumerate(self.ventas):
            print(f"{meses[i]:12} |", end="")
            for monto_m in fila:
                print(f" ${monto_m:<9.2f} |", end="")
            print()


 #//#AQUI HAGO LAS PRUEBAS DE QUE FUNCIONAN LOS MÉTODOS, LAS PONGO PARA QUE SE VEA Q FUNCIONAN LOS METODOS
if __name__ == "__main__":
    ventas = Ventas_Men()

   
    ventas.insertar_venta(0, 0, 30000.0)  
    ventas.insertar_venta(1, 2, 90500.0)  
    ventas.insertar_venta(11, 1, 23000.0) 


    print("Ventas Mensuales:")
    ventas.mostrar_ventas()

   
    monto_m = ventas.buscar_venta(1, 2)
    print(f"\nConsulta: Febrero - Juguetería: ${monto_m:.2f}")

    
    ventas.eliminar_venta(1, 2)
    print("\nVentas después de eliminar:")
    ventas.mostrar_ventas()