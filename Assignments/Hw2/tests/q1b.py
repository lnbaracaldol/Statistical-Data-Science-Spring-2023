OK_FORMAT = True
test = {   'name': 'q1b',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> print(type(allplayers))\n<class 'pandas.core.frame.DataFrame'>\n", 'hidden': False, 'locked': False},
                                   {   'code': '>>> allplayers.columns \n'
                                               "Index(['DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FIRST_LAST', 'ROSTERSTATUS',\n"
                                               "       'FROM_YEAR', 'TO_YEAR', 'PLAYERCODE', 'TEAM_ID', 'TEAM_CITY',\n"
                                               "       'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CODE', 'GAMES_PLAYED_FLAG',\n"
                                               "       'OTHERLEAGUE_EXPERIENCE_CH'],\n"
                                               "      dtype='object')",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> allplayers.shape \n(4540, 13)', 'hidden': False, 'locked': False},
                                   {'code': ">>> allplayers.index.name \n'PERSON_ID'", 'hidden': False, 'locked': False},
                                   {   'code': '>>> allplayers.tail(3).DISPLAY_LAST_COMMA_FIRST\n'
                                               'PERSON_ID\n'
                                               '1629967    Flatten, Skyler\n'
                                               '1630001       Morgan, Matt\n'
                                               '1630003        Scott, MIke\n'
                                               'Name: DISPLAY_LAST_COMMA_FIRST, dtype: object',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
