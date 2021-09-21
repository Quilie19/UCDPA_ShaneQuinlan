import pandas as pd
import numpy as np
import os

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

import matplotlib.pyplot as plt
import seaborn as sns

PL = df[df.Tournament == "Premier League"]
BL = df[df.Tournament == "Bundesliga"]
LL = df[df.Tournament == "LaLiga"]
L1 = df[df.Tournament == "Ligue 1"]
SA = df[df.Tournament == "Serie A"]

colors_blue = ["#132C33", "#264D58", '#17869E', '#51C4D3', '#B4DBE9']
colors_dark = ["#1F1F1F", "#313131", '#636363', '#AEAEAE', '#DADADA']
colors_red = ["#331313", "#582626", '#9E1717', '#D35151', '#E9B4B4']
colors_mix = ["#17869E", '#264D58', '#179E66', '#D35151', '#E9DAB4', '#E9B4B4', '#D3B651', '#6351D3']
colors_div = ["#132C33", '#17869E', '#DADADA', '#D35151', '#331313']

sns.palplot(colors_blue)
sns.palplot(colors_dark)
sns.palplot(colors_red)
sns.palplot(colors_mix)
sns.palplot(colors_div)

grouped = df.groupby("Tournament").sum()
df_idn = grouped.Goals

fig, ax = plt.subplots(figsize=(14, 8), dpi=75)

pie = ax.pie(
    df_idn,
    colors=colors_mix[0:7],
    wedgeprops=dict(width=0.5, alpha=0.9),
    autopct='%1.0f%%',
    pctdistance=1.12,
    textprops={
        'fontsize': 12,
        'color': colors_dark[2],
        'fontweight': 'bold'
    },
)

ax.legend(df_idn.index, loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=2, borderpad=1, frameon=False, fontsize=12)

plt.suptitle(t="Is the Premier League the highest scoring league\n Compared to other European leagues?  ", fontsize=24, fontweight='bold', color=colors_dark[0])
plt.title("The Premier League is the 3rd highest scoring league among the 5 big leagues. The \nleagues that score more goals are Serie A and Ligue 1", fontsize=13, color=colors_dark[2])
plt.tight_layout()
plt.show()

sorted_data = PL.sort_values(by="Goals",ascending=False)
sorted_data.reset_index(inplace=True)
pl_goal_top = sorted_data.iloc[0:1]
pl_goal_bot = sorted_data.iloc[-1]
mean_score = PL['Goals'].mean()
pl_idx = list(sorted_data.index + 1)

plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.bottom'] = False
plt.rcParams['axes.titlecolor'] = colors_dark[0]
plt.rcParams['axes.labelcolor'] = colors_dark[0]

plt.rcParams['xtick.color'] = colors_dark[0]
plt.rcParams['ytick.color'] = colors_dark[0]
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12

plt.rcParams['legend.edgecolor'] = colors_dark[0]

fig, ax = plt.subplots(figsize=(14, 12))

bars0 = ax.barh(pl_goal_top['Team'], pl_goal_top['Goals'], color=colors_blue[3], alpha=0.6, edgecolor=colors_dark[0])
bars1 = ax.barh(sorted_data['Team'], sorted_data['Goals'], color=colors_dark[3], alpha=0.4, edgecolor=colors_dark[0])
bars2 = ax.barh(pl_goal_bot['Team'], pl_goal_bot['Goals'], color=colors_red[2], alpha=0.6, edgecolor=colors_dark[0])
line  = ax.axvline(mean_score, linestyle='--', color=colors_dark[2])

ax.legend(["Average Goal", "Best Team", "Other Teams" ,"Worst Team"], loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=5, borderpad=1, frameon=False, fontsize=12)
ax.grid(axis='x', alpha=0.3)
ax.set_axisbelow(True)
ax.set_xlabel("Goals", fontsize=14, labelpad=10, fontweight='bold', color=colors_dark[0])
ax.set_ylabel("Teams", fontsize=14, labelpad=10, fontweight='bold', color=colors_dark[0])
xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()

avgl  = ax.text(
    s="Avarage\nGoal: {:.2f}".format(mean_score),
    y=ymax-4,
    x=mean_score+1,
    backgroundcolor=colors_dark[2],
    fontsize=14,
    fontweight='bold',
    rotation=270,
    color='white'
)
for i, bar in enumerate(bars1) :
    x=bar.get_width(),
    y=bar.get_y(),
    if i !=0 and i != 19:
        ax.text(
            s=f"{pl_idx[i]}th",
            va='center', ha='center',
            x=x[0]/2, y=y[0]+0.30,
            color=colors_dark[3],
            fontsize=14,
)

for i, bar in enumerate(bars0):
    x = bar.get_width(),
    y = bar.get_y(),
    ax.text(
        s=f"1st",
        va='center', ha='center',
        x=x[0] / 2, y=y[0] + 0.30,
        color="white",
        fontsize=14,
        fontweight='bold',
        alpha=1,
    )

for i, bar in enumerate(bars2):
    x = bar.get_width(),
    y = bar.get_y(),
    ax.text(
        s=f"20th",
        va='center', ha='center',
        x=x[0] / 2, y=y[0] + 0.30,
        color="white",
        fontsize=14,
        fontweight='bold',
        alpha=1,
    )
plt.text(s="Which team scored the most goals?\n ", ha='left', x=xmin, y=ymax*1.08, fontsize=20, fontweight='bold', color=colors_dark[0])
plt.title("Manchester City were the best with 83 goals for the season.\nSheffield United were the worst team in front of goal with only 20 goals", loc='left', fontsize=10, color=colors_dark[2])
plt.tight_layout()
plt.show()


