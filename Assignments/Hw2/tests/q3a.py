OK_FORMAT = True
test = {   'name': 'q3a',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> ## Smoothed surface should sum to 1;\n'
                                               '>>> xedges = np.linspace(start=-300, stop=300, num=151);\n'
                                               '>>> yedges = np.linspace(start=-48, stop=372, num=106);\n'
                                               ">>> bin_shots(pd.DataFrame({'LOC_X' : curry_data.LOC_X , 'LOC_Y' : curry_data.LOC_Y}), (xedges, yedges), density=True)[0].sum()\n"
                                               '1.0',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> ## Total number of shots in the binned results is right;\n'
                                               '>>> xedges = np.linspace(start=-300, stop=300, num=151);\n'
                                               '>>> yedges = np.linspace(start=-48, stop=372, num=106);\n'
                                               ">>> bin_shots(pd.DataFrame({'LOC_X' : curry_data.LOC_X , 'LOC_Y' : curry_data.LOC_Y}), (xedges, yedges))[0].sum()\n"
                                               '1328.0',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> ## Number of bined shots in smaller xrange works;\n'
                                               '>>> xedges2 = np.linspace(start=-100, stop=100, num=151);\n'
                                               '>>> yedges = np.linspace(start=-48, stop=372, num=106);\n'
                                               ">>> bin_shots(pd.DataFrame({'LOC_X' : curry_data.LOC_X , 'LOC_Y' : curry_data.LOC_Y}), (xedges2, yedges))[0].sum()\n"
                                               '589.0',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> ## Number of bined shots in smaller yrange works;\n'
                                               '>>> xedges = np.linspace(start=-300, stop=300, num=151);\n'
                                               '>>> yedges2 = np.linspace(start=0, stop=100, num=151);\n'
                                               ">>> bin_shots(pd.DataFrame({'LOC_X' : curry_data.LOC_X , 'LOC_Y' : curry_data.LOC_Y}), (xedges, yedges2))[0].sum()\n"
                                               '479.0',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
