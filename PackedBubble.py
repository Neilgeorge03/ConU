import pandas as pd
import matplotlib.pyplot as plt
import circlify
from distinctipy import distinctipy

# number of colours to generate

data = pd.read_json("DataSet.json").loc[:, ["Company", "# Laid Off", "Industry"]]
colorDict = dict(zip(data["Industry"].unique(), distinctipy.get_colors(len(data["Industry"].unique()))))
df = pd.read_json("DataSet.json").loc[:, ["Company", "# Laid Off", "Industry"]]  
df["Color"] = df["Industry"].map(colorDict)
df = df.groupby("Company", as_index=False).agg({"# Laid Off": "sum", "Industry": "first", "Color": "first"})
df.sort_values(by="# Laid Off", ascending=False, inplace=True)
top_50 = df.head(50)
layoffs = top_50["# Laid Off"].tolist()

circles = circlify.circlify(
    layoffs,
    show_enclosure=True,
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

fig, ax = plt.subplots(figsize=(20,20))



ax.axis('off')

lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r,
    )
    for circle in circles
)

plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

labels = top_50["Company"].iloc[::-1] # have to reverse to get the order right 

for circle, label, colorCode in zip(circles, labels, top_50["Color"].iloc[::-1]):
    x, y, r = circle
    ax.add_patch(plt.Circle((x,y), r, alpha=0.2, linewidth=2, fill=False, color=colorCode))
    plt.annotate(
        label,
        (x,y),
        va="center",
        ha="center"
    )

plt.legend(colorDict, loc="upper left", ncol=10)

plt.savefig("ConU_FrontEnd/src/img/PackedBubbleChart.png", dpi=300, bbox_inches='tight')