sorted_data = PL.sort_values(by="Shots pg",ascending=False)
sorted_data.reset_index(inplace=True)
pl_goal_top = sorted_data.iloc[0:1]
pl_goal_bot = sorted_data.iloc[-1]
mean_score = PL['Shots pg'].mean()
pl_idx = list(sorted_data.index + 1)


fig, ax = plt.subplots(figsize=(14,12))

bars0 = ax.barh(pl_goal_top['Team'], pl_goal_top['Shots pg'], color="red", edgecolor=colors_dark[0])
bars1 = ax.barh(sorted_data['Team'], sorted_data['Shots pg'], color=colors_dark[3], alpha=0.4, edgecolor=colors_dark[0])
bars2 = ax.barh(pl_goal_bot['Team'], pl_goal_bot['Shots pg'], color=colors_red[2], alpha=0.6, edgecolor=colors_dark[0])
line  = ax.axvline(mean_score, linestyle='--', color=colors_dark[2])

ax.legend(["Average Shots per Game", "Best Team", "Other Teams" ,"Worst Team"], loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=5, borderpad=1, frameon=False, fontsize=12)
ax.grid(axis='x', alpha=0.3)
ax.set_axisbelow(True)
ax.set_xlabel("Shots Per Game", fontsize=14, labelpad=10, fontweight='bold', color=colors_dark[0])
ax.set_ylabel("Teams", fontsize=14, labelpad=10, fontweight='bold', color=colors_dark[0])
xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()

avgl = ax.text(
    s="Avarage\nShots pg: {:.2f}".format(mean_score),
    y=ymax - 5,
    x=mean_score + 0.2,
    backgroundcolor=colors_dark[2],
    fontsize=14,
    fontweight='bold',
    rotation=270,
    color='white'
)
for i, bar in enumerate(bars1):
    x = bar.get_width(),
    y = bar.get_y(),
    if i != 0 and i != 19:
        ax.text(
            s=f"{pl_idx[i]}th",
            va='center', ha='center',
            x=x[0] / 2, y=y[0] + 0.30,
            color=colors_dark[3],
            fontsize=14,
        )
for i, bar in enumerate(bars0):
    x = bar.get_width(),
    y = bar.get_y(),
    ax.text(
        s=f"1st",
        va='center', ha='center',
        x=x[0] / 2, y=y[0] + 0.30,
        color="white",
        fontsize=14,
        fontweight='bold',
        alpha=1,
    )

for i, bar in enumerate(bars2):
    x = bar.get_width(),
    y = bar.get_y(),
    ax.text(
        s=f"20th",
        va='center', ha='center',
        x=x[0] / 2, y=y[0] + 0.30,
        color="white",
        fontsize=14,
        fontweight='bold',
        alpha=1,
    )

plt.text(s="Which team takes the most shots at goal?", ha='left', x=xmin, y=ymax*1.08, fontsize=20, fontweight='bold', color=colors_dark[0])
plt.title("Liverpool attempt the most shots at goal they have 16 per game.\nThe worst team is again Sheffield United", loc='left', fontsize=10, color=colors_dark[2])
plt.tight_layout()
plt.show()


meanx=df['Possession%'].mean()
meany=df['Pass%'].mean()
epl_3x = df[df["Tournament"]=="Premier League"].sort_values(by=["Possession%"],ascending=False)[["Team","Possession%"]][0:3]
epl_3y = df[df["Tournament"]=="Premier League"].sort_values(by=["Pass%"],ascending=False)[["Team","Pass%"]][0:3]


fig, ax = plt.subplots(figsize=(18, 8), dpi=75)

sns.scatterplot(
    data=df,
    x='Possession%',
    y='Pass%',
    size='Rating',
    ax=ax, sizes=(5, 1000),
    alpha=0.9,
    hue='Tournament',
    palette=[colors_red[2],colors_mix[-2], colors_mix[-1], "red",colors_mix[2]]
)
linex = ax.axvline(meanx, linestyle='dotted', color=colors_dark[1], alpha=0.8, label='Average')
liney = ax.axhline(meany, linestyle='dotted', color=colors_dark[1], alpha=0.8)
text  = ax.text(
    s=epl_3x.Team.iloc[0],
    x=epl_3x["Possession%"].iloc[0]-0.8,
    y=epl_3y["Pass%"].iloc[0]-1.5,
    color=colors_dark[2]
)
text1  = ax.text(
    s=epl_3x.Team.iloc[1],
    x=epl_3x["Possession%"].iloc[1]-0.013,
    y=epl_3y["Pass%"].iloc[1]+0.25,
    color=colors_dark[2]
)
text2  = ax.text(
    s=epl_3x.Team.iloc[2],
    x=epl_3x["Possession%"].iloc[2]-0.05,
    y=epl_3y["Pass%"].iloc[2]-1.5,
    color=colors_dark[2]
)


ax.legend(bbox_to_anchor=(1.05, 1), ncol=1, borderpad=1, frameon=False, fontsize=12)
ax.grid(alpha=0.3)
ax.set_axisbelow(True)
ax.set_xlabel("Possession%", fontsize=14, labelpad=10, fontweight='bold', color=colors_dark[0])
ax.set_ylabel("Pass%", fontsize=14, labelpad=10, fontweight='bold', color=colors_dark[0])
xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()


plt.text(s="How do Premier League teams compare among other European leagues in terms of\n Possession%, Pass% and Rating score?", ha='left', x=xmin, y=ymax*1.04, fontsize=24, fontweight='bold', color=colors_dark[0])
plt.title("3 Premier League teams: Man City,Liverpool and Chelsea are noticably better than other EPL teams.\nAll the other Premier League teams are not having enough possession% and passing%.", loc='left', fontsize=13, color=colors_dark[2])
plt.tight_layout()
plt.show()