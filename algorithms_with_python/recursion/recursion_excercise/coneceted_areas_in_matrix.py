def find_area(row: int, col: int, matrix: list) -> int:

    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    
    if matrix[row][col] == "*":
        return 0
    
    matrix[row][col] = "*"
    result = 1
    result += find_area(row + 1, col, matrix)
    result += find_area(row - 1, col, matrix)
    result += find_area(row, col + 1, matrix)
    result += find_area(row, col - 1, matrix)

    return result


rows = int(input())
columns = int(input())
matrix = [list(input()) for _ in range(rows)]

result = []
for row in range(rows):
    for column in range(columns):
        if matrix[row][column] == "-":
            area = find_area(row, column, matrix)
            result.append({"position": (row, column), "area": area})

print(f"Total areas found: {len(result)}")
for index, value in enumerate(sorted(result, 
                                     key=lambda result: -result["area"])):
    print(f"Area #{index + 1} at {value['position']}, size: {value['area']}")