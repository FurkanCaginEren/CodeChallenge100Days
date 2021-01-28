## Tip Calculator

bill = float(input("Bill cost? $"))

person_size = float(input("How many of you going to pay for it   "))

tip_percent = float(input("How much tip u gonna pay 10,12,15   "))

print("Each person should pay   {}".format((tip_percent/100*bill+bill)/person_size))