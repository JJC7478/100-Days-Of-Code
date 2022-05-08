# import csv

# # data = []
# # with open("weather_data.csv") as file:
# #     old_data = file.readlines()
# #     for line in old_data:
# #         new_line = line.strip()
# #         data.append(new_line)

# # print(data)

# with open ("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas