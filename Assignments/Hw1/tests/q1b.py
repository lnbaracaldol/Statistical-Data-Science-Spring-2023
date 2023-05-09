OK_FORMAT = True
test = {   'name': 'q1b',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> \n>>> election_sub.shape\n(1920, 14)', 'hidden': False, 'locked': False},
                                   {'code': '>>> \n>>> election_sub.candidate.isnull().any()\nFalse', 'hidden': False, 'locked': False},
                                   {'code': ">>> \n>>> (election_sub.groupby('candidate').size()==2).all()\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
