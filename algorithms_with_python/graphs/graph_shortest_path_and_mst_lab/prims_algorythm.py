from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight) -> None:
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other) -> bool:
        return self.weight > other.weight

    def __repr__(self) -> str:
        return f"{self.first} - {self.second}"


def prim(node: int, graph: dict, visited: set) -> list:
    result = []
    visited.add(node)

    prio_queue = PriorityQueue()
    for edge in graph[node]:
        prio_queue.put(edge)

    while not prio_queue.empty():
        min_edge = prio_queue.get()
        tree_node = -1

        if min_edge.first in visited and min_edge.second not in visited:
            tree_node = min_edge.second
        elif min_edge.second in visited and min_edge.first not in visited:
            tree_node = min_edge.first

        if tree_node == -1:
            continue

        visited.add(tree_node)
        result.append(min_edge)

        for edge in graph[tree_node]:
            prio_queue.put(edge)

    return result

edges = int(input())
graph = {}
for _ in range(edges):
    first, second, weight = [int(i) for i in input().split(", ")]
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []

    edge = Edge(first, second, weight)

    graph[first].append(edge)
    graph[second].append(edge)

visited = set()

for node in graph:
    if node in visited:
        continue
    print(*prim(node, graph, visited), sep="\n")