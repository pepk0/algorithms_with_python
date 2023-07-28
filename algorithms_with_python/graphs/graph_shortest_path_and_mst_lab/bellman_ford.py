class Edge:
    def __init__(self, parent, child, weight) -> None:
        self.parent = parent
        self.child = child
        self.weight = weight


def bellman_ford(nodes: int, edges: list, distance: dict) -> tuple:
    path = {}

    for _ in range(nodes - 1):
        for edge in edges:
            new_distance = distance[edge.parent] + edge.weight
            if new_distance < distance[edge.child]:
                distance[edge.child] = new_distance
                path[edge.child] = edge.parent

    for _ in range(nodes - 1):
        for edge in edges:
            new_distance = distance[edge.parent] + edge.weight
            if new_distance < distance[edge.child]:
                return -1, -1
            
    return distance[target_node], path


def get_result(nodes: int, edges: list, distance: dict, target: int) -> str:

    result = []
    cost, path = bellman_ford(nodes, edges, distance)
    if cost == -1:
        return "Negative Cycle Detected"
    
    node = target
    while node in path:
        result.insert(0, node)
        node = path[node]

    result.insert(0, start_node)
    
    return f"{' '.join(list(map(str, result)))}\n{cost}"


nodes = int(input())
number_edges = int(input())
edges = []
distance = {}

for _ in range(number_edges):
    parent, child, weight = [int(i) for i in input().split()]
    distance[parent] = float("inf")
    distance[child] = float("inf")

    edges.append(Edge(parent, child, weight))

start_node = int(input())
target_node = int(input())
distance[start_node] = 0

print(get_result(nodes, edges, distance, target_node))
