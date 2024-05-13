import pandas as pd
import os

import datetime

df1 = pd.read_excel(r'C:\Users\sbhadra\AppData\Local\Programs\Python Scripts\Excel\data.xlsx')
df2 = pd.read_excel(r'C:\Users\sbhadra\AppData\Local\Programs\Python Scripts\Excel\Q.xlsx')

df3= df1.merge(df2,how = 'left', on = ['Key'])


df3['Employee Code_x']=df3['Employee Code_x']
df3['Timesheet Date']=df3['Timesheet Date'].astype('datetime64[ns]')
#df3['Date Start'] =  df3['Date Start'].dt.strftime('%m/%d/%Y')
df3['Date Start'] = pd.to_datetime(df3['Date Start']).strftime('%Y-%m-%d')
df3['Date End'] = pd.to_datetime(df3['Date End'], errors='coerce')
df3['Date Expiry'] = pd.to_datetime(df3['Date Expiry'], errors='coerce')
df3['Qualification ID']=df3['Qualification ID'].fillna(-1)
df3['Qualification ID']=df3['Qualification ID'].astype(int)
df3['Comments']=df3['Comments']
df3['Skill Code']=df3['Skill Code']
df3['Qualification ID Integer']=df3['Qualification ID Integer']
print(df3.dtypes)
print(df3)

