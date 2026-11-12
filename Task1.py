import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def print_board():
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("") 

def winner(player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False

def draw():
    if " " in board:
        return False
    else:
        return True

print("Hello Player!")
print_board()

while True:
    choice = input("Enter a position: ")
    index = int(choice) - 1
    
    if board[index] == " ":
        board[index] = "X"
    else:
        print("Try again")
        continue

    print("Your move:")
    print_board()

    if winner("X") == True:
        print("You won!")
        break
        
    if draw() == True:
        print("Tie!")
        break

   
    print("Computer")
    
    computer_played = False
    while computer_played == False:
        comp_move = random.randint(0, 8)
        if board[comp_move] == " ":
            board[comp_move] = "O"
            computer_played = True

    print("Computer's move:")
    print_board()

    if winner("O") == True:
        print("Computer wins!")
        break
        
    if draw() == True:
        print("Tie!")
        break