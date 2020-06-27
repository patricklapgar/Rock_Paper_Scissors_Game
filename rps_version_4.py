from random import randint

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("Rock...")
    print("Paper...")
    print("Scissors...")
    print("Enter your choice: ")

    player = input("Player 1, make your move:\n").lower()
    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"The computer plays: {computer}")

    if player == computer:
            print("Tie game!!")
    elif player == "rock":
        if computer == "scissors":
                print("The player wins!!")
                player_wins += 1
        else:
            print("The computer wins!!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("The player wins!!")
            player_wins += 1
        else:
            print("The computer wins!!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("The computer wins!!")
            computer_wins += 1
        else:
            print("The player wins!!")
            player_wins += 1
    else:
        print("something went wrong, please enter a choice")