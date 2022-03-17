# 100-Days-Of-Code
I have decided to challenge myself by teaching myself Python in 100 days. This file documents my progress during this challenge.

## Day 1
I began learning how to use the print(), input() and len() functions in order to get different outputs on the terminal. I also learned about the string data type how to use variables to store data.

*See Day-1-Test-File.py for details.*

Using this knowledge, I was able to create a Band Name Generator, which allowed the user to generate a band name based on the city they're from and their pet's name.

*See Band-Name-Generator.py for details.*

## Day 2

Expanding upon using the functions I previously learned, I learned about several data types such as integers, floats, and booleans. I also learned how to perform mathematical operations such as addition, subtraction, multiplication and division. Using this, I was able to convert data from one type to the next, using f-strings and functions such as str(), int(), and float().


This culminated into building a tip calculator. The tip calculator takes in the total bill of an order, the tip percentage, the amount of people to split the bill into, and produces the amount each person should pay towards the bill and the tip. This involves converting string inputs into floats, performing mathematical calculations, and converting them back into strings to get the split result.

*See Tip-Calculator.py for details.*

## Day 3

This was the first time I started using if/elif/else statements and logical and conditional operators where I learned their logic, how to nest if statements, and how to use multiple ifs in succession. This allowed me to create several different programs.

First, I created a BMI calculator that determined your BMI based on your height and weight. I also created a leap year calculator which checked if a specific year was a leap year. Then, I made a pizza order calculator which determined the bill of your pizza order based on the size of the pizza and the toppings chosen. Finally, I created a love calculator which arbitrarily determined whether or not a couple was meant to be together based on how many letters in their name fell into the words "true love".

*See BMI-Calculator.py, Leap-Year-Calculator.py, Pizza-Order-Calculator.py, and Love-Calculator.py for details.*

I capped the day off with a choose-you-own-adventure program called "Treasure Island" which used all the knowledge I previously learned plus today's new material. In treasure island, the player makes a series of choices based on the prompts presented to them. If they make the right choices, they win the game.

*See Treasure-Island.py for details.*

## Day 4

I began learning about randomization. Specifically, I learned how to create random integers and numbers as well as take randomly selected data from different data types such as strings. From importing the random module, I am able to use functions such as randint() and choice() to randomly generate different data types. I also learned about lists; specifically indeces, appending lists, and nesting them.

One of the programs that I made was "Banker Roulette" which randomly selects from a list of names who is going to pay for the bill for a meal. Another program I made was "Heads or Tails" which is essentially a coin flip simulator. Finally, I created a "Rock, Paper, Scissors" program which allows the player to play the game 'rock, paper, scissors' against the computer.

*See Banker-Roulette.py, Heads-or-Tails.py, and Rock-Paper-Scissors.py for details.*

These programs built up to creating a Treasure Map which determined where the user wanted to place their treasure on a grid-like map made from lists.

*See Treasure-Map.py for details.*

## Day 5

I began learning how to use for loops for the first time, specifically how to use them with lists. I also learned how to use the range() function with for loops.

With this, I created several mini programs, one being the "Average Student Height Calculator" which cycled through a list of student heights and calculated the average. I also made a high score calculator which determined which student got the highest score from a list of test scores. Finally, I solved the FizzBuzz test, a common coding challenge that takes numbers 1-100 and prints "Fizz" for numbers divisible by 3, "Buzz" for numbers divisible by 5, and "Fizzbuzz" for numbers divisible by both 3 and 5.

*See Average-Student-Height-Calculator.py, Highest-Score.py, and FizzBuzz.py for details.*

This culminated into making a Password Generator which created a random password based on the number of letters, numbers, and symbols the user wanted and randomized the order.

*See Password-Generator.py for details.*

## Day 6

This was where I first learned how to create basic functions and use while loops. I learned how to define and call a function as well as how to create while loops for different conditions. Much of the work I did this day was in the online program called 'Reeborg's World':

 https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

## Day 7

This day I worked on "Hangman", a program that plays the popular game Hangman. This project served more as a test and review for all the knowledge I've gained thus far, including different data types such as lists and strings, performing different mathematical operatons, randomization, modules, and for and while loops. The program begins with randomly choosing one word from a large list of words as well as generating a list with a number of undersccores ("_") corresponding to the number of letters in the random chosen word. Then, upon input where the player guesses a letter belonging to the randomly chosen word, the program cycles through each letter in the word to find a match. If the guessed letter is not in the chosen word, the player loses a life out of 6 lives to start with, which is reflected via ASCII art depicting the 'hangman' character becoming more complete as the player loses more lives. Once the player is out of lives, the game ends and they lose. Alternatively, if the player guesses all the letters of the word before losing their lives, they win.

*See Hangman.py for details*

## Day 8

Previously, I was only able to use simple functions without any inputs nor outputs. However, I decided to delve deeper into the versatility of using functions, which began by including inputs. I learned more about functions with inputs, such as positional and keyword arguments, utilizing multiple inputs, and creating more efficient and flexible code.

To put my knowledge to the test, I created two mini programs. The first was a paint area calculator, which calculated the amount of paint cans one would need to cover a surface of a specific height and width based on the coverage of each paint can. I also created a prime number checker which checked if an inputted number was a prime number or not.

*See Paint-Area-Calculator.py and Prime-Number-Checker.py for details.*

Eventually, I was able to build upon using fucntions with inputs by creating a Caesar Cipher program. This program encoded/decoded user text based on a chosen shift number. This shift number indicated the number of times each letter was shifted forwards (encoding) or backwards (decoding). By taking the chosen text, shift number, and shift direction, the Caesar Cipher program uses a function with those inputs to encode/decode user text.

*See Caesar-Cipher.py for details.*

## Day 9

I began learning about a new data type called dictionaries. These are pieces of data that have two components: a key and a value. While practicing with dictionaries, I learned how to create them, retrieve dictionary items, add new items, edit dictionary items, wipe them, loop through items, and nesting lists and other dictionaries in them as well as nesting dictionaries in lists.

As usual, I practiced using dictionaries by creating mini programs. One was a grading program which took data from an existing dictionary containing student scores and created a new dictionary that assigned students to a tier based on those scores. For example, students that scored above 90 were graded "Outstanding" while scores above 70 and below 81 were "Acceptable". Another was a travel log which allowed dictionaries containing the country visited, the number of visits, and cities visited to be added to a travel log list.

*See Grading-Program.py and Travel-Log.py for details.*

To cap off what I learned, I created a Secret Auction program. This allows for users to bid on an item without them knowing each other's bids until the end of the bidding session. Then, the highest bidder is determined and wins the auction. To elaborate, the program creates a list where a function adds dictionaries of each bidder's name and bid amount. Then, the program cycles through each dictionary's bids to determine the highest the bid and, in turn, the auction winner.

*See Secret-Auction-Program.py for details*

## Day 10