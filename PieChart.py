import pandas as pd
import matplotlib.pyplot as plt


def my_autopct(pct):
    return ('%.2f' % pct) if pct > 1.5 else ''

def my_label(pct):
    print(pct)

dataSet = pd.read_json("DataSet.json").loc[:, ["Company", "# Laid Off"]].dropna().groupby("Company", as_index=False).sum()
top50 = dataSet[dataSet["# Laid Off"] > 1500]
others = dataSet[dataSet["# Laid Off"] < 1500]

df_500_1500 = dataSet[(dataSet["# Laid Off"] > 500) & (dataSet["# Laid Off"] < 1500)]
less = dataSet[(dataSet["# Laid Off"] < 500)]

others_sum = int(others["# Laid Off"].sum())

top50 = top50.append({"Company": "Others", "# Laid Off": others_sum}, ignore_index=True)
top50.sort_values(by="# Laid Off", ascending=True, inplace=True)

# df = df.append({'A': i}, ignore_index=True)
# print(top50)

# Data to plot
# labels = top50["Company"]
# sizes = top50["# Laid Off"]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'green', 'blue', 'orange']

# Plot
plt.rcParams['font.size'] = 7.0

plt.figure(0)
plt.pie(others["# Laid Off"], colors=colors,
autopct=my_autopct, startangle=140, rotatelabels=True, labeldistance=1.1, pctdistance=0.8, textprops={'fontsize': 7})

plt.axis('equal')


plt.figure(1)
plt.pie(top50["# Laid Off"], labels=top50["Company"], colors=colors,
autopct=my_autopct, startangle=140, rotatelabels=True, labeldistance=1.1, pctdistance=0.8, textprops={'fontsize': 7})


plt.figure(2)
plt.pie(df_500_1500["# Laid Off"], labels=df_500_1500["Company"], colors=colors,
autopct=my_autopct, startangle=140, rotatelabels=True, labeldistance=1.1, pctdistance=0.8, textprops={'fontsize': 7})


plt.figure(3)
plt.pie(less["# Laid Off"], colors=colors,
autopct=my_autopct, startangle=140, rotatelabels=True, labeldistance=1.1, pctdistance=0.8, textprops={'fontsize': 7})



plt.show()


# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))
# for ax, col in zip(axes.flat, df.columns):
#     ax.pie(df[col], labels=df.index, autopct=my_autopct)
#     ax.set(ylabel='', title=col, aspect='equal')
# fig.tight_layout()

