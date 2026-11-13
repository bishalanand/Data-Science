import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Churn_Modelling.csv')
#print(df.info())

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

new_df=df[['Age','Tenure']] #or we can use new_df=pd.Dataframe(df,columns=["Age","Tenure"])
#print(new_df.info())

"""if there is null value fill it with mean median mode"""
#feature scaling 1)normalization

scaler=MinMaxScaler()
normalized_df=scaler.fit_transform(new_df)
print(normalized_df)
scaler2=StandardScaler()
scalrized_df=scaler2.fit_transform(new_df)
scalrized_df = pd.DataFrame(scalrized_df, columns=new_df.columns)
print("your scalized df is \n",scalrized_df['Age'])