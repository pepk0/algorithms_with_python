from queue import PriorityQueue as prio_queue


class Edge:
    def __init__(self, source, destination, cost) -> None:
        self.source = source
        self.destination = destination
        self.cost = cost

    def __repr__(self) -> str:
        return f"{self.destination}"


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
            if child.destination in visited:
                continue
            
            next_cost = cost + child.cost 
            queue.put((next_cost, child.destination))
            
            if distance[child.destination] > next_cost:
                distance[child.destination] = next_cost
                path[child.destination] = node

    return distance[end_node], path


def shortest_path(start_node, end_node, graph: dict, distance) -> tuple:  
    result = []
    cost, path = dijkstra(start_node, end_node, graph, distance)

    node = end_node
    while node in path:
        result.insert(0, node)
        node = path[node]

    result.insert(0, start_node)

    return " - ".join(result), cost


number_roads = int(input())
graph = {}
distance = {}

for _ in range(number_roads):
    source, destination, cost = [s for s in input().split(" - ")]
    cost = int(cost)

    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []

    graph[source].append(Edge(source, destination, cost))
    graph[destination].append(Edge(destination, source, cost))

    if source not in distance:
        distance[source] = float("inf")
    if destination not in distance:
        distance[destination] = float("inf")

closed_road = input().split(",")
start_node = input()
end_node = input()

for road in closed_road:
    source, destination = road.split("-")
    for node in graph[source]:
        if node.destination == destination:
            graph[source].remove(node)
    
    for node in graph[destination]:
        if node.source == source:
            graph[destination].remove(node)

path, cost = shortest_path(start_node, end_node, graph, distance)
print(path)
print(cost)
