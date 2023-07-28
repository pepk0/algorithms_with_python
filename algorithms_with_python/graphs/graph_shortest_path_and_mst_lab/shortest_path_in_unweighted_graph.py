def bfs(star_mode, end_node, visited: set, path: dict) -> dict | None:
    
    queue = []
    queue.append(start_node)
    visited.add(star_mode)

    while queue:
        node = queue.pop(0)
        
        for child in graph[node]:
            if child in visited:
                continue
        
            queue.append(child)
            visited.add(child)
            path[node] = child
        
            if child == end_node:
                return path


def shortest_path(path: dict, start_node: str) -> tuple:
    result = [start_node]
    node = start_node
    length = 0
    
    while node in path:
        result.append(path[node])
        node = path[node]
        length += 1

    return length, result


nodes = int(input())
edges = int(input())

graph = {}
for _ in range(edges):
    parent, child = input().split()
    if parent not in graph:
        graph[parent] = [child]
    else:
        graph[parent].append(child)
    
    if child not in graph:
        graph[child] = []

start_node = input()
end_node = input()

visited = set()
path = {}
bfs(start_node, end_node, visited, path)
length, result = shortest_path(path, start_node)

print(f"Shortest path length is: {length}")
print(*result, sep=" ")
