import pandas as pd

projections = {
  'qb': './FantasyPros_Fantasy_Football_Projections_QB.csv',
  'rb': './FantasyPros_Fantasy_Football_Projections_RB.csv',
  'wr': './FantasyPros_Fantasy_Football_Projections_WR.csv'
}

replacement_levels = {
  'qb': 14,
  'rb': 60,
  'wr': 51
}

rename = {
  'qb': {'TDS': 'pTDS', 'TDS.1': 'rTDS'},
  'rb': {'TDS': 'rTDS', 'TDS.1': 'wTDS'},
  'wr': {'TDS': 'wTDS', 'TDS.1': 'rTDS'},
}

pos = 'wr'

df = pd.read_csv(projections[pos])

# print(df.head())


qbs = df[['Player', 'Team', 'TDS', 'TDS.1']]
qbs.rename(rename[pos], inplace=True, axis=1)
# todo conditional add
# qbs['PTS'] = qbs['pTDS'] * 3 + qbs['rTDS'] * 6 + qbs['wTDS'] * 6
qbs['PTS'] = qbs['rTDS'] * 6 + qbs['wTDS'] * 6
qbs.sort_values(by='PTS', ascending=False, inplace=True)
qbs.reset_index(inplace=True, drop=True)


replacement_spot = replacement_levels[pos]
replacement_gap = 5 if replacement_spot > 20 else 3
replacement_players = qbs.iloc[replacement_spot - replacement_gap : replacement_spot + replacement_gap - 1]
replacement_level = replacement_players['PTS'].mean()

qbs['VORP'] = qbs['PTS'] - replacement_level

# todo calc values
elo_values = list(range(1400, 1400 - (len(qbs) * 10), -10))
qbs['ELO'] = elo_values
print(qbs.head(20))

# todo update if exists

qbs.to_csv(f'{pos}.csv')