import pandas

#Creates dictionary of letters and corresponding NATO code words

nato_alphabet = pandas.read_csv("NATO-Alphabet/nato_phonetic_alphabet.csv")
nato_dict = {value.letter: value.code for (key,value) in nato_alphabet.iterrows()}



#Creates a list of the phonetic code words from a word that the user inputs

new_word = input("Enter a word: ").upper()
code_words = [code_word  for letter in new_word for (key,code_word) in nato_dict.items() if letter == key]

print(code_words)