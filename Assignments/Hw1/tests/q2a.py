OK_FORMAT = True
test = {   'name': 'q2a',
    'points': 5,
    'suites': [   {   'cases': [   {'code': '>>> \n>>> probwin_change.shape\n(960, 1)', 'hidden': False, 'locked': False},
                                   {'code': ">>> \n>>> probwin_change.columns\nIndex(['probwin'], dtype='object')", 'hidden': False, 'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> probwin_change.index.sort_values()\n'
                                               "Index(['A. Donald McEachin', 'Aaron Andrus', 'Aaron Swisher',\n"
                                               "       'Abby Finkenauer', 'Abigail Spanberger', 'Adam B. Schiff',\n"
                                               "       'Adam Kinzinger', 'Adam Smith', 'Adrian Smith', 'Adriano Espaillat',\n"
                                               '       ...\n'
                                               "       'William Lacy Clay', 'William Tanoos', 'William Timmons',\n"
                                               "       'Willie Billups', 'Xochitl Torres Small', 'Young Kim', 'Yvette Clarke',\n"
                                               "       'Yvette Herrell', 'Yvonne Hayes Hinson', 'Zoe Lofgren'],\n"
                                               "      dtype='object', name='candidate', length=960)",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> \n>>> np.round(np.abs(probwin_change.probwin).sum(), 1)\n26.7', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
