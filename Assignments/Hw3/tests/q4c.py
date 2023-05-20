OK_FORMAT = True
test = {   'name': 'q4c',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> np.round(xstar2, 2)\n'
                                               'array([0.08, 0.22, 0.  , 0.  , 0.  , 0.  , 2.  , 0.  , 0.  , 0.  , 0.  ,\n'
                                               '       0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 2.  , 1.42, 0.  , 0.  , 2.  ,\n'
                                               '       0.  , 0.  , 1.93, 0.  , 0.15, 0.25, 0.  , 0.  , 0.  , 0.  , 0.  ,\n'
                                               '       0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.24, 0.  , 0.  , 0.  ,\n'
                                               '       0.  , 0.  , 2.  , 0.  , 2.  , 0.  , 0.  , 0.  , 2.  , 0.  , 0.  ,\n'
                                               '       0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ])',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> ncontent.T@xstar2 <= requirements['Max'].values\n"
                                               'Calories         True\n'
                                               'Cholesterol      True\n'
                                               'Total_Fat        True\n'
                                               'Sodium           True\n'
                                               'Carbohydrates    True\n'
                                               'Dietary_Fiber    True\n'
                                               'Protein          True\n'
                                               'Vit_A            True\n'
                                               'Vit_C            True\n'
                                               'Calcium          True\n'
                                               'Iron             True\n'
                                               'dtype: bool',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> ncontent.T@xstar2 >= requirements['Min'].values\n"
                                               'Calories         True\n'
                                               'Cholesterol      True\n'
                                               'Total_Fat        True\n'
                                               'Sodium           True\n'
                                               'Carbohydrates    True\n'
                                               'Dietary_Fiber    True\n'
                                               'Protein          True\n'
                                               'Vit_A            True\n'
                                               'Vit_C            True\n'
                                               'Calcium          True\n'
                                               'Iron             True\n'
                                               'dtype: bool',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
