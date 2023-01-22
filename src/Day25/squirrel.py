
import pandas

data = pandas.read_csv('Squirrel_Data.csv')
sums = data.groupby("Primary Fur Color")["Primary Fur Color"].agg(lambda x: len(x))
sums = pandas.DataFrame(sums)
sums.columns = ["Count"]
print(sums)

new_df = pandas.DataFrame(sums)
new_df.to_csv("Squirrel_Sums.csv")
