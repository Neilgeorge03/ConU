import pandas as pd
import matplotlib.pyplot as plt
import circlify

df = pd.read_json("DataSet.json").loc[:, ["Company", "# Laid Off"]]  
df = df.groupby("Company", as_index=False).sum()
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

labels = top_50["Company"]

for circle, label in zip(circles, labels):
    x, y, r = circle
    ax.add_patch(plt.Circle((x,y), r, alpha=0.2, linewidth=2, fill=False))
    plt.annotate(
        label,
        (x,y),
        va="center",
        ha="center"
    )

plt.show()

# ID -> Key
# items -> Status, Price, Symbol
# Approved -> move to another thing
# Rejected/Cancelled -> remove completely we don't care

