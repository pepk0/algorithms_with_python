# dfs implementation on a graph represented as a adjacency matrix
def dfs(node, graph, visited: set) -> None:
    if node in visited:
        return
    
    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)
    
    print(node, end=" ")


# graph represented with a adjacency matrix 
graph = {

    1: [19, 21, 14],
    19: [7, 12, 31, 21],
    21: [14],
    14: [23, 6],
    7: [1],
    12: [],
    31: [21],
    23: [21],
    6: []
}

# we loop trough every node in our graph so if there is any not connected 
# vertices we visit them too
visited = set()
for node in graph:
    if node not in visited:
        dfs(node, graph, visited)