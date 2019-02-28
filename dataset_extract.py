import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from frecg.tools import *

def find_column(name, headers):
    for i in range(len(headers)):
        if (name in headers[i]):
            return i
    return -1

for root, dirs, files in os.walk("dataset_ppg/extracted_csv/"):
    for file in files:
        ppg_column, ecg_column = -1, -1
        dataset = pd.read_csv("dataset_ppg/extracted_csv/%s" % file)
        headers = list(dataset)
        ppg_column = find_column("PLETH",headers)
        if (ppg_column != -1):
            ecg_column = find_column("MCL",headers)
            if (ecg_column == -1):
                ecg_column = find_column("I",headers)
            if (ecg_column == -1):
                continue
        if (ppg_column != -1 and ecg_column != -1):
            print(file,headers[ppg_column], headers[ecg_column])
            ecg_data, ppg_data = dataset.iloc[:,ecg_column][1::], dataset.iloc[:,ppg_column][1::]
            data = np.transpose([ecg_data, ppg_data])
            save_df(pd.DataFrame(data),"dataset_ppg/ppg_raw/"+file,headers=["ECG", "PPG"])