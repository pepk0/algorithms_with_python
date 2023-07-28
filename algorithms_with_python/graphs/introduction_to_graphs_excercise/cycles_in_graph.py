def is_acyclic(graph: dict) -> str:
    dependence = {}
    for node, children in graph.items():
        if node not in dependence:
            dependence[node] = 0
        for child in children:
            if child not in dependence:
                dependence[child] = 1
            else:
                dependence[child] += 1

    if 0 in dependence.values():
        return "Acyclic: Yes"
    return "Acyclic: No"


graph = {}
dependencies = input()
while dependencies != "End":
    
    parent, child = dependencies.split("-")
    if parent not in graph:
        graph[parent] = [child]
    else:
        graph[parent].append(child)

    dependencies = input()

print(is_acyclic(graph))