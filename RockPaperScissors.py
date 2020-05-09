"""The player and the computer will each guess rock, paper or scissors. Whoever wins gets a point; first to 3 points
wins. Scissors > paper > rock > scissors."""

import random
player_guess = ""
computer_guess = ""
options = [1, 2, 3]
player_score = 0
computer_score = 0
winning_score = 3
num_dict = {1: "rock",
            2: "paper",
            3: "scissors"}

print("You will be playing rock-paper-scissors. Win the best of 3 to win overall!")

while True:
    if computer_score == 3 or player_score == 3:
        break
    player_guess = int(input("Choose 1 (rock), 2 (paper) or 3 (scissors): "))
    if player_guess not in options:
        print("That is not a viable option. Try again")
        continue
    else:
        print("You guessed:", num_dict.get(player_guess))
    computer_guess = random.randint(1, 3)
    print("The computer guessed:", num_dict.get(computer_guess))
    if player_guess == computer_guess:
        print("You tied! Try again")
    elif (player_guess == 1 and computer_guess == 3) or (player_guess == 2 and computer_guess == 1) or (player_guess == 3 and computer_guess == 2):
        player_score += 1
        print(f"Good job; {num_dict.get(player_guess)} beats {num_dict.get(computer_guess)}")
        print(f"The score is {player_score} to {computer_score}")
    elif (computer_guess == 1 and player_guess == 3) or (computer_guess == 2 and player_guess == 1) or (computer_guess == 3 and player_guess ==2):
        computer_score += 1
        print(f"Too bad! {num_dict.get(computer_guess)} beats {num_dict.get(player_guess)}")
        print(f"The score is {player_score} to {computer_score}")

if computer_score == 3:
    print("You lose")
if player_score == 3:
    print("You win!")

