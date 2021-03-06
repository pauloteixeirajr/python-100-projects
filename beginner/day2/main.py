# Number manipulation and F strings in Python
# Rounding numbers
print(round(8 / 3))  # 3
print(round(8 / 3, 1))  # 2.7
print(round(8 / 3, 2))  # 2.67

# Floor Division (converts to int)
print(8 // 3)  # 2

# F strings
# No need to convert the types
score = 10
height = 1.8
is_winning = True
print(f'Your score is {score}. Your height is {height}. {is_winning}')

# Mathematical Operations in Python
# When doing mathematical operations
# python will follow the (PEMDAS) priority
# PARENTHESES
# EXPONENTS
# MULTIPLICATION DIVISION
# ADDITION SUBTRACTION
print(3 + 5)
print(7 - 3)
print(3 * 2)
print(6 / 3)
print(2 ** 3)  # exponent

# Type Error, Type Checking and Type Conversion
print(type('string'))  # <class 'str'>
print(type(12345679))  # <class 'int'>
print(type(12345.67))  # <class 'float'>
print(type(True))  # <class 'bool'>
print(type(False))  # <class 'bool'>

# Converting to avoid Type Errors
print(str(123) + ' is a nice number')
print(int("12") + 10)
print(float(70) + 100.5)

# Python Primitive Data Types
# Strings
print("Hello"[0])  # = H
print("Hello"[4])  # = o
print("123" + "456")  # 123456

# Integer (whole numbers)
print(123 + 456)  # 579
print(123_456_789)  # 123456789 (py removes the underscores)

# Floats
print(3.14159)

# Booleans
print(True)
print(False)
