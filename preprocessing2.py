import os
import pandas as pd

df0=pd.read_csv(r"/Users/zhilinyang/Desktop/ST_data/ST 2017-01-01.csv", header=None)
df1=pd.read_csv(r"/Users/zhilinyang/Desktop/Hi_data/Hi 2017-01-01.csv", header=None)
colname = df0.iloc[0]
df0 = df0.iloc[1:]
df0.columns = colname
df0 = df0.iloc[:,1:]
df0.to_csv(path_or_buf=r"/Users/zhilinyang/Desktop/combST.csv")

colname = df1.iloc[0]
df1 = df1.iloc[1:]
df1.columns = colname
df1 = df1.iloc[:,1:]
df1.to_csv(path_or_buf=r"/Users/zhilinyang/Desktop/combHi.csv")
samplesST=df0['serial_number']
samplesHi=df1['serial_number']

num=0
root_dir1=r"/Users/zhilinyang/Desktop/ST_data"
root_dir2=r"/Users/zhilinyang/Desktop/Hi_data"

for file in os.listdir(root_dir1):
    num = num + 1
    if num<3:
        continue
    file_name=root_dir1+'/'+file
    df=pd.read_csv(file_name,header=None)
    df=df.iloc[:,1:]
    df.to_csv(path_or_buf=r"/Users/zhilinyang/Desktop/combST.csv", mode='a')

num=0
for file in os.listdir(root_dir2):
    num = num + 1
    if num<3:
        continue
    file_name=root_dir2+'/'+file
    df=pd.read_csv(file_name,header=None)
    df=df.iloc[:,1:]
    df.to_csv(path_or_buf=r"/Users/zhilinyang/Desktop/combHi.csv", mode='a')


