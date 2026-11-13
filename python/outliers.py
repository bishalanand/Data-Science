import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics

def find_outliers(data):
    result=[]
    mean_dat=statistics.mean(data)
    std_devia=statistics.stdev(data)

    cutoff=3*std_devia
    min_value=mean_dat-cutoff
    max_value=mean_dat+cutoff

    for i in data:
        if i>max_value or i<min_value:
            result.append(i)
    return result

df=pd.read_csv('Churn_Modelling.csv')
#print(find_outliers(df['Age']))
#print("\n your length :",len(find_outliers(df['Age'])))
n=len(find_outliers(df['Age']))
l=len(df['Age'])
#print("\n percentage of outliers is",(n*100)/l,"%")
print(df['Age'].skew())
import seaborn as sns
"""sns.kdeplot(df['Age'])
plt.show()"""
df['Transformed_age']=np.log(df['Age'])
print(df['Transformed_age'].skew())
sns.kdeplot(df['Transformed_age'])
plt.show()