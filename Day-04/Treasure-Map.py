row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

pos1 = int(position[0])
pos2 = int(position[1])


map[pos2 - 1][pos1 - 1] = "X"


print(f"{row1}\n{row2}\n{row3}")