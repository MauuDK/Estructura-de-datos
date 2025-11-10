
def warshall(grafo):
    n = len(grafo)
    alcan = [fila[:] for fila in grafo]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                alcan[i][j] = alcan[i][j] or (alcan[i][k] and alcan[k][j])
    return alcan

grafo = [
    [1, 1, 0],
    [0, 1, 1],
    [0, 0, 1]
]

resultado = warshall(grafo)
for fila in resultado:
    print(fila)
