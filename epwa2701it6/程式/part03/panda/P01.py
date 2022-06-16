import numpy as np 
import pandas as pd
s1 = pd.Series([1, 3, 5, np.nan, 6, 8])
s2 = pd.Series(np.random.randint(10, size=[3]))


print(s1)
print(s2)