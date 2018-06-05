import os
import pandas as pd
import numpy as np
from cpdetect import cpDetector

root_dir = r"/Users/zhilinyang/Desktop/data_Q1_2017"
omit1st = True

for file in os.listdir(root_dir):
        if omit1st:
            omit1st = False
            continue
        file_name = root_dir + '/' + file
        df0 = pd.read_csv(file_name, header=None)
        df = df0.iloc[1:]
        colname = df0.iloc[0]
        df.columns = colname

        dfST = df[df['model'].str.match('ST')]
        dfHi = df[df['model'].str.match('Hitachi')]
        featuresST = ['smart_1_normalized','smart_1_raw',
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
        featuresHi = ['smart_1_normalized','smart_1_raw',
            'smart_5_normalized','smart_5_raw',
            'smart_3_normalized','smart_3_raw',
            'smart_194_normalized', 'smart_194_raw',
            'smart_196_normalized', 'smart_196_raw',
            'smart_197_normalized', 'smart_197_raw'
            ]

        dfSTcpd=pd.concat([dfST['date'],dfST['serial_number'],dfST[featuresST] ],axis=1)
        dfHicpd=pd.concat([dfHi['date'],dfHi['serial_number'],dfHi[featuresHi] ],axis=1)
        dfSTcpd.dropna(axis=0)
        dfHicpd.dropna(axis=0)
        dfSTcpd.to_csv(path_or_buf=r"/Users/zhilinyang/Desktop/ST_data" + '/ST ' + file)
        dfHicpd.to_csv(path_or_buf=r"/Users/zhilinyang/Desktop/Hi_data" + '/Hi ' + file)






