
import pandas as pd
import numpy as np
import os

import datetime 

df1 = pd.read_excel(r'C:\Users\sbhadra\AppData\Local\Programs\Python Scripts\Excel\data.xlsx')
df2 = pd.read_excel(r'C:\Users\sbhadra\AppData\Local\Programs\Python Scripts\Excel\Q.xlsx')

df1 = df1[['Key','Employee Code','Skill Code','Timesheet Date','Qualified']]
df1['Timesheet Date']=df1['Timesheet Date'].astype('datetime64[ns]')

df2 = df2[['Key','Employee Code','Qualification ID','Date Start','Date End','Date Expiry','Comments','Skill Level','Skill Qualified']]
df2['Qualification ID']=df2['Qualification ID'].fillna(-1)
df2['Qualification ID']=df2['Qualification ID'].astype(int)
df2['Date Start']=df2['Date Start'].astype('datetime64[ns]')
df2['Date End']=df2['Date End'].astype('datetime64[ns]') 
df2['Date Expiry']=df2['Date Expiry'].astype('datetime64[ns]')     
df1['Qualified']=df1['Qualified'].astype(str) 

for i in df2.index:
    if(pd.isnull(df2.at[i, 'Date End'])):
        df2.at[i, 'Date End'] = df2.at[i, 'Date Start']

for i in df1.index:
    for j in df2.index:
        if(df2.at[j, 'Key'] == df1.at[i, 'Key']):
            if(df1.at[i, 'Timesheet Date'] >= df2.at[i, 'Date Start'] and df1.at[i, 'Timesheet Date'] <= df2.at[i, 'Date Start']):
                df1.at[i, 'Qualified'] = 'Learner'
        print(i,df1.at[i, 'Employee Code'],df1.at[i, 'Skill Code'],df1.at[i, 'Timesheet Date'],df2.at[i, 'Date Start'],df2.at[i, 'Date End'],df2.at[i, 'Date Expiry'])
       