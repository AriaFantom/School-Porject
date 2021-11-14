import pandas as pd
import numpy as np

a = np.array([1, 3, 4, 7, 8, 8, 9])
df = pd.Series(a)
print(df)
s = df.quantile(q=0.75)
print('------75th Percentile is------')
print(s)
print('------Element above 75th Percentile------')
print(df[df>s])