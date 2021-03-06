print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[      ]
*******************************************************************************''')
print("Welcome to Treasure Island!\n Your Mission is to find the treasure.")

direction = input("Left or right?\n")
lower_direction = direction.lower()
if lower_direction == "right":
    print("Fall into a hole. Game Over.")
    input("Press any key to exit")
elif lower_direction == "left":
    action = input("Swim or wait?\n")
    lower_action = action.lower()
    if lower_action != "wait":
        print("Attacked by trout.\n Game Over.")
        input("Press any key to exit")
    elif lower_action == "wait":
        door = input("Which Door? Red, Blue, or Yellow?\n")
        lower_door = door.lower()
        if lower_door == "yellow":
            print("You Win!")
            input("Press any key to exit")
        elif lower_door == "red":
            print("Burned by fire.\n Game Over.")
            input("Press any key to exit")
        elif lower_door == "blue":
            print("Eaten by beasts.\n Game Over.")
            input("Press any key to exit")
else:
    print("Game Over.")
    input("Press any key to exit")


