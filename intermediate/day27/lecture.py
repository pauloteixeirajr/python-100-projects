# *args: unlimited positional arguments
def add(*args):
    return sum(args)


print(add(1, 2, 3, 4, 5, 6, 7, 8, 9))

# **kwargs: unlimited keyword arguments


def calculate(num, **kwargs):
    num += kwargs.get("add")
    num *= kwargs.get("multiply")

    return num


print(calculate(2, add=3, multiply=5))
