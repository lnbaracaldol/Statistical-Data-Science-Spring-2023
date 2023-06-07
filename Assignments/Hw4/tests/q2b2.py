OK_FORMAT = True
test = {   'name': 'q2b2',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': ">>> print(output3['U'].iloc[:7,:6].round(2))\n"
                                               'k                  0     1     2     3     4     5\n'
                                               '       user id                                    \n'
                                               'rating 1       -0.22  0.12  1.89  0.67 -0.50  1.25\n'
                                               '       85       0.13  0.39 -0.41  0.63 -0.36  0.48\n'
                                               '       269      1.95  0.36 -0.17 -0.39  0.53  2.67\n'
                                               '       271      0.88  2.12  0.66 -1.61  0.14  0.41\n'
                                               '       301     -0.98 -0.15  1.07  0.17  1.72  1.21\n'
                                               '       312     -1.22  0.74  0.46 -1.19  0.15  1.38\n'
                                               '       328      0.11  0.27 -0.68 -0.57 -0.12  0.72\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> print( (Rsmall - logistic_rating(output3['U'], output3['V'])).iloc[:7, :6].round(3) )\n"
                                               '                                   rating                                   \n'
                                               'user id                               1      85     269    271    301    312\n'
                                               'movie id movie title                                                        \n'
                                               '132      Wizard of Oz, The (1939)  -0.000  0.046  0.000  0.009 -0.002  0.042\n'
                                               '238      Raising Arizona (1987)    -0.001 -0.001  0.024 -0.001    NaN -0.001\n'
                                               '748      Saint, The (1997)            NaN    NaN    NaN    NaN    NaN    NaN\n'
                                               '196      Dead Poets Society (1989)  0.012  0.001 -0.030 -0.001 -0.001    NaN\n'
                                               '197      Graduate, The (1967)       0.026  0.042  0.009 -0.001  0.011 -0.000\n'
                                               '185      Psycho (1960)             -0.000    NaN  0.003 -0.000    NaN  0.043\n'
                                               '194      Sting, The (1973)         -0.001 -0.007  0.044  0.064  0.003 -0.007\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
