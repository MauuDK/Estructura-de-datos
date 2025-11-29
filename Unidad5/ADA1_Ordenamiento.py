
def ordenamiento_burbuja(lista):
    print(f"\nEstado inicial: {lista}")
    arr = lista.copy()
    n = len(arr)
    
    for i in range(n):
        intercambio_hecho = False
       
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambio_hecho = True
        
        
        print(f"Pasada {i+1}: {arr}")
        
        if not intercambio_hecho:
            print("  -> ¡Lista ordenada prematuramente!")
            break
            
    return arr

def ordenamiento_insercion(lista):
    print(f"\nEstado inicial: {lista}")
    arr = lista.copy()
    
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        
        
        while j >= 0 and clave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = clave
        
        
        print(f"Insertando el {clave}: {arr}")
        
    return arr

def ordenamiento_seleccion(lista):
    print(f"\nEstado inicial: {lista}")
    arr = lista.copy()
    n = len(arr)
    
    for i in range(n):
        idx_minimo = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[idx_minimo]:
                idx_minimo = j
        
        
        arr[i], arr[idx_minimo] = arr[idx_minimo], arr[i]
        
        
        if i < n - 1:
            print(f"Posición {i} asegurada con el {arr[i]}: {arr}")
            
    return arr

def main():
    print("--- Visualizador de Ordenamiento ---")
    
    entrada = input("Ingresa los números separados por espacio (ej: 5 2 9 1): ")
    
    try:
        numeros = [int(x) for x in entrada.split()]
    except ValueError:
        print("Error: Ingresa solo números enteros.")
        return

    print("\nSelecciona el método:")
    print("1. Burbuja (Bubble Sort)")
    print("2. Inserción (Insertion Sort)")
    print("3. Selección (Selection Sort)")
    
    opcion = input("Opción (1/2/3): ")

    resultado = []
    
    print("-" * 30)
    if opcion == '1':
        resultado = ordenamiento_burbuja(numeros)
    elif opcion == '2':
        resultado = ordenamiento_insercion(numeros)
    elif opcion == '3':
        resultado = ordenamiento_seleccion(numeros)
    else:
        print("Opción no válida.")
        return
    print("-" * 30)

    print(f"\nResultado Final: {resultado}")

if __name__ == "__main__":
    main()
