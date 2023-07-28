from queue import PriorityQueue as prio_queue

class Edge():
    def __init__(self, from_node, to_node, weight) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    
    # used to see if graph edges are added correctly
    def __repr__(self) -> str:
        return f"{self.to_node}"


def dijkstra(start_node, end_node, graph: dict, distance) -> tuple:
    path = {}
    visited = set()
    queue = prio_queue()

    queue.put((0, start_node))

    while not queue.empty():
        cost, node = queue.get()
        visited.add(node)
        
        if node == end_node:
            break
        if distance[node] < cost:
            continue
        
        for child in graph[node]:
            if child.to_node in visited:
                continue
            
            next_cost = cost + child.weight 
            queue.put((next_cost, child.to_node))
            
            if distance[child.to_node] > next_cost:
                distance[child.to_node] = next_cost
                path[child.to_node] = node
    
    return distance[end_node], path


def shortest_path(start_node, end_node, graph: dict, distance) -> str:  
    result = []
    cost, path = dijkstra(start_node, end_node, graph, distance)

    if cost == float("inf"):
        return "There is no such path."

    node = end_node
    while node in path:
        result.insert(0, node)
        node = path[node]

    result.insert(0, start_node)

    return f"{cost} \n{' '.join(list(map(str, result)))}"


edges = int(input())
graph = {}
distance = {}

for _ in range(edges):
    from_node, to_node, weight = [int(i) for i in input().split(", ")]
    if from_node not in graph:
        graph[from_node] = []
    if to_node not in graph:
        graph[to_node] = []

    graph[from_node].append(Edge(from_node, to_node, weight))
    
    if from_node not in distance:
        distance[from_node] = float("inf")
    if to_node not in distance:
        distance[to_node] = float("inf")


start_node = int(input())
end_node = int(input())
distance[start_node] = 0

print(shortest_path(start_node, end_node, graph, distance))