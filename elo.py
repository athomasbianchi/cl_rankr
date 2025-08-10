import pandas as pd
import random

POS = 'wr'

def calculate_elo_change(player_rating, opponent_rating,actual_score):
    # Calculate expected score
    expected_score = 1 / (1 + 10**((opponent_rating - player_rating) / 400))

    # Calculate rating change
    rating_change = 32 * (actual_score - expected_score)

    return rating_change

def main():
  qbs = pd.read_csv(f'./{POS}.csv', index_col=0)
  elo_i = qbs.columns.get_loc('ELO')
  ranking = True
  count = 0
  while ranking:
    print('Ranks Count: ', count)
    range = random.randint(1,10)
    i = random.randint(0,range*8)
    j = i + random.randint(1,5)
    qbs = qbs.sort_values(by=['ELO', 'VORP'], ascending=[False, False]).reset_index(drop=True)

    i_rating = qbs.iloc[i]['ELO']
    j_rating = qbs.iloc[j]['ELO']

    print(qbs.iloc[[i,j]])
    resp = input('Who do you prefer?')
    if resp == '1':
      i_diff = calculate_elo_change(i_rating, j_rating, 1)
      j_diff = calculate_elo_change(j_rating, i_rating, 0)
      new_i = i_rating + i_diff
      new_j = j_rating + j_diff
      print('new ranks')
      print(qbs.iloc[i]['Player'] + ': ', new_i)
      print(qbs.iloc[j]['Player'] + ': ', new_j)
      qbs.iat[i, elo_i] = new_i
      qbs.iat[j, elo_i] = new_j
      count += 1
    if resp == '2':
      i_diff = calculate_elo_change(i_rating, j_rating, 0)
      j_diff = calculate_elo_change(j_rating, i_rating, 1)
      new_i = i_rating + i_diff
      new_j = j_rating + j_diff
      print(qbs.iloc[i]['Player'] + ': ', new_i)
      print(qbs.iloc[j]['Player'] + ': ', new_j)
      qbs.iat[i, elo_i] = new_i
      qbs.iat[j, elo_i] = new_j
      count += 1
    if resp == 'x':
      ranking = False
      qbs.to_csv(f'{POS}.csv')
main()