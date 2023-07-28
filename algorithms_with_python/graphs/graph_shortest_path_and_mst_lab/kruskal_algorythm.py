class Edge:
    def __init__(self, parent, child, weight) -> None:
        self.parent = parent
        self.child = child
        self.weight = weight

    def __repr__(self) -> str:
        return f"{self.parent} - {self.child}"


def find_root(grp: list, node: int) -> int:

    while node != grp[node]:
        node = grp[node]
    
    return node

number_edges = int(input())
edges = []
group_test = {}
max_node = 0
for _ in range(number_edges):
    parent, child, weight = [int(i) for i in input().split(", ")]
    max_node = max(parent, child)
    if parent not in group_test:
        group_test[parent] = parent   
    if child not in group_test:
        group_test[child] = child   
    edges.append(Edge(parent, child, weight))

groups = [i for i in range(max_node + 1)]

for edge in sorted(edges, key=lambda x: x.weight):
    first_node = find_root(groups, edge.parent)
    second_node = find_root(groups, edge.child)
    if first_node != second_node:
        groups[first_node] = second_node
        print(edge)

print(group_test)