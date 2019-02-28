# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 23:44:44 2019

@author: Faishal Rachman
"""

import pandas as pd
import numpy as np
from scipy.signal import *
import matplotlib.pyplot as plt

def rmse(predictions, targets):
    return np.sqrt(np.mean((predictions-targets)**2))


file = "041.csv"
data = pd.read_csv("dataset_ppg/ppg_raw/"+file)
ppg = data['PPG'].tolist()[:1250]
for i in range(len(ppg)):
    try:
        ppg[i] = float(ppg[i])
    except:
        ppg[i] = 0