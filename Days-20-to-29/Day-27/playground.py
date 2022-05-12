#*Args (unlimited arguments)

def add(*args):
    #args are type tuple
    print(type(args))
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(25,25,25,25,25))


#**Kwargs (unlimited keyword arguments)

def calculate(n, **kwargs):
    #kwargs are type dictionary
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

# print(calculate(2, add=3, multiply=5))


class Car():
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.make)