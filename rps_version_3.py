# Rock, Paper, Scissors Game
# There are two versions of this game that will be created.
# The first will be basic version where two players enter their choice and 
# only one will win

# The second version will be refactored and more simplified than the first version. 
# The third version will have the player be put up against a computer-generated response

# Import random number module
import random

print("Rock...")
print("Paper...")
print("Scissors...")
print("Enter your choice: ")

player = input("Player 1, make your move:\n").lower()
rand_num = random.randint(0, 2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"The computer plays {computer}")

if player == computer:
        print("Tie game!!")
elif player == "rock":
    if computer == "scissors":
            print("The player wins!!")
    else:
        print("The computer wins!!")
elif player == "paper":
    if computer == "rock":
        print("The player wins!!")
    else:
        print("The computer wins!!")
elif player == "scissors":
    if computer == "rock":
        print("The computer wins!!")
    else:
        print("The player wins!!")
else:
    print("something went wrong, please enter a choice")