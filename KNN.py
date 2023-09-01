# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 07:03:57 2022

@author: zjy52
"""

import os
import pandas as pd
import numpy as np
os.chdir('C:/Users/Zjy52/Desktop/quasi-paired/data')
data=pd.read_csv('distance.csv')
names=data['Sample']
df=data.set_index('Sample')
cal=np.array(df)
distance=[]
index=list(names)
for i in range(len(cal)):
    feat=cal[i,]
    feat=feat[feat>0]
    feat=np.sort(feat)
    dis=np.sum(feat[0:int(len(cal)**0.5)])/int(len(cal)**0.5)
    distance.append(dis)
distance={'sample':index,'knn':distance}
K=pd.DataFrame(distance)
Kmean=K['knn'].mean()
Ksd=K['knn'].std()
K_cut_max=Kmean+Ksd
K_cut_min=Kmean-Ksd
K_list=[]
K_dis=[]
for i in range(len(K)):
    if K.knn[i] >= K_cut_min and K.knn[i]<=K_cut_max:
        K_list.append(K['sample'][i])
        K_dis.append(K.knn[i])

f_data={'sample':K_list,'knn':K_dis}
f_data=pd.DataFrame(f_data)
f_data=f_data.set_index('sample')
f_data.to_csv('knn.csv')

##group_healthy
g_data=pd.read_csv('healthy_distance.csv')
gdata=g_data.set_index('Sample')
g_index=[]
for i in range(len(gdata)):
    for j in range(len(K_list)):
        if gdata.index[i]==K_list[j]:
             g_index.append(gdata.index[i])   
gdata=gdata.loc[g_index]
h_dis=[]
h_cal=np.array(gdata)
for i in range(len(h_cal)):
    feat=h_cal[i,]
    feat=feat[feat>0]
    feat=np.sort(feat)
    dis=np.sum(feat[0:int(len(h_cal)**0.5)])/int(len(h_cal)**0.5)
    h_dis.append(dis)
h_dis={'sample':g_index,'knn':h_dis}
H=pd.DataFrame(h_dis)
H=H.set_index('sample')
H.to_csv('healthy_knn.csv')

##CRC_group
c_data=pd.read_csv('crc_distance.csv')
cdata=c_data.set_index('Sample')
c_index=[]
for i in range(len(cdata)):
    for j in range(len(K_list)):
        if cdata.index[i]==K_list[j]:
             c_index.append(cdata.index[i])   
cdata=cdata.loc[c_index]
c_dis=[]
c_cal=np.array(cdata)
for i in range(len(c_cal)):
    feat=c_cal[i,]
    feat=feat[feat>0]
    feat=np.sort(feat)
    dis=np.sum(feat[0:int(len(c_cal)**0.5)])/int(len(c_cal)**0.5)
    c_dis.append(dis)
c_dis={'sample':c_index,'knn':c_dis}
C=pd.DataFrame(c_dis)
C=C.set_index('sample')
C.to_csv('crc_knn.csv')

##group to group
#healthy-crc
full_data=pd.read_csv('out_group_distance.csv')
full_data=full_data.set_index('Sample')
f_h=full_data.loc[g_index]
f_hdis=[]
f_h=np.array(f_h)
f_c=full_data.loc[c_index]
f_cdis=[]
f_c=np.array(f_c)
for i in range(len(f_h)):
    feat=f_h[i,]
    feat=feat[feat>0]
    feat=np.sort(feat)
    dis=np.sum(feat[0:int(len(f_c)**0.5)])/int(len(f_c)**0.5)
    f_hdis.append(dis)
f_hdis={'sample':g_index,'knn':f_hdis}
f_hdis=pd.DataFrame(f_hdis)
f_hdis=f_hdis.set_index('sample')
f_hdis.to_csv('Healthy-crc_knn.csv')

#crc_healthy

for i in range(len(f_c)):
    feat=f_c[i,]
    feat=feat[feat>0]
    feat=np.sort(feat)
    dis=np.sum(feat[0:int(len(f_h)**0.5)])/int(len(f_h)**0.5)
    f_cdis.append(dis)
f_cdis={'sample':c_index,'knn':f_cdis}
f_cdis=pd.DataFrame(f_cdis)
f_cdis=f_cdis.set_index('sample')
f_cdis.to_csv('crc-healthy_knn.csv')