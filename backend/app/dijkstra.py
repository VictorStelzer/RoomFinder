import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    previous_nodes = {node: None for node in graph}

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    current = end
    while current:
        path.insert(0, current)
        current = previous_nodes[current]

    return path, distances[end] if distances[end] != float('inf') else None


def get_valid_points(graph):
    excluidos = {"corredor", "escada", "rampa", "hall"}
    return [node for node in graph if not any(x in node.lower() for x in excluidos)]


if __name__ == "__main__":
    from pprint import pprint
    from graph import campus_graph

    pontos_disponiveis = get_valid_points(campus_graph)
    print("Pontos disponíveis para seleção:")
    pprint(pontos_disponiveis)

    origem = "Entrada Frontal"
    destino = "Sala 305"

    caminho, distancia = dijkstra(campus_graph, origem, destino)

    print(f"\nMenor caminho de {origem} até {destino}:")
    print(" -> ".join(caminho))
    print(f"Distância total: {distancia}")
