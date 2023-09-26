
#random_number_guess_game

import random

print("Welcome to the Random_number_guess")
while True:
    top_of_range = input("Please type the top range number: ")
    if top_of_range.lstrip("-").isdigit():
        top_of_range=int(top_of_range)

        if top_of_range <= 0:
            print("Please type a number larger than 0. Try again!")
            continue
        else:
            break

    else:
        print("Please type a number. Try again!")
        continue

random_number = random.randint(0,top_of_range)

guesses=0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess==random_number:
        print("You got it")
        break
    elif user_guess>random_number:
        print("You were above the number")
    else:
        print("You were below the number")

print("You got it in", guesses, "guesses" )