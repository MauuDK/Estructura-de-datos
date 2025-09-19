
import numpy as np
import time
import pandas as pd


matriz2 = np.random.randint(0, 100, size=(500, 6))

df2 = pd.DataFrame(matriz2, 
                   index=[f"Alumno{i+1}" for i in range(500)],
                   columns=[f"Materia{j+1}" for j in range(6)])
print("\n MATRIZ 2: Alumnos × Materias")
print(df2)


inicio = time.time()
dato2 = matriz2[320][4]
fin = time.time()

print(f"\n Dato buscado → Alumno 321, Materia 5: {dato2}")
print(f"Tiempo de acceso: {fin - inicio:.8f} segundos")