# Prevent the program from crashing. If the user enters
# something that is out of range, just print a default
# output of "Fruit pie"

fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(f"{fruit} pie")


make_pie(4)  # Fruit pie
make_pie(1)  # Pear pie
