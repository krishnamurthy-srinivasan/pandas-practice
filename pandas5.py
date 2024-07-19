#Apply, Map and  ApplyMap Operations on DataFrame

import pandas as pd

nyc_jobs = pd.read_csv(r"C:\Users\Admin\Desktop\Work\Python-for-DataEngineering\Code\Practice\pandas\NYC_Jobs.csv")

print(nyc_jobs)
print(nyc_jobs["Civil Service Title"])
#Apply - used on both dataframes and series. function passed works on rows/cloumns. 
nyc_jobs["Civil Service Title"] =nyc_jobs["Civil Service Title"].apply(lambda x: x.capitalize())
print(nyc_jobs["Civil Service Title"])