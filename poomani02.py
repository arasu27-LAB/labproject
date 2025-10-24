#Create a simple pandas DataFrame
import pandas as pd
data={
 "calories":[420,380,390],
 "duration":[50,40,45]
}
#load data into a DataFrame object:
df=pd.DataFrame(data)
print(df)

#locate Row
print(df.loc[0])

#use a list of indexes:
print(df.loc[[0,1]])

#Named Indexes
import pandas as pd
data={
 "calories":[420,380,390],
 "duration":[50,40,45]
}
df=pd.DataFrame(data,index=["day1","day2","day3"])
print(df)

#Locate Named Indexes
print(df.loc["day2"])

#Load Files Into a DataFrame
import pandas as pd
df=pd.read_csv(r'C:\dataframe.csv')
print(df)                                                                                                              

#Check the number of maximum returned rows
import pandas as pd
print(pd.options.display.max_rows)
import pandas as pd
pd.options.display.max_rows=9999
df=pd.read_csv(r'C:\dataframe.csv')
print(df)

#viewing the Data
import pandas as pd
df=pd.read_csv(r'C:\dataframe.csv')
print(df.head(4))

#Print the last 5 rows of the DataFrame
print(df.tail())
print(df.info())
