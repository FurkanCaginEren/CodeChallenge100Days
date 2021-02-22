#Unlimited positional arguments with function

def add(*args):
    return sum(args)


# **kwargs Keywords arguments within function
# n ==> variable **kwargs ==> dic with key words and values
def calculate(n,**kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# Class ex with **kwargs

class Car():
    def __init__(self,**kwargs):
        self.model = kwargs.get("model")
        self.make = kwargs.get("make")


my_car = Car(make="nissan")