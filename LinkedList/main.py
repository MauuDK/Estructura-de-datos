
from MyLinkedList import MyLinkedList


lista = MyLinkedList()


lista.agregar_al_inicio(30)
lista.agregar_al_final(50)
lista.insertar_en_posicion(40, 1)


print("Contenido actual:", lista.mostrar_lista())  


print("¿Está el 40?", lista.buscar_valor(40)) 
print("¿Está el 100?", lista.buscar_valor(100))  


print("Cantidad de elementos:", lista.contar_elementos()) 


lista.eliminar_por_valor(40)
print("Después de eliminar 40:", lista.mostrar_lista())  
