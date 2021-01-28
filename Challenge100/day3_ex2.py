# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
extra_cheese = extra_cheese.capitalize()
add_pepperoni = add_pepperoni.capitalize()
size = size.capitalize()
#Write your code below this line 👇


total_price = 0;

if size == "S":
  total_price = 15

elif size == "M":
  total=price = 20

elif size == "L":
  total_price = 25

if (add_pepperoni == "Y") and (size == "S"):
  total_price += 2

elif (add_pepperoni == "Y") and (not (size == "S")):
  total_price += 3

if extra_cheese == "Y":
  total_price += 1

print(total_price)



