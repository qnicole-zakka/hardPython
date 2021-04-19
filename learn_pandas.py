import numpy as np
import pandas as pd

# True copy of dataframes
# One way to initiate dataframe
cols2 = ['Eleanor', 'Chidi', 'Tahani', 'Jason']
d2 = np.random.randint(0, 100, (3, 4))
df2 = pd.DataFrame(data=d2, columns=cols2)
print(df2)

# a first view of DataFrame
df2.head()
df2.describe()

print(df2['Eleanor'][1])
dft = df2 # reference 
dftt = df2.copy() # true copy
df2['Eleanor'][1] *= 2  # modify a cell
# observe the cell changes in the original, referenced copy and true copy
print(df2['Eleanor'][1]) 
print(dft['Eleanor'][1])
print(dftt['Eleanor'][1])

# shuffle rows
shuffled_df = df.reindex(np.random.permutation(df.index))

# calculate z-score for all elements in the dataframe
df_mean = df.mean() # mean of all columns
df_std = df.std()
df_zscore = (df - df_mean) / df_std

# group by multiple conditions and get the count of each condition match
df.groupby(['cond1', 'cond2']).size()
