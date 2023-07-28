def dfs(node, graph, visited: set, components: list):    
    if node in visited:
        return
    
    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, components)

    components.append(str(node))
    

visited = set()
graph = {}
num = int(input())
for index in range(num):
    edge = [int(x) for x in input().split()]
    graph[index] = edge

for node in graph:
    if node not in visited:
        components = []
        dfs(node, graph, visited, components)
        print(f"Connected component: {' '.join(components)}")