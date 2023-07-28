# solution to connected components using BFS instead of DFS
def bfs(node, graph, visited: set, components: list):
    if node in visited:
        return
    
    queue = [node]
    visited.add(node)

    while queue:
        curr_node = queue.pop(0)
        components.append(str(curr_node))

        for child in graph[curr_node]:
            if child not in visited:
                queue.append(child)
                visited.add(child)
    
    return components


visited = set()
graph = {}
num = int(input())
for index in range(num):
    edge = [int(x) for x in input().split()]
    graph[index] = edge

for node in graph:
    if node not in visited:
        components = []
        bfs(node, graph, visited, components)
        print(f"Connected component: {' '.join(components)}")