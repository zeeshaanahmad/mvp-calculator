BASKETBALL = 'BASKETBALL'
HANDBALL = 'HANDBALL'

game_types = [BASKETBALL, HANDBALL]

basketball_rating = {
    'G': {
        'scored_points': 2,
        'rebounds': 3,
        'assists': 1
    },
    'F': {
        'scored_points': 2,
        'rebounds': 2,
        'assists': 2
    },
    'C': {
        'scored_points': 2,
        'rebounds': 1,
        'assists': 3
    }
}

handball_rating = {
    'G': {
        'initial_rating': 50,
        'goals_made': 5,
        'goals_recieved': -2
    },
    'F': {
        'initial_rating': 20,
        'goals_made': 1,
        'goals_recieved': -1
    }
}

COLUMN_FORMAT = {
    'BASKETBALL': 'player name;nickname;number;team name;position;scored points;rebounds;assists'.split(';'),
    'HANDBALL': 'player name;nickname;number;team name;position;goals made;goals received'.split(';')
}

INT_COLUMNS = {
    'BASKETBALL': ['scored points', 'rebounds', 'assists'],
    'HANDBALL': ['goals made', 'goals received']
}

input_data = [
    """BASKETBALL
player 1;nick1;4;Team A;G;10;2;7
player 2;nick2;8;Team A;F;0;10;0
player 3;nick3;15;Team A;C;15;10;4
player 4;nick4;16;Team B;G;20;0;0
player 5;nick5;23;Team B;F;4;7;7
player 6;nick6;42;Team B;C;8;10;0""",
    """BASKETBALL
player 7;nick7;3;Team C;C;5;3;1
player 8;nick8;7;Team C;C;10;1;5
player 9;nick9;11;Team C;G;9;9;3
player 10;nick10;25;Team D;F;7;0;8
player 11;nick11;18;Team D;G;2;4;0
player 6;nick6;10;Team D;C;8;11;1""",
    """BASKETBALL
player 5;nick5;2;Team E;C;8;6;9
player 6;nick6;87;Team E;C;7;9;1
player 7;nick7;50;Team E;G;12;4;2
player 10;nick10;26;Team A;G;13;8;6
player 15;nick15;37;Team A;F;1;7;2
player 17;nick17;19;Team A;G;16;0;1""",
    """BASKETBALL
player 55;nick55;98;Team X;F;0;1;10
player 4;nick4;78;Team X;C;4;1;20
player 7;nick7;75;Team X;G;5;12;9
player 20;nick20;66;Team Y;C;1;0;0
player 25;nick25;88;Team Y;G;3;0;7
player 30;nick30;22;Team Y;F;6;2;6""",
    """HANDBALL
player 1;nick1;4;Team A;G;0;20
player 2;nick2;8;Team A;F;15;20
player 3;nick3;15;Team A;F;10;20
player 4;nick4;16;Team B;G;1;25""",
    """HANDBALL
player 5;nick5;5;Team D;F;3;1
player 6;nick6;28;Team D;F;1;0
player 3;nick3;6;Team C;G;5;2
player 2;nick2;10;Team C;G;3;9""",
    """HANDBALL
player 8;nick8;4;Team A;G;10;3
player 9;nick9;8;Team A;G;1;15
player 7;nick7;15;Team A;G;0;2
player 4;nick4;16;Team B;F;17;5""",
    """HANDBALL
player 10;nick10;7;Team X;F;5;9
player 6;nick6;20;Team Y;F;3;2
player 1;nick1;30;Team Y;F;7;11
player 9;nick9;55;Team Y;F;1;17""",
]

invalid_input_data = [
    """BASKETBALL
player 1;nick1;4;G;10;2;7
player 2;nick2;8;Team A;F;0;10;0
player 3;nick3;15;Team A;C;15;10;4
player 4;nick4;16;Team B;G;20;0;0
player 5;nick5;23;Team B;F;4;7;7
player 6;nick6;42;Team B;C;8;10;0""",
    """BASKETBALL
player 7;nick7;3;Team C;C;5;3;1
player 8;nick8;7;Team C;C;10;1;5
player 9;nick9;11;Team C;G;9;9;3
player 10;nick10;25;Team D;F;7;0;8
player 11;nick11;18;Team D;G;2;4;0
player 6;nick6;10;Team D;C;8;11;1""",
    """FOOTBALL
player 5;nick5;2;Team E;C;8;6;9
player 6;nick6;87;Team E;C;7;9;1
player 7;nick7;50;Team E;G;12;4;2
player 10;nick10;26;Team A;G;13;8;6
player 15;nick15;37;Team A;F;1;7;2
player 17;nick17;19;Team A;G;16;0;1""",
    """BASKETBALL
player 55;nick55;98;Team X;F;0;1;10
player 4;nick4;78;Team X;C;4;1;20
player 7;nick7;75;Team X;G;5;12;9
player 20;nick20;66;Team Y;C;1;0;0
player 25;nick25;88;Team Y;G;3;0;7
player 30;nick30;22;Team Y;F;6;2;6""",
    """HANDBALL
player 1;nick1;4;Team A;G;0;20
player 2;nick2;8;Team A;F;15;20
player 3;nick3;15;Team A;F;10;20
player 4;nick4;16;Team B;G;1;25""",
    """HANDBALL
player 5;nick5;5;Team D;F;3;1
player 6;nick6;28;Team D;F;1;0
player 3;nick3;6;Team C;G;5;2
player 2;nick2;10;Team C;G;3;9""",
    """HANDBALL
player 8;nick8;4;Team A;G;10;3
player 9;nick9;8;Team A;G;1;15
player 7;nick7;15;Team A;G;0;2
player 4;nick4;16;Team B;F;17;5""",
    """HANDBALL
player 10;nick10;7;Team X;F;5;9
player 6;nick6;20;Team Y;F;3;2
player 1;nick1;30;Team Y;F;7;11
player 9;nick9;55;Team Y;F;1;17""",
]