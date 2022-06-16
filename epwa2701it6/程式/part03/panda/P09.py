import pandas as pd
import numpy as np
fortune = pd.read_csv("./fortune1000_P09.csv",index_col="Rank")
#print(fortune.head(10))
sector = fortune.groupby("Sector")
#print(type(sector))
#print(sector.size())
s1=sector.get_group("Energy")
s2=sector.get_group("Energy").sum()
#print(s2)

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                      'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
print(df)
s3=df.groupby('A').sum()
s4=df.groupby('B').sum()
s5=df.groupby(['A','B']).sum()
print(s3)