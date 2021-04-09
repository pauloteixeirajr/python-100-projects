# Functions with inputs
# Create a function called greet()
# Write 3 print statements inside the function
# Call the greet() function and run your code
def greet(name):
    print(f"Hi {name}")
    print("How do you do?")
    print("Isn't the weather nice today?")


# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# Positional argument
greet_with("Paulo", "England")
# Keyword argument
greet_with(location="Ireland", name="John")
