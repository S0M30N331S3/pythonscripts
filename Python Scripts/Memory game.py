import random
import string
import time

def generate_board():
    letters = random.sample(string.ascii_uppercase[:6] * 2, 12)
    random.shuffle(letters)
    return letters

def display_board(board):
    for i in range(0, 12, 4):
        print(f"{board[i]:>2} | {board[i+1]:>2} | {board[i+2]:>2} | {board[i+3]:>2}")

def rules():
    print("1. Objective: Find all matching pairs of cards.")
    print("2. Turn: Flip over two cards.")
    print("3. If the cards match, remove them from the grid.\nIf they don't match, flip them back over.")
    print("4. Continue: Keep flipping pairs of cards until all pairs are found.")
    print("5. End of Game: The game ends when all pairs have been matched.")
    print("6. Goal: Try to find all pairs in the fewest number of turns.")

def flip_card(hidden_board, board, pos):
    pos = int(pos) - 1
    hidden_board[pos] = board[pos]
    display_board(hidden_board)
    time.sleep(1)
    
def play_game():
    board = generate_board()
    hidden_board = [str(i+1) for i in range(12)]
    turns = 0
    pairs_found = 0

    while pairs_found < 6:
        display_board(hidden_board)

        pos1 = input("Enter the first position to flip (1-12): ")
        while not pos1.isdigit() or not (1 <= int(pos1) <= 12) or hidden_board[int(pos1) - 1] != pos1:
            print("Invalid input or the card is already flipped.")
            pos1 = input("Enter the first position to flip (1-12): ")

        flip_card(hidden_board, board, pos1)

        pos2 = input("Enter the second position to flip (1-12): ")
        while not pos2.isdigit() or not (1 <= int(pos2) <= 12) or hidden_board[int(pos2) - 1] != pos2 or pos1 == pos2:
            print("Invalid input, card already flipped, or same position as the first.")
            pos2 = input("Enter the second position to flip (1-12): ")

        flip_card(hidden_board, board, pos2)

        if board[int(pos1) - 1] == board[int(pos2) - 1]:
            print("It's a match!")
            pairs_found += 1
        else:
            print("Not a match, try again!")
            time.sleep(2)
            hidden_board[int(pos1) - 1] = pos1
            hidden_board[int(pos2) - 1] = pos2

        turns += 1

    print(f"Congrats, you have found all the pairs in {turns} turns!")
    return turns

def update_high_score(score, high_score):
    if high_score == 0 or score < high_score:
        high_score = score
        print(f"New high score: {high_score} turns")
    else:
        print(f"Current high score: {high_score} turns")
    return high_score
    
def start_game():
    high_score = 0
    while True:
        print("\n1. Play the game")
        print("2. View rules")
        print("3. Exit game")

        choice = input("Enter choice (1-3): ")

        if choice == '1':
            score = play_game()
            high_score = update_high_score(score, high_score)
        elif choice == '2':
            rules()
        elif choice == '3':
            print("Thanks for playing!")
            time.sleep(1)
            break
        else:
            print("Invalid choice, please try again")

print("===== Welcome to the Memory Game =====")
start_game()