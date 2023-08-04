first_string = input()
second_string = input()

matrix = [[0] * (len(second_string) + 1) for _ in range(len(first_string) + 1)]

for row in range(len(first_string) - 1, -1, -1):
    for col in range(len(second_string) - 1, -1, -1):
        
        if first_string[row] == second_string[col]:
            matrix[row][col] = matrix[row + 1][col + 1] + 1
        else:
            matrix[row][col] = max(matrix[row + 1][col], matrix[row][col + 1])

row = 0
col = 0
result = ""
while row < len(first_string) and col < len(second_string):
    if first_string[row] == second_string[col]:
        result += first_string[row]
        row += 1
        col += 1
    else:
        if matrix[row +1][col] > matrix[row][col + 1]:
            row += 1
        else:
            col += 1

print(result)