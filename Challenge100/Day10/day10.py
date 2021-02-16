
# ADD
def add(n1, n2):
    return n1+n2
# Substract


def subsract(n1, n2):
    return n1-n2
# Multiply


def multiply(n1, n2):
    return n1*n2
# Divide


def divide(n1, n2):
    return n1/n2


# for simpler function calls we overload functions to symbols
operations = {
    "+": add,
    "-": subsract,
    "*": multiply,
    "/": divide
}

# recursive function to begin all over when break from while loop


def calculator():
    num1 = float(input("Number one: "))
    for key in operations:
        print(key)

    flag = True
    while flag:
        operational_symbol = input("Pick your operation: ")
        num2 = float(input("Number two: "))
        operation = operations[operational_symbol]
        answer = operation(num1, num2)
        print(f"{num1} {operational_symbol} {num2} = {answer}")

        if input("Do u want to cont Y/N ").lower() == "y":
            num1 = answer
        # to prevent endless loop always add condition
        else:
            flag = False
            calculator()


calculator()
