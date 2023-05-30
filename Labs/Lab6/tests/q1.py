OK_FORMAT = True
test = {   'name': 'q1',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> X.columns\nIndex(['intercept', 'LSTAT'], dtype='object')", 'hidden': False, 'locked': False},
                                   {'code': '>>> X.shape\n(506, 2)', 'hidden': False, 'locked': False},
                                   {'code': ">>> np.all(y == housing['MEDV'])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.all(X['intercept'] == 1)\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.all(X['LSTAT'] == housing['LSTAT'])\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
