with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

names1 = []

for name in names:
    new_name = name.replace("\n", "")
    names1.append(new_name)

for name in names1:
    with open("./Input/Letters/starting_letter.txt", mode="a+") as letter:
        letter.seek(0)
        txt = letter.read()
        letter_to_name = txt.replace("[name]", f"{name}")
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="a+") as draft:
            draft.write(letter_to_name)

