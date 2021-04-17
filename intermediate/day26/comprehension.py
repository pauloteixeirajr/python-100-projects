import random
# Understanding List Comprehension
# new_list = [new_item for item in list]
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

print(new_list)

# Conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
long_names = [name.upper() for name in names if len(name) > 4]
print(short_names)
print(long_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Squaring numbers
squared = [num ** 2 for num in numbers]
print(squared)

# Filtering Even Numbers
even = [num for num in numbers if num % 2 == 0]
print(even)

# Understanding Dict Comprehension
# new_list = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {
    student: score
    for (student, score) in students_scores.items() if score >= 60
}
print(passed_students)

# Number of letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# Convert temperatures in C to F
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = {day: (temp * 9 / 5) + 32 for (day, temp) in weather_c.items()}
print(weather_f)
