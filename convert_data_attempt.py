import pyreadr
import pandas as pd
result = pyreadr.read_w("/Users/user/data/NHL/Data/2021-11-11_rosters.rds") # also works for RData
teams = pyreadr.read_r('/Users/user/data/NHL/Data/2021-11-11_teams.rds')
players = teams = pyreadr.read_r('/Users/user/data/NHL/Data/2021-11-12_players.rds')

# done! let's see what we got
print(result.keys())
df1 = result["df1"]