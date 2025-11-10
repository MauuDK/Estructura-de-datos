

import heapq

def dijkstra(grafo, inicio):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[inicio] = 0
    cola = [(0, inicio)]

    while cola:
        distancia, actual = heapq.heappop(cola)
        if distancia > dist[actual]:
            continue

        for vecino, peso in grafo[actual]:
            nueva_dist = distancia + peso
            if nueva_dist < dist[vecino]:
                dist[vecino] = nueva_dist
                heapq.heappush(cola, (nueva_dist, vecino))
    return dist


grafo = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('E', 3)],
    'D': [],
    'E': [('D', 4)]
}

print("Distancias más cortas desde A:", dijkstra(grafo, 'A'))

