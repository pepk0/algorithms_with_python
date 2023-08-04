rows = int(input())
cols = int(input())

matrix = []
value_matrix = []

for _ in range(rows):
    row = [int(i) for i in input().split()]
    matrix.append(row)
    value_matrix.append([0] * cols)

value_matrix[0][0] = matrix[0][0]

index = 1
while index < cols:
    value_matrix[0][index] = value_matrix[0][index - 1] + matrix[0][index]
    index += 1

index = 1
while index < rows:
    value_matrix[index][0] = value_matrix[index - 1][0] + matrix[index][0]
    index += 1

for row in range(1, rows):
    for col in range(1, cols):
        
        right_move = value_matrix[row - 1][col] + matrix[row][col]
        down_move = value_matrix[row][col - 1] + matrix[row][col]
        
        if down_move >= right_move:
            value_matrix[row][col] = down_move
        else:
            value_matrix[row][col] = right_move

idx_row = rows - 1
idx_col = cols - 1
result = []

while idx_row >= 0 and idx_col >= 0:
    result.insert(0, [idx_row, idx_col])

    if idx_row == 0 and idx_col > 0:
        result.insert(0, [idx_row, idx_col])
        idx_col -= 1
        continue

    if idx_row > 0 and idx_col == 0:
        result.insert(0, [idx_row, idx_col])
        idx_row -= 1
        continue

    if value_matrix[idx_row][idx_col - 1] < value_matrix[idx_row -1][idx_col]:
        idx_row -= 1
    else:
        idx_col -= 1

print(*result)