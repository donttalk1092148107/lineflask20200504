import pandas as pd
import numpy as np
seriesObj = pd.Series(range(10),index=['a', 'a', 'b', 'b', 'b','c','c','c','c','c'])
print(seriesObj)
print(seriesObj['c'])

df = pd.DataFrame(np.random.randn(4,2),index=['a', 'a', 'b', 'b'])
print(df)
print(df[1])
print(df[2:6][1])

#print(df.loc[:,[0,1]])
#print(df.loc['b'])
#print(df.loc['a',1])
print(df.iloc[0])