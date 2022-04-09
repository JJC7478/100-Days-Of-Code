fruits = ["Apple", "Peach", "Pear"]
#for loop
for fruit in fruits: #takes each value in fruits and assigns the variable fruit to them
    print(fruit)
    print(fruit + " Pie")
    print(fruits)
print(fruit)

#for loop with range
for n in range(1, 11):
    print(n)

for n in range(1, 10, 3): #3 defines how much gets added to each instance of n
    print(n)

#Adding only even numbers in a range
total = 0
for n in range(1, 101):
    if n % 2 == 0:
        total += n
print(total)