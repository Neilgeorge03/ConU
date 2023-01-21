import pandas as pd


data = pd.read_json("Dataset/AequitasData.json")

# for columnName in data.columns:
#     # print(f"{columnName}:{data[columnName].unique()}")
#     print(columnName)
    
# print(data.columns)
print(data["Direction"].unique())
print(data["MessageType"].unique())
print(data["Symbol"].unique())
# print(data["OrderPrice"].unique())
print(data["Exchange"].unique())

# print(data["Direction"].unique())



d = {}
# ID -> Key
# items -> Status, Price, Symbol
# Approved -> move to another thing
# Rejected/Cancelled -> remove completely we don't care