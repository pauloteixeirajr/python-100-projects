import pandas

file_path = "./intermediate/day25/data/2018_central_park_squirrel_data.csv"

squirrel_data = pandas.read_csv(file_path)

black_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
gray_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels.size, cinnamon_squirrels.size, black_squirrels.size]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
