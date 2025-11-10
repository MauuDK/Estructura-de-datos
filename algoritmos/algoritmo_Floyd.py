
def floyd(grafo):
    n = len(grafo)
    dist = [fila[:] for fila in grafo]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


INF = float('inf')
grafo = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]

resultado = floyd(grafo)
for fila in resultado:
    print(fila)
