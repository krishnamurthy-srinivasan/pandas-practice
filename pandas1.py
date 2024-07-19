import pandas as pd
df = pd.read_csv(r"C:\Users\Admin\Desktop\Work\Python-for-DataEngineering\Code\Practice\pandas\pandas1.csv")
print(df)

#creating pandas df using dictionary
print("creating pandas df using dictionary")
weather_data = {
    "day":['01-01-2024',
'02-01-2024',
'03-01-2024',
'04-01-2024',
'05-01-2024',
'06-01-2024'] ,
'temperature' : [32,35,28,25,29,30],
'windspeed' :[7,6,4,5,2,5],
'event' : ["Rain", "Sunny", "Snow", "Rain", "Sunny", "Sunny"]
}

using_dict_df = pd.DataFrame(weather_data)

print(using_dict_df)


#Finding number of Rows and Columns

print("Finding number of Rows and Columns")
Rows, Columns  = df.shape

print(f"Rows : {Rows}, Columns: {Columns}")

#Find first N rows and last N rows

print("Find first N rows and last N rows")
print("First 3 rows: ")
print(df.head(3))
print("Last 3 rows: ")
print(df.tail(3))

print("Colunms")

print(df.columns)

#Accessing particular column
print(df.day) #or 
# print(df["day"])

#accessing few columms
print(df[["day", "event"]])

#See all the statistics for numerical values in DF

print(df.describe())

#for particular stat
print("maximum temperature: ", df["temperature"].max())

####################################################################

print("####################################################################")

#Conditional Select on dataframe or filtering based on condition

print("Temperature greater than 30")
print(df[df["temperature"]>30])

print("Maximum Temperature recorded day")
print(df[["day", "temperature"]][df["temperature"] == df["temperature"].max()])

#Changin the index of the df 

print(df.set_index('day'))

#if you have to modify the original df add the argument inplace=True 
df.set_index('day', inplace=True) 
print(df.loc['03-01-2024'])