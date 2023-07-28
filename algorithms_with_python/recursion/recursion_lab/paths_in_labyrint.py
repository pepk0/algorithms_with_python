def get_path(row, column, matrix, curr_move, path: list):
    if row < 0 or column < 0 or row >= rows or column >= columns:
        return
    
    if matrix[row][column] == "*":
        return
    
    if matrix[row][column] == "v":
        return
    path.append(curr_move)
    
    if  matrix[row][column] == "e":
        print("".join(path))
    else:
        matrix[row][column] = "v"

        get_path(row + 1, column, matrix, "D", path)
        get_path(row - 1, column, matrix, "U", path)
        get_path(row, column + 1 , matrix, "R", path)
        get_path(row, column - 1, matrix, "L", path)
        matrix[row][column] = "-"

    path.pop()


rows = int(input())
columns = int(input())
matrix = [list(input()) for _ in range(rows)]

get_path(0 , 0, matrix, "", [])

