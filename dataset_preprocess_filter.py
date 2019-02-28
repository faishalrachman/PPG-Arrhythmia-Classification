# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:13:56 2019

@author: Faishal Rachman
"""

import pandas as pd
from frecg.ecg import *
from frecg.tools import *
from frecg.plot import *
from frecg.ecg_classification import window_class, class_count
from scipy.signal import *

import os
##
for root, dirs, files in os.walk("dataset_ppg/ppg_raw/"):
    for file in files:
#        file = "211.csv"
        data = pd.read_csv("dataset_ppg/ppg_raw/"+file)
        ecg, ppg = data['ECG'].tolist(), data['PPG'].tolist()
        #ecg, ppg = ecg[:2000], ppg[:2000]
        for i in range(len(ecg)):
            try:
                ecg[i] = float(ecg[i])
            except:
                ecg[i] = 0
            try:
                ppg[i] = float(ppg[i])
            except:
                ppg[i] = 0
                
        #ecg, ppg = np.clip(ecg,-1,0.5), bwr(ppg)[1][:2000]
        
        ppg = butter_lowpass_filter(ppg,1.9)
        #ppg = np.clip(ppg,-0.2,0.2)
        filtered_ecg = filter_dwt(ecg)
        r_peaks = getr_peaks(filtered_ecg)
        rr_list, start_stop = get_rr(r_peaks)
        r_class = window_class(rr_list)
        count = class_count(r_class)
        r_peaks_ppg = get_ppgpeaks(ppg)
        #r_peaks_ppg.pop(0)
        #r_peaks_ppg.pop(-1)
        rr_list_ppg, start_stop_ppg = get_rr(r_peaks_ppg)
        r_class_ppg = window_class(rr_list_ppg)
        count_ppg = class_count(r_class_ppg)
#        plot_with_rpeaks(ppg,r_peaks_ppg)
#        plt.show()
        print(file +" "+ str(count) + " " + str(count_ppg))
##        file = "041.csv"
#        try:
#            data = pd.read_csv("dataset_ppg/ppg_raw/"+file)
#            ecg, ppg = data['ECG'].tolist(), data['PPG'].tolist()
#            for i in range(len(ecg)):
#                try:
#                    ecg[i] = float(ecg[i])
#                except:
#                    ecg[i] = 0
#                try:
#                    ppg[i] = float(ppg[i])
#                except:
#                    ppg[i] = 0
#            ecg, ppg = np.clip(ecg,-1,0.5), bwr(ppg)[1]
#            ppg = butter_lowpass_filter(ppg,25)
#            filtered_ecg = filter_dwt(ecg)
#            r_peaks = getr_peaks(filtered_ecg)
#            rr_list, start_stop = get_rr(r_peaks)
#            r_class = window_class(rr_list)
#            count = class_count(r_class)
#            r_peaks_ppg = get_ppgpeaks(ppg)
#            rr_list_ppg, start_stop_ppg = get_rr(r_peaks_ppg)
#            r_class_ppg = window_class(rr_list_ppg)
##            count = class_count(r_class)
#            count_ppg = class_count(r_class_ppg)
#            print(file +" "+ str(count) + " " + str(count_ppg))
#        except:
#            print(file)


#
#file = "211.csv"
#data = pd.read_csv("dataset_ppg/ppg_raw/"+file)
#ecg, ppg = data['ECG'].tolist(), data['PPG'].tolist()
##ecg, ppg = ecg[:2000], ppg[:2000]
#for i in range(len(ecg)):
#    try:
#        ecg[i] = float(ecg[i])
#    except:
#        ecg[i] = 0
#    try:
#        ppg[i] = float(ppg[i])
#    except:
#        ppg[i] = 0
#        
##ecg, ppg = np.clip(ecg,-1,0.5), bwr(ppg)[1][:2000]
#
#ppg = butter_lowpass_filter(ppg,1.9)
##ppg = np.clip(ppg,-0.2,0.2)
#filtered_ecg = filter_dwt(ecg)
#r_peaks = getr_peaks(filtered_ecg)
#rr_list, start_stop = get_rr(r_peaks)
#r_class = window_class(rr_list)
#count = class_count(r_class)
#r_peaks_ppg = get_ppgpeaks(ppg)
##r_peaks_ppg.pop(0)
##r_peaks_ppg.pop(-1)
#rr_list_ppg, start_stop_ppg = get_rr(r_peaks_ppg)
#r_class_ppg = window_class(rr_list_ppg)
#count_ppg = class_count(r_class_ppg)
#plot_with_rpeaks(ppg,r_peaks_ppg)
#plt.show()
#print(file +" "+ str(count) + " " + str(count_ppg))
#
##        
#filtered_ecg = filter_dwt(ecg)
#r_peaks = getr_peaks(filtered_ecg)
#rr_list, start_stop = get_rr(r_peaks)
#r_class = window_class(rr_list)
#count = class_count(r_class)