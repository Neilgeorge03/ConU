import pandas as pd


data = pd.read_json("/Users/neiljoegeorge/Documents/ConU/Layoffsfyi_Tracker_layoffsfyitracker.2023-1-21.json")    

print(data)

# ID -> Key
# items -> Status, Price, Symbol
# Approved -> move to another thing
# Rejected/Cancelled -> remove completely we don't care



