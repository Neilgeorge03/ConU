import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


import pandas as pd
import numpy as np
import spacy
from spacy import displacy
import networkx as nx
import itertools
import matplotlib.pyplot as plt

df = pd.read_csv("DS.csv").loc[:, ["Actors", "Director"]]

new_df = pd.DataFrame(columns=["Actor_A", "Actor_B"])
for index, row in df.iterrows():
    if type(row["Actors"]) == str:
        ls = tuple((row["Actors"].split(",")))
        for element in itertools.permutations(ls, 2):
            new_df = new_df.append({"Actor_A": element[0].strip(), "Actor_B": element[1].strip()}, ignore_index=True)
    else:
        df.loc[index, "Actors"] = []

new_df = pd.DataFrame(np.sort(new_df.values, axis = 1), columns = new_df.columns)

new_df["value"] = 1
new_df = new_df.groupby(["Actor_A","Actor_B"], sort=False, as_index=False).sum()
more_than_2 = new_df[new_df["value"] > 2].copy()
more_than_4 = new_df[new_df["value"] > 4].copy()
more_than_6 = new_df[new_df["value"] > 6].copy()


plt.figure(0, figsize=(50,50))
r_graph = nx.from_pandas_edgelist(new_df,
                            source = "Actor_A",
                            target = "Actor_B",
                            edge_attr = "value",
                            create_using = nx.Graph())
pos = nx.kamada_kawai_layout(r_graph)
nx.draw(r_graph, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
plt.savefig("ConU_FrontEnd/src/img/Relationships.png", dpi=300, bbox_inches='tight')


plt.figure(1, figsize=(50,50))
r_graph = nx.from_pandas_edgelist(more_than_2,
                            source = "Actor_A",
                            target = "Actor_B",
                            edge_attr = "value",
                            create_using = nx.Graph())


pos = nx.kamada_kawai_layout(r_graph)
nx.draw(r_graph, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
plt.savefig("ConU_FrontEnd/src/img/Relationships_more_than_2.png", dpi=300, bbox_inches='tight')

plt.figure(2, figsize=(50,50))
r_graph = nx.from_pandas_edgelist(more_than_4,
                            source = "Actor_A",
                            target = "Actor_B",
                            edge_attr = "value",
                            create_using = nx.Graph())


pos = nx.kamada_kawai_layout(r_graph)
nx.draw(r_graph, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
plt.savefig("ConU_FrontEnd/src/img/Relationships_more_than_4.png", dpi=300, bbox_inches='tight')

plt.figure(3, figsize=(50,50))
r_graph = nx.from_pandas_edgelist(more_than_6,
                            source = "Actor_A",
                            target = "Actor_B",
                            edge_attr = "value",
                            create_using = nx.Graph())


pos = nx.kamada_kawai_layout(r_graph)
nx.draw(r_graph, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos = pos)
plt.savefig("ConU_FrontEnd/src/img/Relationships_more_than_6.png", dpi=300, bbox_inches='tight')

