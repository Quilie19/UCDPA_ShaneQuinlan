import pandas as pd

football_data = pd.read_csv("football_teams.csv")

print(football_data.head(10))

print(football_data.shape)

print(football_data.tail(3))

print(len(football_data.Team.unique()))

print(football_data.columns)

list1 = ["Team","Tournament"]

print(football_data[list1].head())

print(football_data[(football_data["Goals"] < 50) & (football_data["Possession%"] > 50)])

missing_values_count = football_data.isnull().sum()
print(missing_values_count)

cleaned_data = football_data.fillna(0)
print(cleaned_data.isnull().sum())

drop_duplicates = football_data.drop_duplicates()
print(football_data.shape,drop_duplicates.shape)

print(football_data.drop_duplicates())

print(football_data.drop_duplicates(subset=['Tournament']))

df = pd.DataFrame(football_data.drop_duplicates())
print (df)

print(df.sort_values(by = "Goals", ascending = False).head(10))








