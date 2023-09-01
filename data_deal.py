# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 08:52:51 2022

@author: zjy52
"""
import os 
import pandas as pd
os.chdir('C:/Users/Zjy52/Desktop/quasi-paired/species/rawdata')
filePath=r'C:/Users/Zjy52/Desktop/quasi-paired/species/rawdata'
fileList=os.listdir(filePath)
##count_species_numb
species_list=[]
for file in fileList:
    sp=pd.read_csv(os.path.join(filePath,file),sep='\t')
    for i in range(len(sp)):
        species_list.append(sp['Species'][i])
species_list=set(species_list)
s_list=list(species_list)
slist=[]
for i in range(len(fileList)):
    slist.append(fileList[i].replace('.txt',''))
    
df=pd.DataFrame(index=slist,columns=s_list)

for i in range(len(slist)):
        sp=pd.read_csv(fileList[i],sep='\t')
        for m in range(len(sp)):
              for j in range(len(s_list)):          
                if df.columns[j]==sp['Species'][m]:
                    df.loc[slist[i]][j]=sp['Abun'][m]
df=df.fillna(0)
df.to_csv('../species_data.csv')
