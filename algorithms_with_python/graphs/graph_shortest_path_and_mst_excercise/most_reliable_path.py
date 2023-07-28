from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight) -> None:
        self.first = first
        self.second = second
        self.weight = weight
        
    def __repr__(self) -> str:
        return f"{self.second}"

def get_reliable_path(from_node, to_node, graph: dict, destination: dict):
    visited = set()
    path = {}
    prio_queue = PriorityQueue()
    prio_queue.put((-100, from_node))

    while not prio_queue.empty():
        cost, node = prio_queue.get()
        visited.add(node)

        if node == to_node:
            break
        
        if destination[node] < cost:
            continue
        
        for child in graph[node]:
            if child.second in visited:
                continue
        
            next_cost = -((child.weight / 100) * (cost / 100)) * 100
            prio_queue.put((next_cost, child.second))
            
            if destination[child.second] > next_cost:
                destination[child.second] = next_cost
                path[child.second] = node
        
    return get_result(from_node, to_node, path), destination[to_node]


def get_result(from_node, to_node, path: dict):
    result = []
    
    node = to_node
    while node in path:
        result.insert(0, node)
        node = path[node]

    result.insert(0, from_node)

    return result

number_nodes = int(input())
number_edges = int(input())
graph = {}
destination = {}

for _ in range(number_edges):
    first, second, weight = [int(i) for i in input().split()]
    edge = Edge(first, second, -weight)
    if first not in graph:
        graph[first] = []
        destination[first] = float("inf")
    if second not in graph:
        graph[second] = []
        destination[second] = float("inf")

    graph[first].append(Edge(first, second, -weight))
    graph[second].append(Edge(second, first, -weight))
    

from_node = int(input())
to_node = int(input())
destination[from_node] = -100

path, percent = get_reliable_path(from_node, to_node, graph, destination)

print(f"Most reliable path reliability: {abs(percent):.2f}%")
print(*path, sep=" -> ")