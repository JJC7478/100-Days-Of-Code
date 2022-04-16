# Classes

# class User: #name of class should have first word of every letter capitalized (aka PascalCase)
#     pass

# Adding attributes
# user_1 = User()
# user_1.id = "001"
# user_1.username = "john"

# print(user_1.id)

# Constructor
#A constructor is the part of the blueprint that specifies what should happen when the 
# object is being constructed, aka initializing

#e.g., class Car:
        #def __init__(self):
        ##initialize attributes
class UserOne():
    def __init__(self):
        print("new user being created...")

main_user = UserOne()

# Adding attributes with constructors

class Plane:
    def __init__(self, seats, pilots): #when creating an object of this class, you must provide these parameters, 
                                    #i.e., seats, pilots, otherwise you'll get an error
        self.seats = seats
        self.pilots = pilots
        self.passengers = 0 #to save from having to enter a value every time, you can set an attribute to a specific value

my_plane = Plane(5, 2)
print(my_plane.seats, my_plane.pilots)

# Methods in classes

class Bike:
    def __init__(self):
        self.wheels = 2
    
    def flat_tire(self):
        self.wheels = 1


bike = Bike()
bike.flat_tire()
print(bike.wheels)