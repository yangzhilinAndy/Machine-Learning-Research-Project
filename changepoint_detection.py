import pandas as pd
import numpy as np
from cpdetect import cpDetector
df0=pd.read_csv("/Users/zhilinyang/Desktop/combST.csv",header=None)
#df1=pd.read_csv("/Users/zhilinyang/Desktop/combHi.csv",header=None)
colname = df0.iloc[0]
df0 = df0.iloc[1:]
df0.columns = colname

featuresST_norm = ['smart_1_normalized',
            'smart_5_normalized',
            'smart_7_normalized',
            'smart_184_normalized',
            'smart_189_normalized',
            'smart_190_normalized',
            'smart_193_normalized',
            'smart_194_normalized',
            'smart_197_normalized',
            'smart_198_normalized']

change_point_df=pd.DataFrame()

sample='Z305B2QN'
df=df0.loc[df0['serial_number'].str.match(sample)]
df.columns = colname
dates = list(df.loc[:, 'date'])
asample = pd.DataFrame()


for feature in featuresST_norm:
    time_series = np.asarray(df.loc[:,feature])
    time_series = [time_series.astype(np.float)]
    detector = cpDetector(time_series, distribution='normal', log_odds_threshold=0)
    detector.detect_cp()
    detector.to_csv('/Users/zhilinyang/Desktop/cpd.csv')
    newdf = pd.read_csv('/Users/zhilinyang/Desktop/cpd.csv',header=None)
    colname = newdf.iloc[0]
    newdf = newdf.iloc[1:]
    newdf.columns = colname
    cpd=list(newdf['ts'])
    change_points=[dates[int(pt)] for pt in cpd]
    change_points = pd.Series(change_points)
    print(change_points)
    asample=pd.concat([asample,change_points],axis=1,ignore_index=True)
asample.columns=[0]+featuresST_norm
print(asample.head())
