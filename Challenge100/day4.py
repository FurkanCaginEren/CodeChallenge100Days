import random
tas = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kagit = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

makas = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

 
a = ['tas','kagit','makas']

while True:

    game = random.choice(a)
    print (game)
    choice =input ("tas-kagit-makas q for exit game ")

    if choice == game:
        print ("Draw")
    elif choice == "tas" and game == ('kagit'):
        print (tas)
        print (kagit)
        print ("U lost")
    elif choice == "tas" and game == ('makas'):
        print (tas)
        print (makas)
        print  ("U won")
    elif choice == "makas" and game == ('kagit'):
        print (makas)
        print (kagit)
        print  ("U won")
    elif choice == "makas" and game == ('tas'):
        print (makas)
        print (tas)
        print ("U lost")
    elif choice == "kagit" and game == ('makas'):
        print (kagit)
        print (makas)
        print ("U lost")
    elif choice == "kagit" and game == ('tas'):
        print (kagit)
        print (tas)
        print ("You won")

    if choice == "q":
        break





