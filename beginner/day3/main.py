# Control flow with if / else and conditional operators
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

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
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be okay. You get a free ride!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    # Multiple if statements in succession
    wants_photo = input("Do you want a photo taken? Y or N: ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
