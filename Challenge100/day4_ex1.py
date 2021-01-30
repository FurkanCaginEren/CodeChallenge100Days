## BUNKER ROULETTE
import random



print("This game picks a person from a list given by input names becareful u have to write down names format as A, b, ")

name_string = input("Type down names in correct format")

name_list = name_string.split(", ")

winnner = random.choice(name_list)

print (winnner + " is the winner of lottary that has to pay the bill")