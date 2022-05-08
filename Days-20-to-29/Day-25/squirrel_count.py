import pandas

data = pandas.read_csv("squirrel_data.csv")

#Retrieving number of squirrels for each color
gray = (len(data[data["Primary Fur Color"] == "Gray"]))
cinnamon = ((len(data[data["Primary Fur Color"] == "Cinnamon"])))
black = (len(data[data["Primary Fur Color"] == "Black"]))

#Creating dataframe
data_dict = {
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [int(gray), int(cinnamon), int(black)]
}

squirrel_count = pandas.DataFrame(data_dict)
print(squirrel_count)
squirrel_count.to_csv("squirrel_count.csv")