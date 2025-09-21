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


def reconstruct_path(parents, start, goal):
    """Reconstrói o caminho do final para o início."""
    path = [goal]
    while path[-1] != start:
        path.append(parents[path[-1]])
    path.reverse()
    return path


# --- Algoritmo de Busca em Profundidade (DFS) ---

def dfs(graph, start, goal):
    """Busca em Profundidade (Depth-First Search)"""
    if start not in graph or goal not in graph:
        return None

    stack = [start]
    visited = {start}
    parents = {start: None}

    while stack:
        current_node = stack.pop()

        if current_node == goal:
            return reconstruct_path(parents, start, goal)

        # Adiciona vizinhos à pilha em ordem reversa (para explorar em ordem alfabética)
        for neighbor in sorted(graph[current_node], reverse=True):
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current_node
                stack.append(neighbor)
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

    print(f"--- Executando Busca em Profundidade (DFS) de '{start_node}' para '{goal_node}' ---")

    path_dfs = dfs(graph, start_node, goal_node)

    if path_dfs:
        print(f"Caminho encontrado: {' -> '.join(path_dfs)}")
        print(f"Custo (nº de salas): {len(path_dfs)}")
    else:
        print("Caminho não encontrado.")