# bfs implementation on a graph represented as a adjacency matrix
def bfs(node, graph, visited: set) -> None:
    if node in visited:
        return

    queue = [node]
    visited.add(node)

    while queue:
        curr_node = queue.pop(0)
        print(curr_node, end=" ")
        
        for child in graph[curr_node]:
            if child not in visited:
                queue.append(child)
                visited.add(child)


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
# we loop trough every node in the graph, se we can search for 
# vertices that are not connected
visited = set()
for node in graph:
    if node not in visited:
        bfs(node, graph, visited)