import pandas

data = pandas.read_csv('50_states.csv')
data_list = data.to_dict('records')
print(data_list)