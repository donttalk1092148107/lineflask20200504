import numpy as np 
import pandas as pd

dates = pd.date_range('20200401', periods=6)


df0 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD')) 
print(df0)
