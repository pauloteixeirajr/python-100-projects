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
