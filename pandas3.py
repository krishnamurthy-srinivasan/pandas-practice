import pandas as pd
import matplotlib_inline
df = pd.read_csv(r"C:\Users\Admin\Desktop\Work\Python-for-DataEngineering\Code\Practice\pandas\pandas3.csv")
print(df)

groups = df.groupby("city")

for city, group in groups:
    print("City: ", city)
    print("Group DF: ")
    print(group)

#Applying aggregation function on groups - SPLIT - APPLY - COMBINE

print("Maximum stats for each cities: ")
print(df.groupby("city").max())

#To print all stats for the group

print(df.groupby("city").describe())
