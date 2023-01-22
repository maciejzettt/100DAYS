import pandas

data = pandas.read_csv('weather_data.csv')
# print(data)
temperatures = data['temp']
temp_mean = temperatures.mean(numeric_only=True)
temp_max = temperatures.max(numeric_only=True)
temp_min = temperatures.min(numeric_only=True)

monday = data[data.day == 'Monday']
monday_temp = float(monday.temp)
monday_temp_f = round((9 * monday_temp) / 5 + 32, 2)
print(monday_temp_f)