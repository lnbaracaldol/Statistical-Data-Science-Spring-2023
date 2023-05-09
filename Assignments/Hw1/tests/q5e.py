OK_FORMAT = True
test = {   'name': 'q5e',
    'points': 5,
    'suites': [   {   'cases': [   {'code': '>>> \n>>> len(bootstrap_data_means(election_sub))\n19', 'hidden': False, 'locked': False},
                                   {'code': '>>> \n>>> all(election_agg.index == bootstrap_data_means(election_sub).index)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> \n>>> 'mean' in bootstrap_data_means(election_sub).columns\nFalse", 'hidden': False, 'locked': False},
                                   {'code': '>>> \n>>> bootstrap_election_100_agg.shape\n(19, 100)', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
