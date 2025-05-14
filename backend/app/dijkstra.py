# dijkstra.py
import heapq

def get_valid_points(graph):
    return list(graph.keys())

def dijkstra(grafo, inicio, destino):
    fila = [(0, inicio, [])]
    visitados = set()

    while fila:
        distancia_atual, no_atual, caminho = heapq.heappop(fila)

        if no_atual in visitados:
            continue
        visitados.add(no_atual)

        if no_atual == destino:
            return caminho + [(no_atual, None, 0)], distancia_atual

        for vizinho, dados in grafo.get(no_atual, {}).items():
            if vizinho not in visitados:
                nova_distancia = distancia_atual + dados["distancia"]
                nova_rota = caminho + [(no_atual, dados["direcao"], dados["distancia"])]
                heapq.heappush(fila, (nova_distancia, vizinho, nova_rota))

    return None, float("inf")