OK_FORMAT = True
test = {   'name': 'q3b',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> import matplotlib ;\n>>> np.alltrue(np.array([l.get_text() for l in ax_3b.xaxis.get_ticklabels()]) == days)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import matplotlib ;\n'
                                               '>>> bars = [rect.get_height() for rect in ax_3b.get_children() \n'
                                               '...         if isinstance(rect, matplotlib.patches.Rectangle) and rect.get_x() != 0.0\n'
                                               '...        ];\n'
                                               ">>> np.allclose(np.array(bars)[-7:], calls['Day'].value_counts()[days].values)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
