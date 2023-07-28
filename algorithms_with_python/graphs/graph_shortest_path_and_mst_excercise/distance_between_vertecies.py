def find_path(from_node: str, to_node: str, graph: dict) -> int:
    visited = set()
    parent = {}

    queue = [from_node]
    visited.add(from_node)

    while queue:
        
        node = queue.pop(0)
        if node == to_node:
            return get_path_length(parent, from_node, to_node)

        for child in graph[node]:
            if child not in visited:
                queue.append(child)
                visited.add(child)
                parent[child] = node
        
    return -1


def get_path_length(path: dict, from_node, to_node) -> int:
    result = 1

    target = path[to_node]
    while target != from_node:
            result += 1
            target = path[target]

    return result
            

number_nodes = int(input())
number_pairs = int(input())

pairs = []
graph = {}

for _ in range(number_nodes):
    parent, children = input().split(":")

    if children == [""]:
        children = []
    else:
        children = children.split()
    
    if parent not in graph:
        graph[parent] = children
    else:
        graph[parent] += children

for _ in range(number_pairs):
    from_node, to_node = input().split("-")
    pairs.append((from_node, to_node))

for from_node, to_node in pairs:
    print(f"{{{from_node}, {to_node}}} -> "
          f"{find_path(from_node, to_node, graph)}")