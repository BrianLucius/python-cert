sudoku1 = [[2,9,5,7,4,3,8,6,1],
           [4,3,1,8,6,5,9,2,7],
           [8,7,6,1,9,2,5,4,3],
           [3,8,7,4,5,9,2,1,6],
           [6,1,2,3,8,7,4,9,5],
           [5,4,9,2,1,6,7,3,8],
           [7,6,3,5,2,4,1,8,9],
           [9,2,8,6,7,1,3,5,4],
           [1,5,4,9,3,8,6,7,2]]

sudoku2 = [[1,9,5,7,4,3,8,6,2],
           [4,3,1,8,6,5,9,2,7],
           [8,7,6,1,9,2,5,4,3],
           [3,8,7,4,5,9,2,1,6],
           [6,1,2,3,8,7,4,9,5],
           [5,4,9,2,1,6,7,3,8],
           [7,6,3,5,2,4,1,8,9],
           [9,2,8,6,7,1,3,5,4],
           [2,5,4,9,3,8,6,7,1]]

def check_rows(sudoku):
    for row in range(9):
        if [1,2,3,4,5,6,7,8,9] != sorted(sudoku[row]):
            return False
    return True

def check_cols(sudoku):
    for col in range(9):
        col_data = []
        for row in range(9):
            col_data.append(sudoku[row][col])
        if [1,2,3,4,5,6,7,8,9] != sorted(col_data):
            return False
    return True

def check_squares(sudoku):
    for row_offset in range(0,9,3):
        for col_offset in range(0,9,3):
            squares_data = []
            for row in range(3):
                for col in range(3):
                    squares_data.append(sudoku[row_offset+row][col_offset+col])
            if [1,2,3,4,5,6,7,8,9] != sorted(squares_data):
                return False
    return True

if check_rows(sudoku1) and check_cols(sudoku1) and check_squares(sudoku1):
    print('Yes')
else:
    print('No')
    
if check_rows(sudoku2) and check_cols(sudoku2) and check_squares(sudoku2):
    print('Yes')
else:
    print('No')