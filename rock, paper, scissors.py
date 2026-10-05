import random

while True:
    try:
        wins = int(input("How many wins/losses will we play until? (number)"))
        if wins < 1:
            print("Must be at least 1!")
            continue
        losses = wins
    except ValueError:
        print("Only numbers!")
        continue
    break

wins1 = 0
losses1 = 0

while True:
    print()
    my_choice = input("rock, paper, scissors, wind: ").lower().strip()
    options = ["rock", "paper", "scissors", "wind"]
    computer = random.choice(options)
    print()
    print(f"Computer chose: {computer}")
    
    rock = ["scissors", "wind"]
    paper = ["rock"]
    scissors = ["paper", "wind"]
    wind = ["paper"]

    if my_choice not in options:
        print("I don't know that, try again")
        continue
    elif my_choice == computer:
        print("Draw!")
    elif my_choice == "rock" and computer not in rock:
        print("Computer win!")
        losses1 += 1
    elif my_choice == "paper" and computer not in paper:
        print("Computer win!")
        losses1 += 1
    elif my_choice == "scissors" and computer not in scissors:
        print("Computer win!")
        losses1 += 1
    elif my_choice == "wind" and computer not in wind:
        print("computer win!")
        losses1 += 1
    else:
        print("You win!")
        wins1 += 1

    if wins1 >= wins:
        print()
        print(f"You won the game! Wins: {wins1}, losses: {losses1}")
        break
    if losses1 >= wins:
        print()
        print(f"You lost! Wins: {wins1}, losses: {losses1}")
        break
