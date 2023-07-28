def dfs(source, destination,  graph, visited):

    if source in visited:
        return
    
    visited.add(source)
    
    if source == destination:
        return
    

    for child in graph[source]:
        dfs(child, destination, graph, visited)


def cycle_edge(source, destination, graph):
    visited = set()

    dfs(source, destination, graph, visited)

    return destination in visited


results = []
edges = []
graph = {}

nodes = int(input())
for _ in range(nodes):

    parent, children = input().split(" -> ")
    children = children.split()
    graph[parent] = children
    for child in children:
        edges.append((parent, child))

for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue
    
    graph[source].remove(destination)
    graph[destination].remove(source)
    if cycle_edge(source, destination, graph):
        results.append(f"{source} - {destination}")        
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f"Edges to remove: {len(results)}")
for result in results:
    print(result)