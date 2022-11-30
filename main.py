import pandas

data = pandas.read_csv("weather_data.csv")
#print(type(data["day"]))
#print(type(data))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

#average = round(sum(temp_list) / len(temp_list), 2)
#print(average)

print(data.temp)

# Get data in row
print(data[data.day == "Wednesday"])
print(data[data.temp == data.temp.min()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp_celsius = int(monday.temp)
monday_temp_farenheit = monday_temp_celsius * 9/5 + 32
print(monday_temp_farenheit)

# Create a dataframe from scratch
data_dict = {"Students":["Ola", "Tina", "Crille"], "Scores": [89, 76, 71]}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("our_results.csv")