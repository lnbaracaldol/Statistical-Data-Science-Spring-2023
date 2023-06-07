OK_FORMAT = True
test = {   'name': 'q1c2',
    'points': 4,
    'suites': [   {   'cases': [   {'code': ">>> output2['U'].shape\n(5, 8)", 'hidden': False, 'locked': False},
                                   {   'code': ">>> print((output2['V']@output2['U'].T).round(2))\n"
                                               '                                   rating                        \n'
                                               'user id                               1     85    269   271   301\n'
                                               'movie id movie title                                             \n'
                                               '132      Wizard of Oz, The (1939)    4.00  5.00  5.00  5.00  4.01\n'
                                               '238      Raising Arizona (1987)      4.00  2.00  5.00  4.00  3.01\n'
                                               '748      Saint, The (1997)           1.92  1.53  1.97  1.47  1.52\n'
                                               '196      Dead Poets Society (1989)   5.00  4.00  1.00  4.00  4.00\n'
                                               '197      Graduate, The (1967)        5.00  5.00  5.00  4.00  5.01\n'
                                               '185      Psycho (1960)               4.00  3.67  5.00  3.00  3.80\n'
                                               '194      Sting, The (1973)           4.01  4.01  5.00  5.00  3.99\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> output2['V'].shape\n(7, 8)", 'hidden': False, 'locked': False},
                                   {   'code': ">>> output2['U'].index\n"
                                               "MultiIndex([('rating',   1),\n"
                                               "            ('rating',  85),\n"
                                               "            ('rating', 269),\n"
                                               "            ('rating', 271),\n"
                                               "            ('rating', 301)],\n"
                                               "           names=[None, 'user id'])",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> output2['V'].index\n"
                                               "MultiIndex([(132,  'Wizard of Oz, The (1939)'),\n"
                                               "            (238,    'Raising Arizona (1987)'),\n"
                                               "            (748,         'Saint, The (1997)'),\n"
                                               "            (196, 'Dead Poets Society (1989)'),\n"
                                               "            (197,      'Graduate, The (1967)'),\n"
                                               "            (185,             'Psycho (1960)'),\n"
                                               "            (194,         'Sting, The (1973)')],\n"
                                               "           names=['movie id', 'movie title'])",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> output2['U'].columns\nRangeIndex(start=0, stop=8, step=1, name='k')", 'hidden': False, 'locked': False},
                                   {'code': ">>> output2['V'].columns\nRangeIndex(start=0, stop=8, step=1, name='k')", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
