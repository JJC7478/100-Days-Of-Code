# Data Types
# String
"Hello"

# Pulling out a particular element from a string is called subscripting
print("Hello"[4])

# Integer

print(123 + 345)

# Underscores can be used instead of commas to separate large numbers (e.g., 345,123,879 -> 345_123_879)

345_123_879

# Floating Point Number (aka, float)

3.14159

# Boolean

True
False
# type() function tells the type of data something is

a = 397.851
type(a)

# str() function converts data to string type

num_char = len("Hello World")
new_num_char = str(num_char)
print(new_num_char)
print("Hello World has " + new_num_char + " characters.")

# float() function converts data to float type

print(80 + float("875"))

# int() function converts data to int type

print(900 + int(825.5))

# Whenever you divide, you always end up with a floating point number
print(6/3)
print(type(6/3))

# Use * to multiply and ** to raise a number to the power of another number
print(8 * 9)
print(2 ** 8)

# Use round() function to round numbers
# Can specify number of decimal places to round to using round(<number> , <number of decimal places>)

print(round(87.598723, 2))

## Can use // during division instead of / to convert output into an integer

print(8 // 3)

## <variable> +=, -=, /= is shorthand for manipulating a variable based on its previous value

score = 0
score += 1
print(score)
print(type(score))

# f-String can be used to convert all values within parentheses into a string
# type f in front of double quotes and put variables in curly braces 

score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}, and you winning is {isWinning}")