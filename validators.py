import re
from metadata import *

# Validates if the game type in match data belongs to supported games 
def is_first_line_valid_game_type(line):
    return line in game_types

# Validates if the data is in proper format and also according to the known format for each game type
# Checks if each line is a valid csv and has correct number of columns as per the format specified in metadata
def is_csv_valid(game_type, lines):
    return all([is_csv_line_valid(line, len(COLUMN_FORMAT[game_type])) for line in lines])

# Generic method to check if a given string is a valid CSV and has correct number of columns as per the valid_length criteria
# Uses a regular expression to check for the valid csv formatting
def is_csv_line_valid(line, valid_length, separator=';'):
    r = re.compile(r'''
        \s*                # Any whitespace.
        (                  # Start capturing here.
          [^{0}"']+?         # Either a series of non-comma non-quote characters.
          |                # OR
          "(?:             # A double-quote followed by a string of characters...
              [^"\\]|\\.   # That are either non-quotes or escaped...
           )*              # ...repeated any number of times.
          "                # Followed by a closing double-quote.
          |                # OR
          '(?:[^'\\]|\\.)*'# Same as above, for single quotes.
        )                  # Done capturing.
        \s*                # Allow arbitrary space before the comma.
        (?:{0}|$)            # Followed by a comma or the end of a string.
        '''.format(separator), re.VERBOSE)
    return len(r.findall(line)) == valid_length

# Main validator method that takes the raw data read from source and validates using above methods
# Returns tuple: is_valid (boolean), message (str)
def is_match_data_valid(match_data):
    # split into a list of strings - lines from input match data
    lines = match_data.split('\n')
    
    # check if there is any data 
    if (len(lines) <= 0 ):
        return False, "No data available to process"
    
    # Game type - First line is always the game type
    header = lines[0]
    
    # Should fail if the first line is not a supported game type
    if not is_first_line_valid_game_type(header):
        return False, "Game is not supported"
    
    # Should fail if there are no player stats for the match
    if (len(lines) <= 1):
        return False, "Not enough data"
    
    # Extract the remaining lines - player stats
    player_stats = lines[1:]
    
    # Check if the lines are valid CSV and contain the correct information columns
    if not is_csv_valid(header, player_stats):
        return False, "Match stats are not following valid {} game stats format".format(header)
    
    # If all conditions pass, assume data is valid
    return True, "Data is valid"
