import pandas as pd
import numpy as np

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

premierleague_standings = pd.read_csv("PremierLeague_standings.csv")

print (premierleague_standings)

df1 = pd.DataFrame(premierleague_standings)

print(df.loc[df["Tournament"] == "Premier League"])

print(pd.merge(df,df1,on="Team"))

bundesliga_standings = pd.read_csv("Bundesliga_standings.csv")
laliga_standings = pd.read_csv("LaLiga_standings.csv")
ligue1_standings = pd.read_csv("Ligue1_standings.csv")
seriea_standings = pd.read_csv("SerieA_standings.csv")

df2 = pd.DataFrame(bundesliga_standings)
df3 = pd.DataFrame(laliga_standings)
df4 = pd.DataFrame(ligue1_standings)
df5 = pd.DataFrame(seriea_standings)

concat_df = pd.concat([df1, df2, df3, df4, df5], axis = 0, ignore_index= True)
print(concat_df)

print(concat_df.sort_values(by = "P", ascending = False).head(10))














