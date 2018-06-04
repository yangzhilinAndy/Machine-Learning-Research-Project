import os
import pandas as pd
import numpy as np
from cpdetect import cpDetector

df00=pd.read_csv('/Users/zhilinyang/Desktop/data_Q1_2017/2017-01-01.csv',header=None)
df000=df00.iloc[1:]
colname=df00.iloc[0]
df000.columns=colname
root_dir = r"/Users/zhilinyang/Desktop/data_Q1_2017"
combST = pd.DataFrame()
combHi = pd.DataFrame()

for file in os.listdir(root_dir):
        file_name = root_dir +'/'+ file
        df0=pd.read_csv(file_name,header=None)
        df=df0.iloc[1:]
        colname=df0.iloc[0]
        df.columns=colname
        dfST=df[df['model'].str.match('ST')]
        samplesST=dfST['serial_number']
        dfHi=df[df['model'].str.match('Hitachi')]
        samplesHi = dfHi['serial_number']
        featuresST=['smart_1_normalized','smart_1_raw',
            'smart_5_normalized','smart_5_raw',
            'smart_7_normalized','smart_7_raw',
            'smart_184_normalized','smart_184_raw',
            'smart_188_raw','smart_240_raw',
            'smart_189_normalized','smart_189_raw',
            'smart_190_normalized','smart_190_raw',
            'smart_193_normalized','smart_193_raw',
            'smart_194_normalized','smart_194_raw',
            'smart_197_normalized','smart_197_raw',
            'smart_198_normalized','smart_198_raw',
            'smart_241_raw','smart_242_raw']
        featuresHi=['smart_1_normalized','smart_1_raw',
            'smart_5_normalized','smart_5_raw',
            'smart_3_normalized','smart_3_raw',
            'smart_194_normalized', 'smart_194_raw',
            'smart_196_normalized', 'smart_196_raw',
            'smart_197_normalized', 'smart_197_raw'
            ]
        
        #change point detection
        dfSTcpd=pd.concat([ dfST['date'],dfST['serial_number'],dfST[featuresST] ],axis=1)
        dfHicpd=pd.concat([ dfHi['date'],dfHi['serial_number'],dfHi[featuresST] ],axis=1)
        dfST.dropna(axis=0)
        dfHi.dropna(axis=0)
        for sample in samplesST:
            sample = str(sample)
            combST.append(dfSTcpd[dfSTcpd['serial_number'].str.match(sample)])
            combHi.to_csv(path_or_buf='')
        for sample in samplesHi:
            sample = str(sample)
            combHi.append(dfSTcpd[dfSTcpd['serial_number'].str.match(sample)])
            combHi.to_csv(path_or_buf='')










