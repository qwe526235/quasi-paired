# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 15:36:29 2022

@author: zjy52
"""

import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
os.chdir('C:/Users/Zjy52/Desktop/quasi-paired')
data=pd.read_excel('test_genus.xlsx')
##all
names=data['ID']
names=list(names)
df=data.set_index('ID')
cal=np.array(df)
standardizer = StandardScaler()
cal=standardizer.fit_transform(cal)
feat=[]
for i in range(len(cal)):
    for j in range(len(cal)):
          dist= np.linalg.norm(cal[i] - cal[j])
          feat.append(dist)
def cut_list(lists, cut_len):
    res_data = []
    if len(lists) > cut_len:
        for i in range(int(len(lists) / cut_len)):
            cut_a = lists[cut_len * i:cut_len * (i + 1)]
            res_data.append(cut_a)
        last_data = lists[int(len(lists) / cut_len) * cut_len:]
        if last_data:
            res_data.append(last_data)
    else:
        res_data.append(lists)
    return res_data

feat=cut_list(feat, len(df))
feat=pd.DataFrame(feat,index=names, columns=names)
feat.to_csv('dis_CAL.csv')
##CRC
crc=data[55:]
crc_name=crc['ID']
df_crc=crc.set_index('ID')
cal_crc=np.array(df_crc)
cal_crc=standardizer.fit_transform(cal_crc)
feat_crc=[]
for i in range(len(cal_crc)):
    for j in range(len(cal_crc)):
          dist= np.linalg.norm(cal_crc[i] - cal_crc[j])
          feat_crc.append(dist)
feat_crc=cut_list(feat_crc, 73)
feat_crc=pd.DataFrame(feat_crc,index=list(crc_name),columns=list(crc_name))
feat_crc.to_csv('CRC.csv')
##Healthy
heal=data[0:54]
heal_name=heal['ID']
df_heal=heal.set_index('ID')
cal_heal=np.array(df_heal)
cal_heal=standardizer.fit_transform(cal_heal)
feat_heal=[]
for i in range(len(cal_heal)):
    for j in range(len(cal_heal)):
          dist= np.linalg.norm(cal_heal[i] - cal_heal[j])
          feat_heal.append(dist)
feat_heal=cut_list(feat_heal,54 )
feat_heal=pd.DataFrame(feat_heal,index=list(heal_name),columns=list(heal_name))
feat_heal.to_csv('healthy.csv')

##group
len_heal=len(list(heal_name))
len_crc=len(list(crc_name))
h_name=list(heal_name)
c_name=list(crc_name)
for i in range(len(list(heal_name))):
    for j in range(len(list(heal_name))):
        feat[h_name[i]][h_name[j]]=0

for i in range(len(list(crc_name))):
            for j in range(len(list(crc_name))):
                feat[c_name[i]][c_name[j]]=0
feat.to_csv('group.csv')


