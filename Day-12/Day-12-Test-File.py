#Scope

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

#increase_enemies()
#print(f"enemies outside function: {enemies}")

# Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# print(potion_strength) <- potion_strength not accessible outside of the confines of drink_potion()

# Global Scope

# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()

# There is no Block scope in python

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy) # new_enemy still exists in global scope and not only within if block


# Modifying global scope

# enemies = 1

# def increase_enemies():
    # global enemies # use global to specify that you are referencing a global variable rather than a local variable
    # CAUTION: try to avoid modifying global scope within a function that has local scope like below
    #enemies += 1
    # instead, for example, return the modification as an output and set it equal to the global variable
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies() 
# print(f"enemies outside function: {enemies}")

# Global Constants

#Naming convention of global constants is to turn the variable into all uppercase

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@JJC7478"