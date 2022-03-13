#Creating a dictionary
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again."}

#Retrieving items from a dictionary
print(programming_dictionary["Bug"])

#Adding new items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary["Loop"])

#Creating an empty dictionary
empty_dictionary = {}

#Wipe an existing dictionary
programming_dictionary = empty_dictionary
print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A worm in your computer."
print(programming_dictionary["Bug"])

#Loop through a dictionary
for key in programming_dictionary:
    #retieves only key
    print(key)
    #retrieves key value
    print(programming_dictionary[key])