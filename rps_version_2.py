# Rock, Paper, Scissors Game
# There are two versions of this game that will be created.
# The first will be basic version where two players enter their choice and 
# only one will win

# The second version will be refactored and more simplified than the first version. 
# The third version will have the player be put up against a computer-generated response

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move:\n")
print("**** NO CHEATING ****\n\n" * 20)
player2 = input("Player 2, make your move:\n")

if player1 == player2:
        print("Tie game!!")
elif player1 == "rock":
    if player2 == "scissors":
            print("player 1 wins!!")
    elif player2 == "paper":
        print("player 2 wins!!")
elif player1 == "paper":
    if player2 == "rock":
        print("player 1 wins!!")
    elif player2 == "scissors":
        print("player 2 wins!!")
elif player1 == "scissors":
    if player2 == "rock":
        print("player 2 wins!!")
    elif player2 == "paper":
        print("player 1 wins!!")
else:
    print("something went wrong, please enter a choice")