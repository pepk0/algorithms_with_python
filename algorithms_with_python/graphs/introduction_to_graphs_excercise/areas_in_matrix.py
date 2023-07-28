def dfs_area(letter: str, row: int, col: int, graph: list) -> None:
    
    if row < 0 or col < 0 or row >= len(graph) or col >= len(graph[0]):
        return
    
    if graph[row][col] != letter:
        return
    
    graph[row][col] = -1

    dfs_area(letter, row + 1, col, graph)
    dfs_area(letter, row - 1, col, graph)
    dfs_area(letter, row, col - 1, graph)
    dfs_area(letter, row, col + 1, graph)


rows = int(input())
columns = int(input())
graph = [[s for s in input()] for _ in range(rows)]
areas = {}
areas_total = 0

for row in range(rows):
    for col in range(columns):
        if graph[row][col] == -1:
            continue

        letter = graph[row][col]
        dfs_area(letter, row, col, graph)
        if letter not in areas:
            areas[letter] = 1
        else:
            areas[letter] += 1
        areas_total += 1

print(f"Areas: {areas_total}")
for letter, frequency in sorted(areas.items()):
    print(f"Letter '{letter}' -> {frequency}")
