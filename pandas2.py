#Handling missing data 
from numpy import nan
from pandas import Timestamp
import pandas as pd
df = pd.read_csv(r"C:\Users\Admin\Desktop\Work\Python-for-DataEngineering\Code\Practice\pandas\pandas2.csv", parse_dates=["day"])

print(df)

#Changing the day as index

df.set_index("day", inplace=True)

#it is often better to replace the NaN with some Meaningful values
modified_df = df.fillna(0)
print(modified_df)

#Here the event is also replaced with 0 which doesnt makesense, so to replace meaningful values for different columns
#we need to pass dictionary

modified_df1 = df.fillna({"temperature": 0, "windspeed": 0, "event": "No Event Recorded"})
print(modified_df1)

#replacing with 0 doesnt make sense in these cases where mean of temperature and windspeed could produce erred data
#in those cases we could use ffill and bfill which completes the missing value with previous/next value

modified_df2 = df.fillna(method = "bfill") #or df.fillna(method="ffill")
print(modified_df2)

#We can use axis 0 or 1 to fill it by next column data and "limit" arg to limit no of missing values that can
#be filled maximum contigously

#Still this is just like assuming the values randomly, we could use interpolation method of pandas
#to give more meaning to the missing value
modified_df3 = df.interpolate(method="time").fillna({"event":"No Event"})
print(modified_df3)

#Sometimes we just need to drop the rows with Na values

modified_df4 = df.dropna()
print(modified_df4)

#can conditions like if every column is na then drop the row with "how" arg or can give threshold with "thresh" arg

modified_df5 = df.dropna(how="all")
print(modified_df5)

modified_df6 = df.dropna(thresh=2  )
print(modified_df6)

# print(df.to_dict())

# df_dict = {'temperature': {Timestamp('2024-01-01 00:00:00'): 32.0, Timestamp('2024-02-01 00:00:00'): nan, Timestamp('2024-03-01 00:00:00'): 28.0, Timestamp('2024-04-01 00:00:00'): 25.0, Timestamp('2024-05-01 00:00:00'): 29.0, Timestamp('2024-06-01 00:00:00'): 30.0}, 'windspeed': {Timestamp('2024-01-01 00:00:00'): 7.0, Timestamp('2024-02-01 00:00:00'): 6.0, Timestamp('2024-03-01 00:00:00'): 4.0, Timestamp('2024-04-01 00:00:00'): 5.0, Timestamp('2024-05-01 00:00:00'): 5.0, Timestamp('2024-06-01 00:00:00'): nan}, 'event': {Timestamp('2024-01-01 00:00:00'): 'Rain', Timestamp('2024-02-01 00:00:00'): 'Sunny', Timestamp('2024-03-01 00:00:00'): 'Snow', Timestamp('2024-04-01 00:00:00'): 'Rain', Timestamp('2024-05-01 00:00:00'): nan, Timestamp('2024-06-01 00:00:00'): 'Sunny'}}

print("#####################################################################################")

#Using replace to handle values
df.fillna({'temperature': -99999, "windspeed": -99999, "event": "No Event"}, inplace=True)
print(df)
modified_df7 = df.replace({"temperature" : -99999, "windspeed" : -99999, "event":"No Event"}, nan)

print(modified_df7)