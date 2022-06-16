import pandas as pd
import numpy as np
employees = pd.read_csv('./employees_P08.csv')
employees["Gender"] == "Male"
s1=employees["Gender"] == "Male"
s2=employees['Team'] != "Finance"
s3=employees["Salary"] > 148941
s4=employees[employees["Salary"] > 148941]
s5=employees["Start Date"] <= "1980-05-01"
mask1 = employees["Team"] != "Marketing"
mask2 = employees["Start Date"] < "1980-01-01"
s6=employees[(mask1 & mask2)] 
s7=employees[(mask1 | mask2)]
s8=employees["Team"].isin(["Legal","Scales","Product"])
s9=employees["Team"].isnull()
s10=employees["Team"].notnull()
print(s10)


