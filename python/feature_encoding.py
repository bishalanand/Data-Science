import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing

df=pd.read_csv('Churn_Modelling.csv')
#print(df.head(5))
df.drop(columns=['RowNumber','CustomerId','Surname'],axis=1,inplace=True)
#print(df.info())
#print(df['Gender'].value_counts())

#label enx=coding

le=preprocessing.LabelEncoder()
df['gender_encoder']=le.fit_transform(df.Gender.values)
print(df.gender_encoder.value_counts())

#one-hot encoding technique

print(df.Geography.value_counts())
df.drop(columns='gender_encoder',axis=1,inplace=True)
on_label=pd.get_dummies(df)
print(on_label)

#target encoding

