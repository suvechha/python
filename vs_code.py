import pandas as pd
import os

import datetime

df1 = pd.read_excel(r'C:\Users\sbhadra\AppData\Local\Programs\Python Scripts\Excel\data.xlsx')
df2 = pd.read_excel(r'C:\Users\sbhadra\AppData\Local\Programs\Python Scripts\Excel\Q.xlsx')

df3= df1.merge(df2,how = 'left', on = ['Key'])
#print (df3)

print(df3[['Employee Code_x','Timesheet Date','Date Start','Date End','Date Expiry','Comments','Skill Code','Qualification ID','Qualification ID Integer']])

df3['Qualification ID'] = df3['Qualification ID'].map(str)

