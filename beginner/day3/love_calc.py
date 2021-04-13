# Love Calculator
# Write a program that tests the compatibility between two people.
print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

combined_names = name1 + name2

true = 0
love = 0

true += combined_names.count("t")
true += combined_names.count("r")
true += combined_names.count("u")
true += combined_names.count("e")

love += combined_names.count("l")
love += combined_names.count("o")
love += combined_names.count("v")
love += combined_names.count("e")

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
