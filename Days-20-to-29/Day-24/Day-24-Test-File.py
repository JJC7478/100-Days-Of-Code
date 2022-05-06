#Opening files in python

#file = open("my_file.txt")

#Reading files

# contents = file.read()
# print(contents)

# #Closing files

# file.close()

#Alternative way of opening and closing files

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#     #No longer have to remember closing down the files

#Make file writeable #Using absolute path
# with open("/Users/johnj/OneDrive/Desktop/my_file.txt", mode= "a") as file:
#     file.write("\nNew text.")
    # "w" is for write, but deletes all the text
    # "a" is for append

#Creating a new file from scratch

# with open("new_file.txt", mode= "w") as file:
#     file.write("New text.")