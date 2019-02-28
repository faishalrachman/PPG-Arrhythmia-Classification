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
###
        
sinyalhasil_normal = []
sinyalhasil_pac = []
sinyalhasil_pvc = []
sinyalhasil_ppg_normal = []
sinyalhasil_ppg_pac = []
sinyalhasil_ppg_pvc = []
        
for root, dirs, files in os.walk("dataset_ppg/ppg_raw/"):
    for file in files:
        data = pd.read_csv("dataset_ppg/ppg_raw/"+file)
        ecg, ppg = data['ECG'].tolist(), data['PPG'].tolist()
#        ecg = ecg[:len(ecg)-180]
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
        r_peaks = get_ppgpeaks(filtered_ecg)
        rr_list, start_stop = get_rr(r_peaks)
        r_class = window_class(rr_list)
        count = class_count(r_class)
        print(file +" "+ str(count))
        for i in range(len(r_class)):
            panjang = 1500
            awal = start_stop[i-1][1]
            akhir = awal+panjang
            data_ecg = ecg[awal:akhir]
            data_ppg = ppg[awal:akhir]
            if (len(data_ecg) == panjang and len(data_ppg) == panjang):
                if (r_class[i] == "N"):
                    sinyalhasil_normal.append(data_ecg)
                    sinyalhasil_ppg_normal.append(data_ppg)
                elif (r_class[i] == "A"):
                    sinyalhasil_pac.append(data_ecg)
                    sinyalhasil_ppg_pac.append(data_ppg)
                elif (r_class[i] == "V"):
                    sinyalhasil_pvc.append(data_ecg)
                    sinyalhasil_ppg_pvc.append(data_ppg)
            else:
                print (len(data_ecg), len(data_ppg))
#                
#            
#save_df(pd.DataFrame(sinyalhasil_normal),"classified/ecg_normal.csv")
#save_df(pd.DataFrame(sinyalhasil_ppg_normal),"classified/ppg_normal.csv")
#save_df(pd.DataFrame(sinyalhasil_pac),"classified/ecg_pac.csv")
#save_df(pd.DataFrame(sinyalhasil_ppg_pac),"classified/ppg_pac.csv")
#save_df(pd.DataFrame(sinyalhasil_pvc),"classified/ecg_pvc.csv")
#save_df(pd.DataFrame(sinyalhasil_ppg_pvc),"classified/ppg_pvc.csv")
#



##
#file = "209.csv"
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
#r_peaks = get_ppgpeaks(filtered_ecg)
#rr_list, start_stop = get_rr(r_peaks)
#r_class = window_class(rr_list)
#count = class_count(r_class)
#print(file +" "+ str(count))
#
#sinyalhasil = []
#sinyalhasil_ppg = []
#
#for i in range(len(r_class)):
#    awal = start_stop[i-1][1]
#    akhir = awal+1000
#    sinyalhasil.append(ecg[awal:akhir])
#    sinyalhasil[i].append(r_class[i])
#    
#    sinyalhasil_ppg.append(ppg[awal:akhir].tolist())
#    sinyalhasil_ppg[i].append(r_class[i])
#save_df(pd.DataFrame(sinyalhasil),"dataset_classified_ecg/"+file)
#save_df(pd.DataFrame(sinyalhasil_ppg),"dataset_classified_ppg/"+file)
#
#
##        
##filtered_ecg = filter_dwt(ecg)
#r_peaks = getr_peaks(filtered_ecg)
#rr_list, start_stop = get_rr(r_peaks)
#r_class = window_class(rr_list)
#count = class_count(r_class)