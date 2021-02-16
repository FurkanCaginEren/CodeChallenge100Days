programming_dictionary = {}


selection = "y"
while True:
    if selection == "y":
        name = input("Bidder Name: ")
        bid_price = int(input("Bid Amount : $"))
        programming_dictionary[f"{name}"] = bid_price
        selection = input("Are there any more bidders Y/N ").lower()
    if selection != "y" and selection != "n":
        print("Wrong input")
        selection = input("Are there any more bidders Y/N ").lower()
    elif selection == "n":
        break

info_list = []
for i in programming_dictionary:
    info_list.append(programming_dictionary[i])

info_list.sort(reverse=True)

for name, price in programming_dictionary.items():
    if price == info_list[0]:
        print(f"{name} is the winner with {price}$ bid")
