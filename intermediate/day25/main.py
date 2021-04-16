# Reading CSV Data in Python
# with open("./intermediate/day25/weather_data.csv") as data:
#     csv = data.readlines()
#     print(csv)
# import csv

# # in-built
# with open("./intermediate/day25/weather_data.csv") as data:
#     rows = csv.reader(data)
#     temperatures = []
#     for row in list(rows)[1:]:
#         temperatures.append(int(row[1]))

#     print(temperatures)

import pandas

data = pandas.read_csv("./intermediate/day25/weather_data.csv")
print(data["temp"])
