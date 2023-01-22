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
less_sum = int(less["# Laid Off"].sum())

top50 = top50.append({"Company": "Others", "# Laid Off": others_sum}, ignore_index=True)
df_500_1500 = df_500_1500.append({"Company": "Others", "# Laid Off": less_sum}, ignore_index=True)
top50.sort_values(by="# Laid Off", ascending=True, inplace=True)
df_500_1500.sort_values(by="# Laid Off", ascending=True, inplace=True)

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red', 'green', 'blue', 'orange']

# Plot
plt.rcParams['font.size'] = 7.0


plt.axis('equal')


plt.figure(0)
plt.pie(top50["# Laid Off"], labels=top50["Company"], colors=colors,
autopct=my_autopct, startangle=140, rotatelabels=True, labeldistance=1.1, pctdistance=0.8, textprops={'fontsize': 7})
plt.savefig("ConU_FrontEnd/src/img/Companies with more than 1500 layoffs.png", dpi=300, bbox_inches='tight')
plt.figure(1)
plt.pie(df_500_1500["# Laid Off"], labels=df_500_1500["Company"], colors=colors,
autopct=my_autopct, startangle=140, rotatelabels=True, labeldistance=1.1, pctdistance=0.8, textprops={'fontsize': 7})
plt.savefig("ConU_FrontEnd/src/img/Companies with 500 to 1500 layoffs.png", dpi=300, bbox_inches='tight')

plt.figure(2)
plt.pie(less["# Laid Off"], colors=colors,
autopct=my_autopct, startangle=140, rotatelabels=True, labeldistance=1.1, pctdistance=0.8, textprops={'fontsize': 7})
plt.savefig("ConU_FrontEnd/src/img/Companies with less than 500 layoffs.png", dpi=300, bbox_inches='tight')