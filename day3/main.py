# Control flow with if / else and conditional operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Comparison operators
# > greater than
# < less than
# >= greater than or equal
# <= less than or equal
# == equal
# != not equal

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
