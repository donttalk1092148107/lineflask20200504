import numpy as np 
import pandas as pd

teams = ['Web', 'Mobile', 'Data']
nums = [12, 14, 34]
rd_team_dict = {
                'teams': teams,
                'nums': nums
}
rd_team_df = pd.DataFrame(rd_team_dict)

print(rd_team_df)