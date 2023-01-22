import pandas as pd
import seaborn as sb
import squarify
import matplotlib.pyplot as plt

data = pd.read_json("DataSet.json")
df = data[["Date","Company", "# Laid Off"]].copy()
# labels = ['AB', 'A', 'ABC', 'ABCD']
# sizes = [500, 250, 120, 60]
# color = ['red', 'green', 'blue', 'orange']

# squarify.plot(data["# Laid Off"], label = data["Company"], pad = True)
# plt.axis('off')
# plt.show()


df.plot(kind='bar', stacked=True)
 
# labels for x & y axis
plt.xlabel('Months')
plt.ylabel('Temp ranges in Degree Celsius')
 
# title of plot
plt.title('Monthly Temperatures in a year')
plt.show()