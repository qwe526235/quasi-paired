# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 09:31:46 2022

@author: zjy52
"""
import os
import pandas as pd
os.chdir('C:/Users/Zjy52/Desktop/quasi-paired/data')
#healthy
hc=pd.read_csv('Healthy-crc_knn.csv')
h=pd.read_csv('healthy_knn.csv')
h_sample=[]
for i in range(len(hc)):
    if hc['knn'][i]<=h['knn'][i]:
        h_sample.append(hc['sample'][i])
h_sample=pd.DataFrame(h_sample,columns=['sample'])
h_sample.to_csv('healthy_sample.csv')

#crc
ch=pd.read_csv('crc-healthy_knn.csv')
c=pd.read_csv('crc_knn.csv')
c_sample=[]
for i in range(len(ch)):
    if ch['knn'][i]<=c['knn'][i]:
        c_sample.append(ch['sample'][i])
c_sample=pd.DataFrame(c_sample,columns=['sample'])
c_sample.to_csv('crc_sample.csv')