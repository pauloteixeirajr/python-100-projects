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
print(data["temp"].to_list())
print(data["temp"].mean())
print(data["temp"].max())
print(data["temp"].min())
print(data.temp)

# Searching a data frame
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.temp, monday.condition)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Agatha"],
    "scores": [76, 56, 65]
}

new_df = pandas.DataFrame(data_dict)
print(new_df)

# You can use dataframes to save new csvs
new_df.to_csv('./intermediate/day25/new_def.csv')
