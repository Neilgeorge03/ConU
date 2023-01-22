import pandas as pd
import matplotlib.pyplot as plt


def my_autopct(pct):
    return ('%.2f' % pct) if pct > 3 else ''

def my_label(pct):
    print(pct)

dataSet = pd.read_json("DataSet.json").loc[:, ["Company", "# Laid Off"]].[].dropna()
top50 = dataSet[dataSet["# Laid Off"] > 1500].loc[:,["Company", "# Laid Off"]]
others = dataSet[dataSet["# Laid Off"] < 1500].loc[:,["Company", "# Laid Off"]]

others_sum = int(others["# Laid Off"].sum())

top50 = top50.append({"Company": "Others", "# Laid Off": others_sum}, ignore_index=True)

# df = df.append({'A': i}, ignore_index=True)
# print(top50)

# Data to plot
# labels = top50["Company"]
# sizes = top50["# Laid Off"]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'green', 'blue', 'orange']

# Plot
plt.rcParams['font.size'] = 7.0

plt.pie(top50["# Laid Off"], labels=top50["Company"], colors=colors,
autopct=my_autopct, startangle=140, rotatelabels=True, labeldistance=1.1, pctdistance=0.8, textprops={'fontsize': 7})

plt.axis('equal')
plt.show()


# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 6))
# for ax, col in zip(axes.flat, df.columns):
#     ax.pie(df[col], labels=df.index, autopct=my_autopct)
#     ax.set(ylabel='', title=col, aspect='equal')
# fig.tight_layout()

