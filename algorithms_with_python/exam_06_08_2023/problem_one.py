def shortest_path(matrix: list, moves: list):
    start_position = (0, 0, 0)
    queue = [start_position]
    
    while queue:
        next_row, next_col, length = queue.pop(0)

        for move_row, move_col in moves:
            if next_row + move_row < 0 or next_row + move_row >= len(matrix):
                continue
            if next_col + move_col < 0 or next_col + move_col >= len(matrix[0]):
                continue

            new_row = next_row + move_row
            new_col = next_col + move_col

            if matrix[new_row][new_col] == "E":
                return length + 1

            if matrix[new_row][new_col] == ".":
                queue.append((new_row, new_col, length + 1)) # type: ignore
                matrix[new_row][new_col] = "#"
        
    return - 1


rows = int(input())
maze = [[s for s in input()] for _ in range(rows)]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
path = float("inf")

while True:

    result = (shortest_path(maze, moves))
    if result == -1:
        break

    if result <= path:
        path = result

print(path)