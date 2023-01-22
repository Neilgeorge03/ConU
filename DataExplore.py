import pandas as pd
import matplotlib.pyplot as plt
import circlify

df = pd.read_json("Layoffsfyi_Tracker_layoffsfyitracker.2023-1-21.json").loc[:, ["Company", "# Laid Off"]]  
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


data = pd.read_json("/Users/neiljoegeorge/Documents/ConU/Layoffsfyi_Tracker_layoffsfyitracker.2023-1-21.json")    

print(data)

# ID -> Key
# items -> Status, Price, Symbol
# Approved -> move to another thing
# Rejected/Cancelled -> remove completely we don't care


df.plot(kind='bar', stacked=True)
 
# labels for x & y axis
plt.xlabel('Months')
plt.ylabel('Temp ranges in Degree Celsius')
 
# title of plot
plt.title('Monthly Temperatures in a year')
plt.show()