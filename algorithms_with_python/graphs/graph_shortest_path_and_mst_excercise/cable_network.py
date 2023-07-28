from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight) -> None:
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __repr__(self) -> str:
        return f"{self.first} - {self.second}"


def prim(graph: dict, visited: set, budget: int) -> int:
    prio_queue = PriorityQueue()
    result = 0

    for node in visited:
        for child in graph[node]:
            prio_queue.put(child)

    while not prio_queue.empty():
        min_edge = prio_queue.get()
        valid_edge = None

        if min_edge.first in visited and min_edge.second not in visited:
            valid_edge = min_edge.second
        elif min_edge.second in visited and min_edge.first not in visited:
            valid_edge = min_edge.first

        if valid_edge == None:
            continue

        visited.add(valid_edge)
        if budget < min_edge.weight:
            return result

        budget -= min_edge.weight
        result += min_edge.weight

        for child in graph[valid_edge]:
            prio_queue.put(child)

    return result


budget = int(input())
number_nodes = int(input())
number_edges = int(input())

visited = set()
graph = {}

for _ in range(number_edges):
    usr_input = list(input().split())
    if "connected" in usr_input:
        visited.add(int(usr_input[0]))
        visited.add(int(usr_input[1]))
        usr_input.remove("connected")

    first, second, weight = [int(i) for i in usr_input]
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []

    graph[first].append(Edge(first, second, weight))
    graph[second].append(Edge(second, first, weight))

print(f"Budget used: {prim(graph, visited, budget)}")
