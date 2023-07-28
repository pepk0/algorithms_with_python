def dfs_salary(node: int, graph: dict, salaries = {}):

    if graph[node] == []:
        salaries[node] = 1
        return 1
    
    if node in salaries:
        return salaries[node]
    
    result = 0
    for child in graph[node]:
        result += dfs_salary(child, graph)
    salaries[node] = result

    return result


graph = {}
employs = int(input())
for i in range(employs):
    employ = input()
    graph[i] = [x for x in range(employs) if employ[x] == "Y"]

result = 0
for employ in graph:
    result += dfs_salary(employ, graph)

print(result)