
import numpy as np
import time
import pandas as pd


matriz1 = np.random.randint(0, 100, size=(6, 500))


df1 = pd.DataFrame(matriz1, 
                   index=[f"Materia{i+1}" for i in range(6)],
                   columns=[f"Alumno{j+1}" for j in range(500)])
print("\n MATRIZ 1: Materias × Alumnos")
print(df1)


inicio = time.time()
dato1 = matriz1[4][320]
fin = time.time()

print(f"\nDato buscado → Materia 5, Alumno 321: {dato1}")
print(f"⏱ Tiempo de acceso: {fin - inicio:.8f} segundos")