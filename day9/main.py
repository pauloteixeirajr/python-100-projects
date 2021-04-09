# Dictionaries and Nesting
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary
print(programming_dictionary["Bug"])
print(programming_dictionary["Function"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Edit an item in a dictionary
programming_dictionary["Loop"] = "A built-in statement that allows you to repeat code in a loop."

# Loop through a dictionary
for key in programming_dictionary:
    print(programming_dictionary[key])

# Nesting Lists and Dictionaries
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "number_of_visits": 12
    },
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

print(travel_log)
