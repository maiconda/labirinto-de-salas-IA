import heapq

# --- Estrutura do Ambiente e Funções Auxiliares ---

# Grafo representando as conexões entre as salas
graph = {
    'A': ['C'], 'B': ['C', 'D'], 'C': ['A', 'B', 'G'], 'D': ['B', 'E'],
    'E': ['D', 'F'], 'F': ['E', 'J'], 'G': ['C', 'K', 'H'], 'H': ['G', 'K', 'I', 'L'],
    'I': ['H', 'J'], 'J': ['F', 'M', 'I'], 'K': ['G', 'N', 'H'], 'L': ['H', 'M'],
    'M': ['J', 'L', 'P'], 'N': ['K', 'O', 'Q'], 'O': ['N', 'P'], 'P': ['O', 'M', 'T'],
    'Q': ['N', 'R'], 'R': ['Q', 'S'], 'S': ['R', 'T'], 'T': ['S', 'P', 'U'],
    'U': ['T']
}

# Coordenadas (x, y) para cada sala para a heurística
coordinates = {
    'A': (0, 0), 'B': (0, 1), 'C': (1, 1), 'D': (0, 2), 'E': (0, 3), 'F': (0, 4),
    'G': (1, 0), 'H': (2, 1), 'I': (1, 2), 'J': (1, 3), 'K': (2, 0), 'L': (2, 2),
    'M': (2, 3), 'N': (3, 0), 'O': (3, 1), 'P': (3, 2), 'Q': (4, 0), 'R': (4, 1),
    'S': (4, 2), 'T': (4, 3), 'U': (4, 4)
}


def reconstruct_path(parents, start, goal):
    """Reconstrói o caminho do final para o início."""
    path = [goal]
    while path[-1] != start:
        path.append(parents[path[-1]])
    path.reverse()
    return path


def manhattan_distance(node, goal):
    """Calcula a Distância de Manhattan."""
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]
    return abs(x1 - x2) + abs(y1 - y2)


# --- Algoritmo de Busca A* ---

def a_star_search(graph, start, goal):
    """Busca A* (A-Star Search)"""
    if start not in graph or goal not in graph:
        return None

    # Fila de prioridade: (f_cost, g_cost, node)
    priority_queue = [(manhattan_distance(start, goal), 0, start)]
    g_costs = {node: float('inf') for node in graph}
    g_costs[start] = 0
    parents = {start: None}

    while priority_queue:
        _, g_cost, current_node = heapq.heappop(priority_queue)

        if current_node == goal:
            return reconstruct_path(parents, start, goal)

        for neighbor in sorted(graph[current_node]):
            new_g_cost = g_cost + 1  # Custo de cada passo é 1
            if new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                h_cost = manhattan_distance(neighbor, goal)
                f_cost = new_g_cost + h_cost
                parents[neighbor] = current_node
                heapq.heappush(priority_queue, (f_cost, new_g_cost, neighbor))
    return None  # Caminho não encontrado


# --- Execução Principal ---

if __name__ == "__main__":
    salas_validas = sorted(graph.keys())
    print("Salas disponíveis:", ", ".join(salas_validas))

    while True:
        start_node = input("Digite a sala inicial: ").upper()
        if start_node in salas_validas:
            break
        print(f"Erro: Sala '{start_node}' inválida. Tente novamente.")

    while True:
        goal_node = input("Digite a sala final: ").upper()
        if goal_node in salas_validas:
            break
        print(f"Erro: Sala '{goal_node}' inválida. Tente novamente.")

    print(f"--- Executando Busca A* de '{start_node}' para '{goal_node}' ---")

    path_a_star = a_star_search(graph, start_node, goal_node)

    if path_a_star:
        print(f"Caminho encontrado: {' -> '.join(path_a_star)}")
        print(f"Custo (nº de salas): {len(path_a_star)}")
    else:
        print("Caminho não encontrado.")