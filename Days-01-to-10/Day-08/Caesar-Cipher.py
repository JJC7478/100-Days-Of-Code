from base64 import decode
from cmath import log
from turtle import position
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
is_Running = True
def caesar(cipher_direction, user_text, shift_number):
    cipher_text = ""
    if cipher_direction == "decode":
        shift_number *= -1
    for letter in user_text:
        if letter in alphabet:
            index_sum = (int(alphabet.index(letter)) + shift_number)
            cipher_text += alphabet[(index_sum % 26)]
        else:
            cipher_text += letter
    user_text = cipher_text
    print(f"The {direction}d text is {user_text}.")

print(logo)
while is_Running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(cipher_direction=direction, user_text=text, shift_number=shift)
    response = input("Would you like to run again? Press any key to restart or type 'no' to exit.")
    if response == "no":
        is_Running = False