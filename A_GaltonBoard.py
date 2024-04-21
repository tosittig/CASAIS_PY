import random as rd
# import numpy as np
# import matplotlib.pyplot as plt


# Function for the decision of the ball at a nail
def get_decision():
    # Generate a random number between 0 and 1
    rand_num = rd.random()
    # Define return values as either 0 or 1
    if rand_num < 0.5:
        return 0
    else:
        return 1


# Function to run a ball through the board
def run_ball():
    count_bin = 0
    for i in range(height):
        decision = get_decision()
        count_bin = count_bin + decision
        print("decision", i, ": ", decision)
    # update bins with the result of the ball
    bins[count_bin] = bins[count_bin] + 1
    # print sum for testing
    print("Sum: ", count_bin)
    print()

# Define the size of the Dalton Board
height = int(input("Height? "))
# create a vector with a number of elements equal to height and initialize all elements to '0'
bins = [0] * (height + 1)

# Run a large number of balls through the board
balls = int(input("Number of balls? "))
for j in range(balls):
    run_ball()

# print bins for testing
print()
print("Number of balls in the bins: ")
print(bins)

# visualize results
# plt.bar(range(len(bins)), height=bins, color="blue")
# plt.xlabel("Bins")
# plt.ylabel("Number of balls")
# plt.title("Galton Board Simulation")
# plt.savefig("./cx_out/galton_board.png")
