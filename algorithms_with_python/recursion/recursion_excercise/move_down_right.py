# def find_paths(rows: int, columns: int, 
#                cur_row = 0, cur_col = 0) -> int:
    
#     if cur_row >= rows or cur_col >= columns:
#         return 0

#     if cur_row == rows - 1  and cur_col == columns - 1:
#         return 1
    
#     result = 0
#     result += find_paths(rows, columns, cur_row + 1, cur_col)
#     result += find_paths(rows, columns, cur_row, cur_col + 1)

#     return result


def find_paths(rows: int, columns: int) -> int:

    if rows == 0 or columns == 0:
        return 0
    
    if rows == 1 and columns == 1:
        return 1
    
    return find_paths(rows, columns - 1) + find_paths(rows - 1, columns)



rows = int(input())
columns = int(input())
print(find_paths(rows, columns))