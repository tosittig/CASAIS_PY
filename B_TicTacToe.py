import numpy as np
import random as rd


# Function to setup a new board
def setup():
    board = np.array([[' .', ' .', ' .'],
                      [' .', ' .', ' .'],
                      [' .', ' .', ' .']], dtype=str)
    return board


# Function to print the board to the console
def output(board):
    print("  x  1  2  3 ")
    print("y ----------")
    for r in range(3):
        print(r + 1, "|", end=" ")
        for c in range(3):
            print(board[r, c], end=" ")
        print()
    print()


# Function to request user input (x and y coordinate) and update the board with 'X'
def user_input(board):
    while True:
        x = int(input("Enter x-coordinate of your 'X' (1-3): ")) - 1
        y = int(input("Enter y-coordinate of your 'X' (1-3): ")) - 1
        if 0 <= x < 3 and 0 <= y < 3:
            if board[y, x] == ' .':
                board[y, x] = ' X'
                break
            else:
                print("Cell already occupied! Please enter different coordinates.")
        else:
            print("Invalid coordinates! Please enter values between 1 and 3.")


# Extension: Function to generate random input (x and y coordinate) and update the board with 'O'
def computer_input(board):
    while True:
        x = rd.randint(0, 2)
        y = rd.randint(0, 2)
        if board[y, x] == ' .':
            board[y, x] = ' O'
            break


# Function to detect winner in the board
def hasWon(board):
    # Check diagonals
    if (board[0, 0] == board[1, 1] == board[2, 2] != ' .') or (board[0, 2] == board[1, 1] == board[2, 0] != ' .'):
        return True

    # Extension: Check rows and columns
    for i in range(3):
        if (board[i, 0] == board[i, 1] == board[i, 2] != ' .') or (board[0, i] == board[1, i] == board[2, i] != ' .'):
            return True

    return False


# Function to make next move while nobody has won
def next_move(board):
    while not hasWon(board):
        user_input(board)
        output(board)
        if hasWon(board):
            print("Congratulations! You won!")
            break
        computer_input(board)
        output(board)
        if hasWon(board):
            print("Computer has won!")
            break


# Set up new game
board = setup()
output(board)

# Start the game
next_move(board)
