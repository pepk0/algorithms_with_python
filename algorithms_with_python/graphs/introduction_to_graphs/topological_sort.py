def get_dependencies(graph: dict) -> dict:
    dependencies = {}
    for node in graph:
        if node not in dependencies:
            dependencies[node] = 0

        for children in graph[node]:
            if children not in dependencies:
                dependencies[children] = 1
            else:
                dependencies[children] += 1
    
    return dependencies


def find_unrepentant_node(dependencies: dict) -> str | int:
    for node, dependence in dependencies.items():
        if dependence == 0:
            return node
    return -1 

# getting the graph from input
nodes = int(input())
graph = {}
for _ in range(nodes):
    line_tokens = input().split('->')
    node = line_tokens[0].strip()
    children = line_tokens[1].strip().split(', ') if line_tokens[1] else []
    graph[node] = children

dependence = get_dependencies(graph)
topological_sort = []
graph_has_cycle = False

while dependence:
    
    unrepentant_node = find_unrepentant_node(dependence)
    if unrepentant_node == -1:
        graph_has_cycle = True
        break
    topological_sort.append(unrepentant_node)
    for child in graph[unrepentant_node]:
        dependence[child] -= 1
    dependence.pop(unrepentant_node)

if graph_has_cycle:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(topological_sort)}")

    