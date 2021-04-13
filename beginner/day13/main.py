# Debugging
# Describe the problem
from random import randint


def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Reproduce the bug
dice_imgs = [1, 2, 3, 4, 5, 6]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# Play computer and evaluate each line
year = int(input("What's your year of birth?: "))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.")

# Fix errors and watching for red underlines
age = input("How old are you?")
if age > 18:
    print("You can drive at {age}")

# Squash bugs with a print() statement
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


# Bringing out the Big gun: using a debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
