first_phrase = input()
second_phrase = input()

matrix = [[0] * (len(first_phrase) + 1) for _ in range(len(second_phrase) + 1)]

for i in range(len(first_phrase) + 1):
    matrix[0][i] = i

for i in range(len(second_phrase) + 1):
    matrix[i][0] = i

# for row in matrix:
#     print(*row, sep=" ")

for row in range(1, len(matrix)):
    for col in range(1, len(matrix[0])):

        if first_phrase[row - 1] == second_phrase[col - 1]:
            matrix[row][col] = matrix[row - 1][col - 1]
        else:
            new_value = min(matrix[row - 1][col], matrix[row][col - 1]) + 1
            matrix[row][col] = new_value

print(f"Deletions and Insertions: {matrix[-1][-1]} ")
