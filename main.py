from mvp_finder import *
from metadata import *

# Test with invalid data
# bb_matches = accumulate_matches(invalid_input_data, BASKETBALL)
# hb_matches = accumulate_matches(invalid_input_data, HANDBALL)


# Test with valid data - Comment below lines and uncomment the above lines in order to test with invalid input data
bb_matches = accumulate_matches(input_data, BASKETBALL)
hb_matches = accumulate_matches(input_data, HANDBALL)

# process basketball matches
for m in bb_matches:
    m = infer_winning_team(m, 'team name', 'scored points')
    m['rating'] = m.apply(lambda row : calculate_basketball_player_rating(row['team name'], 
                                                       row['position'], 
                                                       row['scored points'], 
                                                       row['rebounds'], 
                                                       row['assists'], 
                                                       row['winning team'],
                                                       basketball_rating), axis = 1)

# process handball matches
for m in hb_matches:
    m = infer_winning_team(m, 'team name', 'goals made')
    m['rating'] = m.apply(lambda row : calculate_handball_player_rating(row['team name'], 
                                                       row['position'], 
                                                       row['goals made'], 
                                                       row['goals received'], 
                                                       row['winning team'],
                                                       handball_rating), axis = 1)

# Find max player rating for Basketball matches data
bbmvp = find_max_rating(pd.concat(bb_matches, ignore_index=True), 'player name','rating')
print_mvp(bbmvp, 'player name', 'rating', 'BASKET BALL MVP')

# Find max player rating for Handball matches data
hbmvp = find_max_rating(pd.concat(hb_matches, ignore_index=True), 'player name','rating')
print_mvp(hbmvp, 'player name', 'rating', 'HAND BALL MVP')

# Find overall MVP from both basketball and handball data - Player with highest rating combined Basketball and Handball matches
final_mvp = find_max_rating(pd.concat([bbmvp, hbmvp], ignore_index=True), 'player name','rating')
print_mvp(final_mvp, 'player name', 'rating', 'ALL GAMES MVP')