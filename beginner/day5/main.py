# Python Loops
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# for loops and the range function
# doesn't print the last number
for number in range(1, 11):
    print(number)

# Adding all numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number

print(total)
