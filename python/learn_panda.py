import pandas as pd
import numpy as np
"""df=pd.read_csv('Churn_Modelling.csv')
#print(df)
#print(df.info())
return all imformation about data
#for returning about statisstical data like sum,mean,meadin and all other data
#print(df.describe())
b=df.sort_values('CreditScore',ascending=False)
print(b)"""
lst = [['tom', 'reacher', 25], ['krish', 'pete', 30],
       ['nick', 'wilson', 26], ['juli', 'williams', 22]]

# Create DataFrame
df = pd.DataFrame(lst, columns=['FName', 'LName', 'Age'])
"""list=np.array(df['Age'])
name_list=np.array(df['FName'])
l=pd.DataFrame(list,index=['gi','ba','la','ka'],columns=['Age'])
m=pd.DataFrame(name_list,index=['gi','ba','la','ka'],columns=['Name'])
print(l)
print(m)"""
age_list = np.array(df['Age'])
name_list = np.array(df['FName'])

# Custom index
custom_index = ['gi', 'ba', 'la', 'ka']

# Combine into one DataFrame
combined_df = pd.DataFrame({
    'Name': name_list,
    'Age': age_list
}, index=custom_index)

print(combined_df.isnull())
