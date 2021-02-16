# Guess a number game
import random
from logo import logo


def choose_level(level):
    if level == "easy":
        return 10
    elif level == "hard":
        return 5


def guess_number():
    print(logo)

    level = input("Choose a level easy or hard ")

    life = choose_level(level)
    print(f"You got {life} lifes")
    guess_number = random.randrange(0, 100)

    print(guess_number)

    guess_correct = False

    while not guess_correct:

        user_number = int(input("Guess a number between 0-100: "))
        if life == 1:
            print("no life left you lost")
            guess_correct = True
        elif guess_number == user_number:
            print("Correct Number")
            guess_correct = True
        elif guess_number > user_number:
            life -= 1
            print("Too low")
            print(f"Remaning life left {life}")
        elif user_number > guess_number:
            life -= 1
            print("Too high")
            print(f"Remaning life left {life}")


while input("Do u want to play guess_number  game Y/N ").lower() == "y":

    guess_number()
