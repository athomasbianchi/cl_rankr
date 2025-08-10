import pandas as pd
import random

def calculate_elo_change(player_rating, opponent_rating,actual_score):
    # Calculate expected score
    expected_score = 1 / (1 + 10**((opponent_rating - player_rating) / 400))

    # Calculate rating change
    rating_change = 32 * (actual_score - expected_score)

    return rating_change

def main():
  qbs = pd.read_csv('./qb.csv', index_col=0)
  rbs = pd.read_csv('./rb.csv', index_col=0)
  # wrs = pd.read_csv('./wr.csv', index_col=0)
  qb_elo_i = qbs.columns.get_loc('ELO')
  rb_elo_i = rbs.columns.get_loc('ELO')
  # wr_elo_i = rbs.columns.get_loc('ELO')
  ranking = True
  count = 0
  round = 1
  while ranking:
    print('Ranks Count: ', count)
    q_i = random.randint(0,5)
    r_i = random.randint(0,20)
    w_i = random.randint(0,20)

    qbs = qbs.sort_values(by=['ELO', 'VORP'], ascending=[False, False]).reset_index(drop=True)
    rbs = rbs.sort_values(by=['ELO', 'VORP'], ascending=[False, False]).reset_index(drop=True)
    # wrs = wrs.sort_values(by=['ELO', 'VORP'], ascending=[False, False]).reset_index(drop=True)

    print(qbs.head(5))
    print(rbs.head(20))
    # print(wrs.head(20))

    q_rating = qbs.iloc[q_i]['ELO']
    r_rating = rbs.iloc[r_i]['ELO']
    # w_rating = wrs.iloc[w_i]['ELO']

    print(qbs.iloc[[q_i]])
    print(rbs.iloc[[r_i]])
    resp = input('Who do you prefer?')
    if resp == '1':
      q_diff = calculate_elo_change(q_rating, r_rating, 1)
      r_diff = calculate_elo_change(r_rating, q_rating, 0)
      new_q = q_rating + q_diff
      new_r = r_rating + r_diff
      print('new ranks')
      print(qbs.iloc[q_i]['Player'] + ': ', new_q)
      print(rbs.iloc[r_i]['Player'] + ': ', new_r)
      qbs.iat[q_i, qb_elo_i] = new_q
      rbs.iat[r_i, rb_elo_i] = new_r
      count += 1
    if resp == '2':
      q_diff = calculate_elo_change(q_rating, r_rating, 0)
      r_diff = calculate_elo_change(r_rating, q_rating, 1)
      new_q = q_rating + q_diff
      new_r = r_rating + r_diff
      print('new ranks')
      print(qbs.iloc[q_i]['Player'] + ': ', new_q)
      print(rbs.iloc[r_i]['Player'] + ': ', new_r)
      qbs.iat[q_i, qb_elo_i] = new_q
      rbs.iat[r_i, rb_elo_i] = new_r
      count += 1
    if resp == 'x':
      ranking = False
      qbs.to_csv('qb.csv')
      rbs.to_csv('rb.csv')
main()