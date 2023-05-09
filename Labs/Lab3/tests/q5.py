OK_FORMAT = True
test = {   'name': 'q5',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> import matplotlib ;\n>>> np.alltrue(np.array([l.get_text() for l in ax_5.xaxis.get_ticklabels()]) == days)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import matplotlib ;\n'
                                               '>>> bars = [rect.get_height() for rect in ax_5.get_children() \n'
                                               '...         if isinstance(rect, matplotlib.patches.Rectangle) and rect.get_x() != 0.0\n'
                                               '...        ];\n'
                                               '>>> np.allclose(np.array(bars)[-7:], np.array([27, 32, 29, 33, 35, 40, 12]))\n'
                                               'False',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
