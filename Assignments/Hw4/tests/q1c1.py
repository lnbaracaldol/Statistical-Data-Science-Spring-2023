OK_FORMAT = True
test = {   'name': 'q1c1',
    'points': 4,
    'suites': [   {   'cases': [   {'code': ">>> output1['U'].shape\n(16, 10)", 'hidden': False, 'locked': False},
                                   {'code': ">>> output1['V'].shape\n(15, 10)", 'hidden': False, 'locked': False},
                                   {   'code': ">>> output1['U'].index\n"
                                               "MultiIndex([('rating',   1),\n"
                                               "            ('rating',  85),\n"
                                               "            ('rating', 269),\n"
                                               "            ('rating', 271),\n"
                                               "            ('rating', 301),\n"
                                               "            ('rating', 312),\n"
                                               "            ('rating', 328),\n"
                                               "            ('rating', 339),\n"
                                               "            ('rating', 389),\n"
                                               "            ('rating', 650),\n"
                                               "            ('rating', 716),\n"
                                               "            ('rating', 727),\n"
                                               "            ('rating', 178),\n"
                                               "            ('rating', 299),\n"
                                               "            ('rating', 387),\n"
                                               "            ('rating', 883)],\n"
                                               "           names=[None, 'user id'])",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> output1['V'].index\n"
                                               "MultiIndex([(132,            'Wizard of Oz, The (1939)'),\n"
                                               "            (238,              'Raising Arizona (1987)'),\n"
                                               "            (748,                   'Saint, The (1997)'),\n"
                                               "            (196,           'Dead Poets Society (1989)'),\n"
                                               "            (197,                'Graduate, The (1967)'),\n"
                                               "            (185,                       'Psycho (1960)'),\n"
                                               "            (194,                   'Sting, The (1973)'),\n"
                                               "            (742,                       'Ransom (1996)'),\n"
                                               "            ( 82,                'Jurassic Park (1993)'),\n"
                                               "            ( 97,           'Dances with Wolves (1990)'),\n"
                                               "            (475,                'Trainspotting (1996)'),\n"
                                               "            (268,                  'Chasing Amy (1997)'),\n"
                                               "            (186,          'Blues Brothers, The (1980)'),\n"
                                               "            (496,        'It's a Wonderful Life (1946)'),\n"
                                               "            (111, 'Truth About Cats & Dogs, The (1996)')],\n"
                                               "           names=['movie id', 'movie title'])",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> output1['U'].columns\nRangeIndex(start=0, stop=10, step=1, name='k')", 'hidden': False, 'locked': False},
                                   {'code': ">>> output1['V'].columns\nRangeIndex(start=0, stop=10, step=1, name='k')", 'hidden': False, 'locked': False},
                                   {   'code': ">>> print((output1['V']@output1['U'].T).iloc[:5,:5].round(2))\n"
                                               '                                   rating                        \n'
                                               'user id                               1     85    269   271   301\n'
                                               'movie id movie title                                             \n'
                                               '132      Wizard of Oz, The (1939)    4.00  5.00  5.00  5.00  4.01\n'
                                               '238      Raising Arizona (1987)      4.00  2.00  5.00  4.01  1.85\n'
                                               '748      Saint, The (1997)           4.76  2.37  3.07  2.45  3.80\n'
                                               '196      Dead Poets Society (1989)   5.00  4.00  0.99  4.01  4.01\n'
                                               '197      Graduate, The (1967)        5.00  5.01  5.00  4.00  4.99\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
