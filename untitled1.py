# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 01:25:36 2019

@author: Faishal Rachman
"""

import pandas as pd
import pywt
from frecg.ecg import *
data_ppg = pd.read_csv("classified/gabungan.csv",header=None).values
length = len(data_ppg[0])
signal = data_ppg[:,0:1000].tolist()
signal_class = data_ppg[:,1000].tolist()
signals = [butter_lowpass_filter(ppg) for ppg in signal]

#
#from keras.models import Sequential
#from keras.layers import Dense
#from keras.wrappers.scikit_learn import KerasClassifier
#from keras.utils import np_utils
#import numpy as np
#np.random.seed(7)
#
#def baseline_model():
#	# create model
#	model = Sequential()
#	model.add(Dense(100, input_dim=1000, activation='relu'))
#	model.add(Dense(3, activation='softmax'))
#	# Compile model
#	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#	return model
#
#estimator = KerasClassifier(build_fn=baseline_model, epochs=200, batch_size=5, verbose=0)

#filtered = [np.concatenate(pywt.wavedec(signal[i],'db4',level=7)) for i in range(len(signal))]
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(hidden_layer_sizes=2000)
clf.fit(signals,signal_class)
pred = clf.predict(signal)
    
ppg = pd.read_csv("dataset_ppg/ppg_raw/211.csv")['PPG'].values.tolist()
for i in range(len(ppg)):
    try:
        ppg[i] = float(ppg[i])
    except:
        ppg[i] = 0
ppg = butter_lowpass_filter(ppg)

panjang = len(ppg)/1000        
ppg_1000 = np.array_split(np.array(ppg),panjang)
filtered = [np.concatenate(pywt.wavedec(ppg_1000[i],'db4',level=7)) for i in range(len(ppg_1000))]
pred = clf.predict(ppg_1000)