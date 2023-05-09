OK_FORMAT = True
test = {   'name': 'q6a',
    'points': 3,
    'suites': [   {   'cases': [   {'code': ">>> 'Hour' in calls.columns\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> set(calls["Hour"]) == set(range(24))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> list(calls["Hour"][:5]) == [22, 21, 20, 8, 13]\nFalse', 'hidden': False, 'locked': False},
                                   {'code': ">>> np.allclose(calls['Hour'].mean(), 13.35823)\nFalse", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
