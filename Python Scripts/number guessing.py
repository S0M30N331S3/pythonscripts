import random 

def get_valid_guess():
    while True:
        try:
            guess = int(input("Guess the correct number from 1 to 10: "))
            if 1 <= guess <= 10:
                return guess
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_continue_choice():
    while True:
        choice = input("Enter y to continue, enter n to exit: ").lower()
        if choice in ['y', 'n']:
            return choice
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

while True:
    x = random.randint(1,10)

    while True:
        y = get_valid_guess()

        if y<x:
            print("Higher")
        elif y>x:
            print("lower")
        else:
            print(f"That's right the number is: ",x) 
            break
     
    if get_continue_choice() == 'n':
        ("Thanks for playing!")
        break