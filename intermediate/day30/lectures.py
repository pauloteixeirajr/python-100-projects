# Catching Expressions: The try catch except finally Pattern
# try:
#     file = open("a_file.txt")
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()

# Raising your own exceptions
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height should be less than 3 meters")

bmi = weight / height ** 2
print(bmi)
