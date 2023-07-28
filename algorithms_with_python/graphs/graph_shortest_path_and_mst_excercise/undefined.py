class Edge:
    def __init__(self, first, second, weight) -> None:
        self.first = first
        self.second = second
        self.weight = weight

    def __repr__(self) -> str:
        return f"{self.first} - {self.second}"


def bellman_ford(edges: list, cost: dict, source: int, 
                 destination: int) -> tuple:
    nodes = len(cost)
    path = {}

    for _ in range(nodes - 1):
        for edge in edges:
            new_cost = cost[edge.first] + edge.weight
            if cost[edge.second] > new_cost:
                cost[edge.second] = new_cost
                path[edge.second] = edge.first

    for _ in range(nodes - 1):
        for edge in edges:
            new_cost = cost[edge.first] + edge.weight
            if cost[edge.second] > new_cost:
                return -1, -1
    
    return get_path(source, destination, path, cost)

def get_path(source: int, destination: int, path: dict, cost: dict) -> tuple:
    result = []
    
    node = destination
    while node in path:
        result.insert(0, node)
        node = path[node]
    
    result.insert(0, source)

    return result, cost[destination]

number_nodes = int(input())
number_edges = int(input())
edges = []
cost = {}

for _ in range(number_edges):
    first, second, weight = [int(i) for i in input().split()]
    edges.append(Edge(first, second, weight))
    
    if first not in cost:
        cost[first] = float("inf")
    if second not in cost:
        cost[second] = float("inf")

source = int(input())
destination = int(input())
cost[source] = 0

path, cost = bellman_ford(edges, cost, source, destination)

if path == -1:
    print("Undefined")
else:
    print(*path, sep=" ")
    print(cost)