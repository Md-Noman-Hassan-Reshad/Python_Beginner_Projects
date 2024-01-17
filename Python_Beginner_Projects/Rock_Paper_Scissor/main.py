import random

choices = ["Rock(1)", "Paper(2)", "Scissors(3)"]
computer_score = 0
player_score = 0

total_match = int(input("How many match do you want to play? "))

for match in range(1, total_match + 1):
    print(f"Total match is {total_match}")
    print(f"Match {match}")
    print()

    print("Enter 1, 2, or 3")

    # Get player input and convert it to an integer
    player = input("1. Rock, 2. Paper, or 3. Scissors? ")
    print()

    # Ensure player input is a valid choice
    if player not in ['1', '2', '3']:
        print("Invalid choice. Please enter 1, 2, 3, or 0.")
        print()
        continue

    # Convert player input to an integer
    player = int(player)

    # Get a random choice for the computer
    computer = random.randint(1, 3)

    # Display the choices
    print(f"Player chose: {choices[player - 1]}")
    print(f"Computer chose: {choices[computer - 1]}")

    # Compare choices and determine the winner
    if player == computer:
        print("Tie!")

    elif (player == 1 and computer == 2) or \
         (player == 2 and computer == 3) or \
         (player == 3 and computer == 1):
        print("You lose!")
        computer_score += 1

    else:
        print("You won!")
        player_score += 1

    print()
    print(f"Player's score: {player_score}")
    print(f"Computer's score: {computer_score}")

    print(f"Match left {total_match - match}")
    print("-" * 40)

print("Final Scores:")
print(f"Player's score: {player_score}")
print(f"Computer's score: {computer_score}")
print()

if player_score > computer_score:
    print(f"Player Won the match!")
elif player_score == computer_score:
    print("The match was Tie!")
else:
    print("Computer Won the match!")
