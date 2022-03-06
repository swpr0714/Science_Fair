import netCDF4 as nc
import numpy as np
import pandas as pd
import os
import csv
path_0 ='c:/NC'
all_season = os.listdir(path_0)
for season in all_season:
    path_1 = os.path.join(path_0,season)
    all_folder = os.listdir(path_1)
    for folder in all_folder: #求月平均
        path_2 = os.path.join(path_1,folder)
        all_file = os.listdir(path_2)
        for file in all_file: #求各日平均
            path_3 = os.path.join(path_2,file)
            #%%
            err = 0
            cor = 0
            all = 0
            list = []
            all_month = []
            month = []
            month_avg = []
            #%%
            data = nc.Dataset(path_3)
            sst = np.array(data['analysed_sst'])
            sst0 = np.reshape (sst,(3600,7200))
            for i in range (1900,2400,1):
                for j in range (5800,7200,1):
                    if sst0[i,j] < 0:
                        sst0[i,j] = 0
                        all = all + 1
                        err = err + 1
                    else:
                        cor = cor + 1
                        all = all + 1
                        list.append(sst0[i,j])
                            #%%
            month.append(np.average(list)-273.15) #算出日平均 寫入month
            print('1')
        all_month.append(month) #算出月平均寫入all_month
        print('2')
    x = str(season)
    y = '.csv'
    z = x+y
    with open(z, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(all_month)