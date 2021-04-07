# Write a program that chooses a random name to pay the bill
import random

names_str = input("Give me everybody's names, separated by a comma: ")
names = names_str.split(", ")
random_index = random.randint(0, len(names) - 1)
random_name = names[random_index]

print(f"{random_name} is going to buy the meal today!")
