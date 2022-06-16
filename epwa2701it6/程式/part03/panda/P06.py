import pandas as pd
nba = pd.read_csv('./nba_P06.csv')
#nba = nba.dropna()
nba = nba.fillna(0)
#nba.sort_values("Name")
#nba.sort_values(by='Name', ascending=False)
print(nba.head(10))