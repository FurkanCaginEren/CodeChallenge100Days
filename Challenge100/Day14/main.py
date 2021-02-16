from logo import logo
from data import data
from logo import vs
import random

print(logo)

# name = string
# follower_count = int
# description = string
# country = string


def pick_person():
    """"Picks random person from data list"""
    return random.choice(data)


def compare_follower(data1, data2):
    """Compares follower_count values in Data"""
    if data1['follower_count'] > data2['follower_count']:
        return "a"
    else:
        return "b"


def game():
    person_1 = pick_person()
    person_2 = pick_person()
    score = 0
    game_is_on = True

    while game_is_on:
        person_1 = person_2
        person_2 = pick_person()
        while person_1 == person_2:
            person_2 = pick_person()

        print(
            f"Compare A: {person_1['name']} a {person_1['description']},from {person_1['country']} ")
        print(vs)
        print(
            f"Compare B: {person_2['name']} a {person_2['description']},from {person_2['country']} ")

        if input("Choose A for 1st B for 2nd ").lower() == compare_follower(person_1, person_2):
            score += 1
        else:
            game_is_on = False
            print("Game Over")

        print(f"Total Score {score}")


game()
