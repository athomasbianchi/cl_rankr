import pandas as pd
import random



def calculate_elo_change(player_rating, opponent_rating,actual_score):
    # Calculate expected score
    expected_score = 1 / (1 + 10**((opponent_rating - player_rating) / 400))

    # Calculate rating change
    rating_change = 32 * (actual_score - expected_score)

    return rating_change


def main():
  qbs = pd.read_csv('./qbs.csv', index_col=0)
  elo_i = qbs.columns.get_loc('ELO')
  ranking = True
  while ranking:
    count = 0
    i = random.randint(0,39)
    j = i + random.randint(1,3)
    qbs = qbs.sort_values(by=['ELO', 'VORP'], ascending=[False, False]).reset_index(drop=True)
    print(qbs.head())
    print('Player 1')
    print(qbs.iloc[i])
    i_rating = qbs.iloc[i]['ELO']
    j_rating = qbs.iloc[j]['ELO']
    print('Player 2')
    print(qbs.iloc[j])
    resp = input('Who do you prefer?')
    if resp == '1':
      print('You prefer')
      print(qbs.iloc[i]['Player'])
      i_diff = calculate_elo_change(i_rating, j_rating, 1)
      j_diff = calculate_elo_change(j_rating, i_rating, 0)
      new_i = i_rating + i_diff
      new_j = j_rating + j_diff
      print('new ranks')
      print(qbs.iloc[i]['Player'] + ': ', new_i)
      print(qbs.iloc[j]['Player'] + ': ', new_j)
      qbs.iat[i, elo_i] = new_i
      qbs.iat[j, elo_i] = new_j
    if resp == '2':
      print('You prefer')
      print(qbs.iloc[j]['Player'])
      i_diff = calculate_elo_change(i_rating, j_rating, 0)
      j_diff = calculate_elo_change(j_rating, i_rating, 1)
      new_i = i_rating + i_diff
      new_j = j_rating + j_diff
      print(qbs.iloc[i]['Player'] + ': ', new_i)
      print(qbs.iloc[j]['Player'] + ': ', new_j)
      qbs.iat[i, elo_i] = new_i
      qbs.iat[j, elo_i] = new_j

    if resp == 'x':
      ranking = False


main()