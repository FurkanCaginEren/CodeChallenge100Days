import random
from names import word_list
from stages import stages

chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
for i in range(len(chosen_word)):
    display.append("_")

print(display)

life = 7
while True:
    guess = input("Guess a letter: ").lower()
    i = 0

    for letter in chosen_word:
        if letter == guess:

            display[i] = letter
        i += 1
    if guess not in chosen_word:
        print(stages[life-1])
        life -= 1
        print("No Letter in Word,Life LEFT:{}".format(life))

    print(display)
    if "_" not in display or life == 0:
        print("Game Over")
        life = 0
        break
