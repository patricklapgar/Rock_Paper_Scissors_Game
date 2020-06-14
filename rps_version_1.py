# Rock, Paper, Scissors Game
# There are two versions of this game that will be created.
# The first will be basic version where two players enter their choice and 
# only one will win

# The second version will put the player against a computer-generated answer

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move:\n")
player2 = input("Player 2, make your move:\n")

if player1 == "rock" and player2 == "scissors":
    print("player 1 wins!!")
elif player1 == "rock" and player2 == "paper":
    print("player 2 wins!!")
elif player1 == "paper" and player2 == "rock":
    print("player 1 wins!!")
elif player1 == "paper" and player2 == "scissors":
    print("player 2 wins!!")
elif player1 == "scissors" and player2 == "rock":
    print("player 2 wins!!")
elif player1 == "scissors" and player2 == "paper":
    print("player 1 wins!!")
elif player1 == player2:
    print("Tie game!!")
else:
    print("something went wrong, please enter a choice")