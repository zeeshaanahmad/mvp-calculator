import pandas as pd
from metadata import *
from validators import *

# read from input data, validate and structure the data for further calculations
def accumulate_matches(data, game_type):
    match_stats = []
    for i in range(len(data)):
        
        # validate input data
        is_valid, msg = is_match_data_valid(data[i])
        
        # raise exception if data is not valid. MVP Calculation should fail
        if not is_valid:
            raise Exception("MVP Calculation Failed.\nError: {}".format(msg))
        
        lines = input_data[i].split('\n')
        players_data = [row.split(';') for row in lines[1:]]
        if game_type == lines[0]:
            # creating a pandas data frame to hold match data
            df = pd.DataFrame(players_data, columns=COLUMN_FORMAT[game_type])
            
            # converting columns with numerical values to integer for calculation
            df[INT_COLUMNS[game_type]] = df[INT_COLUMNS[game_type]].astype(int)
            
            # keeping a list of all match data frames for later calculations
            match_stats.append(df)
    return match_stats

# Find winning team for the match 
# For basketball matches => maximum total scored points
# For handball matches => maximum total goals scored by the team 
def infer_winning_team(df, team_col, score_col):
    z = df.groupby(team_col)[score_col].sum().reset_index()
    df['winning team'] = z.loc[z[score_col].idxmax()][team_col]
    return df

# Calculates rating based on the rating lookup provided for each position for basketball games
# Players from winning team get 10 extra points
def calculate_basketball_player_rating(team_name, position, scored_points, rebounds, assists, winning_team, rating_lookup):
    rating = scored_points * rating_lookup[position]['scored_points'] + rebounds * rating_lookup[position]['rebounds'] + assists * rating_lookup[position]['assists']
    if team_name == winning_team:
        rating += 10
    return rating

# Calculates rating based on the rating lookup provided for each position for handball games
# Players from winning team get 10 extra points
def calculate_handball_player_rating(team_name, position, goals_made, goals_recieved, winning_team, rating_lookup):
    rating = rating_lookup[position]['initial_rating'] + goals_made * rating_lookup[position]['goals_made'] + goals_recieved * rating_lookup[position]['goals_recieved']
    if team_name == winning_team:
        rating += 10
    return rating

# Find player with maximum value of rating column in a given data frame
def find_max_rating(df, player_col, rating_col):
    x = df.groupby(player_col)[rating_col].sum().reset_index()
    return x[x[rating_col] == x[rating_col].max()]

# Handles printing results on terminal
# Also accounts for tied MVP situations where more than one players have same rating points
def print_mvp(df, player_col, rating_col, heading):
    print('{0}\n{1}'.format(heading,  '-'*len(heading)))
    if (len(df) > 1):
        print("MVP title is Tied between", ', '.join(df[player_col].tolist()), 'with', df[rating_col].tolist()[0], 'points each.')
    elif (len(df) == 1):
        print("MVP is", ', '.join(df[player_col].tolist()), 'with', df[rating_col].tolist()[0], 'points.')
    print("\n")