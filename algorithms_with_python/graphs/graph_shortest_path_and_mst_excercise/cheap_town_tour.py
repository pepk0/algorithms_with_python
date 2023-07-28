from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight) -> None:
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other) -> int:
        return self.weight > other.weight

    def __repr__(self) -> str:
        return f"{self.second}"


def get_result(node: int, graph: dict) -> str:
    visited = set()
    result = 0
    prio_queue = PriorityQueue()
    visited.add(node)

    for child in graph[node]:
        prio_queue.put(child)

    while not prio_queue.empty():
        min_node = prio_queue.get()
        valid_edge = None
        
        if min_node.first in visited and min_node.second not in visited:
            valid_edge = min_node.second
        elif min_node.second in visited and min_node.first not in visited:
            valid_edge = min_node.first
        
        if valid_edge == None:
            continue

        visited.add(valid_edge)
        result += min_node.weight

        for child in graph[valid_edge]:
            prio_queue.put(child)

    return f"Total cost: {result}"

number_towns = int(input())
number_streets = int(input())
graph = {}
node = 0

for _ in range(number_streets):
    first, second, weight = [int(i) for i in input().split(" - ")]
    if first not in graph:
        graph[first] = []
        node = first
    if second not in graph:
        graph[second] = []

    graph[first].append(Edge(first, second, weight))
    graph[second].append(Edge(second, first, weight))

print(get_result(node, graph))