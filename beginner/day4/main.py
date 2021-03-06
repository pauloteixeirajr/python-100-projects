# Random Module
import random

random_int = random.randint(1, 10)
# 0 - 1
random_float = random.random()

print(random_int)
print(random_float)
# 0 - 4
print(random_float * 5)

# Python Lists
states = ["Delaware", "Pennsylvania", "New York"]
states.append("California")
states.extend(["Alaska", "Hawaii"])

print(states)
print(states[0])
print(states[1])
print(states[2])
print(states[-1])

# dirty_dozen = [
#     "Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
#     "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"
# ]

fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_doze = [fruits, vegetables]
