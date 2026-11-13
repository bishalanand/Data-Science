# Import pandas package
import pandas as pd
import numpy as np

def normalize(x, y):
    x_new = ((x - np.mean([x, y])) /
             (max(x, y) - min(x, y)))

    # print(x_new)
    return x_new

def main():
    # create a dictionary with three fields each
    data = {
        'X': [1, 2, 3],
        'Y': [45, 65, 89]}

    # Convert the dictionary into DataFrame
    df = pd.DataFrame(data)
    print("Original DataFrame:\n", df)

    df['X_norm'] = df.apply(lambda row: normalize(row['X'],
                                             row['Y']), axis=1)
    
    df['Y_norm']=df.apply(lambda row:normalize(row['Y'],row['X']),axis=1)

    print('\nNormalized:')
    print(df)

if __name__ == '__main__':
    main()