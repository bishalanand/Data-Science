import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics
import seaborn as sns

df=pd.read_csv('Churn_Modelling.csv')
sns.boxplot(data=df)
plt.show()