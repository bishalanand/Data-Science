import pandas as pd
import numpy as np

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)

# select all rows 
# and second to fourth column
df["Age"]+=10
print(df["Age"].iloc[0:3])
print(df.loc[:,["Age","Qualification"]])
data2=pd.read_csv("Churn_Modelling.csv",index_col="Geography")
data3=data2.loc[["France","Germany"],["Age","Tenure","Surname"]]
data3.rename(columns={'Tenure':'Time_period'},inplace=True)
print(data3)
data3.loc[(data3['Age']==42) & (data3['Time_period']==8),'Age']=45
print(data3[(data3['Age'] == 45) & (data3['Time_period'] == 8)])
print(data3)
