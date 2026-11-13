import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""lst = [['tom', 'reacher', 25], ['krish', 'pete', 30],
       ['nick', 'wilson', 26], ['juli', 'williams', 22]]

# Create DataFrame
df = pd.DataFrame(lst, columns=['FName', 'LName', 'Age'])
print(df['age'])

df.plot(x='key', y='value',kind='line')
df.plot(x='key', y='value',kind='area')
plt.show()"""

#x_point=np.array([0,3,4,4,3,6,7,9])
y_point=np.array([6,9,2,3,5,6,6,0])
plt.plot(y_point)
plt.show()