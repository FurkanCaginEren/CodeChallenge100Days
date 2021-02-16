MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def report():
    water_level = resources["water"]
    milk_level = resources["milk"]
    coffee_level = resources["coffee"]
    money_level = profit
    return print(f"water: {water_level} \nmilk: {milk_level} \ncoffee: {coffee_level} \nmoney: {money_level} \n")


def insert_money():
    coin = []
    coin_type = ["quarters", "dimes", "nickles", "pennies"]
    for i in range(0, 4):
        coin.append(int(input(f"how many {coin_type[i]} ")))
    print(coin[0]*0.25+coin[1]*0.10+coin[2]*0.05+coin[3]*0.01)
    return coin[0]*0.25+coin[1]*0.10+coin[2]*0.05+coin[3]*0.01


def prep_drink():
    global profit
    stop_prep = False
    req_list = []
    while True:
        order = input("What would you like? (espresso/latte/cappuccino) ")
        if order == "report":
            report()
        elif order == "off":
            return
        else:
            req_list.append(MENU[order]["ingredients"]["water"])
            if order == "espresso":
                req_list.append(0)
            else:
                req_list.append(MENU[order]["ingredients"]["milk"])
            req_list.append(MENU[order]["ingredients"]["coffee"])

            j = 0
            for i in resources:

                if resources[i] < req_list[j]:
                    stop_prep = True
                    print(f"Sorry not enough {i}")
                j += 1

            if not stop_prep:
                total = insert_money()
                if total > MENU[order]["cost"]:
                    change = total - MENU[order]["cost"]
                    print(
                        f"enough money and ur change is : {round(change, 2)}")

                    step = 0
                    for i in resources:
                        resources[i] -= req_list[step]
                        step += 1
                    profit += MENU[order]["cost"]
                    print(f"Here is your {order}")
                else:
                    print("Sorry that's not enough money. Money refunded")


prep_drink()


# Kendime notlar listeye atama yaparak uzatma yapmaya gerek yoktu

# drink  = MENU[order] yaparak dic komple elemanları ile ekleyebilirdim  ve sonrasında basit işlemler

# fonksiyon kullanmaya başladım ama daha çok kullanarak daha basitleştirebilirim
