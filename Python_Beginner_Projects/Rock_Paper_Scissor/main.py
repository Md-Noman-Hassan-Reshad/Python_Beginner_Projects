import random

choices = ["Rock", "Paper", "Scissors"]
computer = random.randint(1, 3)
player = False

computer_score = 0
player_score = 0

while True:
    print("Enter 0 to end game")
    print("Enter 1, 2, or 3")
    player = input("1.Rock, 2.Paper or 3.Scissors? ").capitalize()

    if player == computer:
        print("Tie!")

    elif player == 1 and computer == 2:
        print("You lose!")
        computer_score += 1

    elif player == 2 and computer == 3:
        print("You lose!")
        computer_score += 1

    elif player == 3 and computer == 1:
        print("You lose!")
        computer_score += 1

    elif player == 0:
        print("Final Scores:")
        print(f"Player's score: {player_score}")
        print(f"Computer's score: {computer_score}")
        break
    
    else:
        print("You won!")
        player_score += 1