def print_board(chess_board):
    for row in chess_board:
        print(" ".join(row))
    print()


def can_place(row, column, rows, columns, left_diagonal, right_diagonal):
    if row in rows:
        return False
    if column in columns:
        return False
    if row - column in left_diagonal:
        return False
    if row + column in right_diagonal:
        return False
    return True


def set_queen(row, column, chess_board, rows, columns, 
              left_diagonal, right_diagonal):
    chess_board[row][column] = "*"
    rows.add(row)
    columns.add(column)
    left_diagonal.add(row - column)
    right_diagonal.add(row + column)


def remove_queen(row, column, chess_board, rows, columns, 
                 left_diagonal, right_diagonal):
    chess_board[row][column] = "-"
    rows.remove(row)
    columns.remove(column)
    left_diagonal.remove(row - column)
    right_diagonal.remove(row + column)



def place_queens(row, chess_board, rows, columns, left_diagonal, right_diagonal):
    if row == 8:
        print_board(chess_board)
        return
    
    for column in range(0, 8):
        if can_place(row, column, rows, columns, left_diagonal, right_diagonal):
            set_queen(row, column, chess_board, rows, columns, 
                      left_diagonal, right_diagonal)
            place_queens(row + 1, chess_board, rows, columns, 
                         left_diagonal, right_diagonal)
            remove_queen(row, column, chess_board, rows, columns,
                          left_diagonal, right_diagonal)



chess_board = [["-"] * 8 for _ in range(8)]
place_queens(0, chess_board, set(), set(), set(), set())

