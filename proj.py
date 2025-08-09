import pandas as pd

df = pd.read_csv('./FantasyPros_Fantasy_Football_Projections_QB.csv')

# print(df.head())

qbs = df[['Player', 'Team', 'TDS', 'TDS.1']]
qbs.rename({'TDS': 'pTDS', 'TDS.1': 'rTDS'}, inplace=True, axis=1)
qbs['PTS'] = qbs['pTDS'] * 3 + qbs['rTDS'] * 6
qbs.sort_values(by='PTS', ascending=False, inplace=True)
qbs.reset_index(inplace=True, drop=True)

replacement_spot = 14
replacement_players = qbs.iloc[replacement_spot-3:replacement_spot+2]
replacement_level = replacement_players['PTS'].mean()

qbs['VORP'] = qbs['PTS'] - replacement_level

elo_values = list(range(1300, 1300 - (len(qbs) * 10), -10))
qbs['ELO'] = elo_values
print(qbs.head(20))

qbs.to_csv('qbs.csv')