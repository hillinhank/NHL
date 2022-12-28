import pyreadr
import numpy as np

rosters = pyreadr.read_r('2021-11-11_rosters.rds')
df_rosters=rosters[None]
df_rosters


teams = pyreadr.read_r('2021-11-11_teams.rds')
df_teams=teams[None]
df_teams

players = pyreadr.read_r('2021-11-12_players.rds')
df_players=players[None]
df_players

