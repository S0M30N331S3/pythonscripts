def display_board(board):
    print(f"{board['1']} | {board['2']} | {board['3']}")
    print("--+---+--")
    print(f"{board['4']} | {board['5']} | {board['6']}")
    print("--+---+--")
    print(f"{board['7']} | {board['8']} | {board['9']}")

def check_win(board, player):
    win_conditions = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['1', '4', '7'],
        ['2', '5', '8'],
        ['3', '6', '9'],
        ['1', '5', '9'],
        ['3', '5', '7']
    ]
    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

def check_draw(board):
    return all(board[pos] != ' ' for pos in board)

def is_valid_move(board, move):
    return board[move] == ' '

def get_player_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move in board and is_valid_move(board, move):
            return move
        else:
            print("Invalid move. Please try again.")

def tic_tac_toe():
    board = {
        '1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '
    }
    current_player = 'X'
    display_board(board)

    while True:
        move = get_player_move(board, current_player)
        board[move] = current_player
        display_board(board)

        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

def rule():
    print("""
Objective: Get three of your marks ('X' or 'O') in a row—horizontally, vertically, or diagonally—before your opponent does.

Players: Two players take turns marking the spaces on a 3x3 grid.

Gameplay:
Players alternate turns, starting with 'X'.
Once placed, marks cannot be moved or removed.

Winning:
A player wins by getting three of their marks in a row.
Rows can be horizontal, vertical, or diagonal.

Draw:
If all spaces are filled without either player achieving three in a row, the game is a draw.""")
print("=====Welcome to Tic Tac Toe=====")
while True:
    print("\n1. Play the game ")
    print("2. View rules")
    print("3. Exit game")

    choice=input("Enter Choice(1-3): ")
    if choice == '1':
        tic_tac_toe()
    if choice == '2':
        rule()
    if choice == '3':
        print("Thanks for playing!")
        break
    else:
        print("Invalid input")