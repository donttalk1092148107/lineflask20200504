import numpy as np 
import pandas as pd

df = pd.DataFrame({ 'A' : 1.,
                    'B' : pd.Timestamp('20170102'),
                    'C' : pd.Series(8,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

print('\n1-df\n',df)
print('\n2-df.dtypes\n',df.dtypes)
print('\n3-df.shape\n',df.shape)
print('\n4-len(df)\n',len(df))
print('\n5-df.info()\n',df.info())
print('\n6-df.describe()\n',df.describe())
#count個數 mean平均值 std均方差 min最小值 max最大值 25%(前25%數據平均值)
print('\n7-df.head(2)\n',df.head(2))
print('\n8-df.tail(2)\n',df.tail(2))
print('\n9-df.index\n',df.index)
print('\n10-df.columns\n',df.columns)
print('\n11-df.values\n',df.values)
print('\n12-df.T\n',df.T)
print('\n13-df.sort_index\n',df.sort_index(axis=0, ascending=False))
print('\n14-df.sort_values\n',df.sort_values(by='E'))
print('\n15-df.loc\n',df.loc[0])
print('\n16-df.iloc\n',df.iloc[0:3, 1:2])
print('\n17-df.A > 0\n',df[df.A > 0])