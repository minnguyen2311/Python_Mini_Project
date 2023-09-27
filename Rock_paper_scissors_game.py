
# Rock paper scissors game

import random

user_wins=0
computer_wins=0

options=["rock","paper","scissors"]

while True:
    user_input = input("Please type Rock/Paper/Scissors or type Q to quit: ").lower().lstrip()
    if user_input == "q":
        break
    elif user_input not in options:
        continue

    random_number=random.randint(0,2)
    # rock:0, paper:1, scissors:2
    computer_input=options[random_number]
    if user_input == "rock" and computer_input == "scissors":
        user_wins += 1
        print("You won")

    elif user_input == "paper" and computer_input == "rock":
        user_wins += 1
        print("You won")
    elif user_input == "scissors" and computer_input == "paper":
        user_wins += 1
        print("You won")
    elif user_input == computer_input:
        print("It is a draw")
    else:
        computer_wins += 1
        print("You lost")

print("You won", user_wins, "times" + ", " + "the computer won", computer_wins, "times" )
print("Goodbye!")