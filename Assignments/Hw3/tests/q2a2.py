OK_FORMAT = True
test = {   'name': 'q2a2',
    'points': 4,
    'suites': [   {   'cases': [   {'code': '>>> len(contours)\n4', 'hidden': False, 'locked': False},
                                   {'code': '>>> f_vals.shape\n(2000, 3)', 'hidden': False, 'locked': False},
                                   {'code': ">>> ax.xaxis.get_label_text(), ax.yaxis.get_label_text()\n('$x_1$', '$x_2$')", 'hidden': False, 'locked': False},
                                   {'code': ">>> [f.get_text() for f in ax.legend_.get_texts()]\n['0', '10', '20', '30']", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
