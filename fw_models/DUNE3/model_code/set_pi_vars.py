'''
get_rep_period
    - Calculate the variables dependent on pi parameters
'''

import pandas as pd
import pickle
import numpy as np

def set_pi_vars(vars):
    print('\t\tStarted applying variables dependent on pi parameters...')
    # Unpack Variables
    pi_1 = vars['pi_1']
    pi_2 = vars['pi_2']
    L = vars['L_']

    # Position of wavemaker
    Xc_WK = pi_1*L

    # Position of sponge
    Sponge_west_width = pi_2*L

    print('\t\tFinished applying variables dependent on pi parameters...')

    return {'Xc_WK': Xc_WK,
            'Sponge_west_width': Sponge_west_width}