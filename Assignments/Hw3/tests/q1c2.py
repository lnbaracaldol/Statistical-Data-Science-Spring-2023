OK_FORMAT = True
test = {   'name': 'q1c2',
    'points': 6,
    'suites': [   {   'cases': [   {'code': '>>> len(boundary)\n4', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.all([type(d) is pd.DataFrame for d in boundary])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> type(hull) is pd.DataFrame\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> np.all([f in hull.columns.values for f in ['$x_1$', '$x_2$', 'constraint']])\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
