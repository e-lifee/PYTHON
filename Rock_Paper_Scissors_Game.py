# Import the random library
import random

# Add the code to create a list containing the three actions of the game.
game = ["rock", "paper", "scissors"]

# Add the code to set the scores of players to 0
score1, score2 = 0, 0

# Add a round_counter that is 0 at the beginning
round_counter = 0

# Add the code to ask the user how many rounds they want to play
rounds = int(input("How many rounds do you want to play? "))

# Write a while loop and put the game inside
while round_counter < rounds:

    # increase round_counter by 1 and print it
    round_counter += 1
    print(f"Round {round_counter}")

    # Add the code to select a random action for each player
    player1 = random.choice(game)
    player2 = random.choice(game)

    # Add the code to print the players' choices
    print(f"Player 1: {player1}")
    print(f"Player 2: {player2}")

    # Add the tie condition
    if player1 == player2:
        print("Tie!")

    # Add the remaining conditions
    elif player1 == "paper" and player2 == "rock":
        score1 += 1

    elif player1 == "paper" and player2 == "scissors":
        score2 += 1

    elif player1 == "scissors" and player2 == "rock":
        score2 += 1

    elif player1 == "scissors" and player2 == "paper":
        score1 += 1

    elif player1 == "rock" and player2 == "paper":
        score2 += 1

    elif player1 == "rock" and player2 == "scissors":
        score1 += 1

    else:
        print("ERROR")

    # print the score
    print(f"Score: Player 1 - {score1}, Player 2 - {score2}")
#Print the outcome of the game by using conditional statements
if score1>score2 :
      print("PLAYER1'S WON!")
elif score1<score2 :
      print("PLAYER2'S WON!")
else :
      print("Tie! Both players chose the same action.")
