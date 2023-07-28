def dfs(node, graph, visited: set):
    
    if node in visited:
        return

    visited.add(node)

    for children in graph[node]:
        dfs(children, graph, visited)


buildings = int(input())
streets = int(input())

graph = {}
edges = []

for _ in range(streets):
    building, connection = input().split(" - ")
    if building not in graph:
        graph[building] = []
    if connection not in graph:
        graph[connection] = []
    
    if building in graph:
        graph[building].append(connection)
    if connection in graph:
        graph[connection].append(building)

    edges.append((building, connection))

print("Important streets:")
for first, second in edges:
    visited = set()
    
    graph[first].remove(second)
    graph[second].remove(first)
    
    dfs(first, graph, visited)
    if len(visited) < buildings:
        print(f"{min(first, second)} {max(first, second)}")
    
    graph[first].append(second)
    graph[second].append(first)
