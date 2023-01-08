from random import randrange

board = []
board_lookup_table = [('n/a', 'n/a'), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in range(0,13):
        if (row == 0) or (row % 4 == 0):
            print('+-------+-------+-------+')
        elif (row % 2 != 0):
            print('|       |       |       |')
        elif (row %2 == 0):
            print('|', board[int((row-2)/4)][0], '|', board[int((row-2)/4)][1], '|', board[int((row-2)/4)][2],'|', sep='   ', end='\n')

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    valid_move = False
    while not valid_move:
        try:
            move = int(input('Enter your move: '))
            if not(1 <= move <= 9):
                print('Not a valid move, try again.')
                valid_move = False
            elif board_lookup_table[move] not in make_list_of_free_fields(board):
                print('Cell already taken, try again.')
            else: 
                valid_move = True
        except:
            print('Not a valid value. Try again.')
            valid_move = False
    (x, y) = board_lookup_table[move]
    board[x][y] = 'O'

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    free_fields.clear()
    for x in range(0, 3):
        for y in range(0, 3):
            if board[x][y] not in ['X','O']:
                free_fields.append((x,y))
    return(free_fields)
        

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    victory = False
    if ([sign]*3 in ([[board[row][col] for row in range(0, 3)] for col in range(0,3)]) or
        [sign]*3 in ([[board[row][col] for col in range(0, 3)] for row in range(0,3)]) or
        [sign]*3 in ([[board[row][row] for row in range(0, 3)]]) or
        [sign]*3 in ([[board[2-row][row] for row in range(0, 3)]])):
        victory = True
    return victory

def draw_move(board):
    # The function draws the computer's move and updates the board.
    valid_move = False
    while not valid_move:
        move = randrange(1, 10)
        if board_lookup_table[move] in make_list_of_free_fields(board):
            valid_move = True
            (x, y) = board_lookup_table[move]
            board[x][y] = 'X'

def generate_board(board):
    # for r in range(0, 7, 3):
    #     row = [r+c for c in range(1, 4)]
    #     board.append(row)
    board.extend([[row + col for col in range(1, 4)] for row in range(0, 7, 3)])
    board[1][1] = 'X'

generate_board(board)

while make_list_of_free_fields(board) != []:
    display_board(board)
    enter_move(board)
    if victory_for(board, 'O'):
        break
    draw_move(board)
    if victory_for(board, 'X'):
        break
    
display_board(board)    
if victory_for(board, 'O'):
    print("Congratulations, you win this round!")
elif victory_for(board, 'X'):
    print("The computer wins this round!")
else:
    print("This round was a draw.")
