board = [["","",""],
         ["","",""],
         ["","",""]]

def print_board(board):
    #use loops to iterate through the rows and columns of the board, printing each square in the appropriate location
    print("  0   1   2")
    k = 0
    for i in range(3):
        print(k, end=" ")
        for j in range(3):
            print(board[i][j], end = " ")
            if j < 2:
                print(' | ', end='')
        print()
        k+=1
        if i < 2:
            print("  ---------")
def index_validation(board, symbol):
    # prompt the player for their move (using input())
    while True:
        try:
            row_index = int(input(f"Player {symbol}, enter row (0-2): "))
            col_index = int(input(f"Player {symbol}, enter column (0-2): "))
            if row_index < 0 or row_index > 2 or col_index < 0 or col_index > 2 :
                print("Please enter a valid number between 0 and 2.")
                continue
            return row_index, col_index
        except ValueError:
            print("Invalid input. Please enter a valid integer between 0 and 2.")
            
def next_move(board, symbol):
    #check the game board if the location is available for next move
    row_index, col_index = index_validation(board, current_player)
    while(True):
        if board[row_index][col_index] != "":
            print("Place has been taken choose another one..")
            row_index, col_index = index_validation(board, current_player)
        else:
            return row_index, col_index
        
    
def check_winner(board, symbol):
    #check if any of the rows, columns, or diagonals of the board contain three of the player's symbols in a row
    for i in range(3):
        row_win = True
        for j in range(3):
            if board[i][j] != symbol:
                row_win = False
                break
        if row_win:
            return True

    for i in range(3):
        col_win = True
        for j in range(3):
            if board[j][i] != symbol:
                col_win = False
                break
        if col_win:
            return True

    main_diag_win = True
    for i in range(3):
        if board[i][i] != symbol:
            main_diag_win = False
            break
    if main_diag_win:
        return True

    secondary_diag_win = True
    for i in range(3):
        if board[i][2 - i] != symbol:
            secondary_diag_win = False
            break
    if secondary_diag_win:
        return True

    return False


def check_tie(board):
    #if every square on the board has been filled.
    for i in range(3):
        for j in range(3):
            if(board[i][j] != ""):
                continue
            else:
                return False

    return True

while(True):
    current_player = input('Choose a symbol to play with (X-O): ')
    if current_player.upper() == 'X' or current_player.upper() == 'O':
        break
    else:
        print('Invalid input..')


Flage = True
while Flage:
    # In each iteration of the loop, print the current state of the game board, prompt the current player for their move,
    # update the game board with the player's symbol, and check if the game has been won or tied.
    # If the game has been won or tied, end the loop and print the appropriate message
    print_board(board)
    row,col = next_move(board, current_player)
    board[row][col] = current_player

    if check_winner(board, current_player):
        print_board(board)
        print(f"Player {current_player} wins.")
        Flage = False
    elif check_tie(board):
        print_board(board)
        print("It's a tie!")
        print("Both players lost")
        Flage = False

    current_player = 'O' if current_player.upper() == 'X' else 'X'
    
    
    
    
    