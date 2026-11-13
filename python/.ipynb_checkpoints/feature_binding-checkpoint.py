import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

df=pd.read_csv('Churn_Modelling.csv')
print(df.head(5))

labela=['0-20','21-40','41-60','above 60']
binse=[0,20,40,60,100]
df.Age.fillna(df['Age'].mean())

df['age_bined']=pd.cut(df.Age,binse,labels=labela,include_lowest=True)
df_feature=df[["Age","age_bined"]]
print(df_feature)
print(df_feature.info())

plt.bar(labela,df['age_bined'].value_counts())
plt.xlabel('years_binding',color='green')
plt.ylabel('counts')
plt.title('Customer Distribution by Age Group', 
          fontsize=16,         # Increase size
          fontweight='bold',   # Make it bold
          color='darkblue')
plt.tight_layout()
plt.show()