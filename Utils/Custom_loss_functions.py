import numpy as np
import pandas as pd
from numba import jit

# Defining the Normalized Gini method
@jit
def gini(actual, pred, cmpcol = 0, sortcol = 1):
    assert( len(actual) == len(pred) )
    all = np.asarray(np.c_[ actual, pred, np.arange(len(actual)) ], dtype=np.float)
    all = all[ np.lexsort((all[:,2], -1*all[:,1])) ]
    totalLosses = all[:,0].sum()
    giniSum = all[:,0].cumsum().sum() / totalLosses
    
    giniSum -= (len(actual) + 1) / 2.
    return giniSum / len(actual)

def gini_normalized(a, p):
    return gini(a, p) / gini(a, a)

def gini_lgb(act, preds):
#    labels = dtrain.get_label()
    gini_score = gini_normalized(act, preds)
    return 'gini_lgb', gini_score,True
