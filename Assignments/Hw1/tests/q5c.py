OK_FORMAT = True
test = {   'name': 'q5c',
    'points': 5,
    'suites': [   {   'cases': [   {'code': '>>> len(upper)\n19', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(lower)\n19', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(lower < upper)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> (frac_covering > 0.5) & (frac_covering < 1)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.round(frac_covering, 3)\n0.684', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
