
# coding: utf-8

# In[2]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


dir1 = r"/Users/zhilinyang/Desktop/dataset/data_Q1_2017"
dir2 = r"/Users/zhilinyang/Desktop/dataset/data_Q2_2017"
dir3 = r"/Users/zhilinyang/Desktop/dataset/data_Q3_2017"
dir4 = r"/Users/zhilinyang/Desktop/dataset/data_Q4_2017"
root_dir=[dir1,dir2,dir3,dir4]


# In[20]:


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


# In[ ]:


for i in range(0,4): 
   for file in os.listdir(root_dir[i]):
       file_name = root_dir[i] + '/' + file
       df = pd.read_csv(file_name, header=None)
       colname = df.iloc[0]
       df = df.iloc[1:]
       df.columns = colname

       #Select all Seagate A samples and its features
       dfST = df[df['model'].str.match('ST4000DM000')]
       dfST=pd.concat([dfST['date'],dfST['serial_number'],dfST[featuresST],dfST['failure']],axis=1)
       dfST.dropna(axis=0)
       #combine all dates' data into a single file
       dfST.to_csv(path_or_buf=r"/Users/zhilinyang/Desktop/STA_combine.csv", mode='a')


# Here I met a bug: I don't know why there happens to be an addtional empty file called '.DStore' appearing in the 4th folder, and I must skip it

# In[ ]:


#to process the 4th folder and skip the empty one
i=3
omit=True
for file in os.listdir(root_dir[i]):
        if omit:
            omit=False
            continue
        file_name = root_dir[i] + '/' + file
        df = pd.read_csv(file_name, header=None)
        colname = df.iloc[0]
        df = df.iloc[1:]
        df.columns = colname
        #Select all Seagate A samples and its features
        dfST = df[df['model'].str.match('ST4000DM000')]
        dfST=pd.concat([dfST['date'],dfST['serial_number'],dfST[featuresST],dfST['failure']],axis=1)
        dfST.dropna(axis=0)
        #combine all dates' data into a single file
        dfST.to_csv(path_or_buf=r"/Users/zhilinyang/Desktop/STA_combine.csv", mode='a')


# In[3]:


newdf=pd.read_csv("/Users/zhilinyang/Desktop/STA_combine.csv",header=None)
newdf.head()


# In[6]:


colname=newdf.iloc[0]
total_df=newdf.iloc[1:,:]
total_df.columns=colname
total_df.head()


# In[9]:


#The column "failure" is in mixed type and needs type conversion
fail_samples_df=total_df[total_df.failure.astype('int64')==1] 
fail_samples_df.head()


# In[10]:


fail_name_list=fail_samples_df.iloc[:,1]
print(len(fail_name_list))
fail_name_list.head()


# 1072 failed samples in total

# In[37]:


sample = total_df[total_df.iloc[:,1].str.match('Z3029FAS')]
sample.head()


# Next I intend to plot the time series to see whether there is truly a significant changepoint. Use the 100th sample as an example:

# In[63]:


from jupyterthemes import jtplot
jtplot.style(theme='solarizedl')
indicator_list=['smart_1_raw','smart_7_raw','smart_240_raw','smart_242_raw']
for ind in indicator_list:
    plt.plot(sample['date'], sample[ind], ':r',lw=3)
    y_ticks=np.linspace(0,len(sample[ind]),5)
    plt.yticks(y_ticks)
    plt.xlabel(ind)
    plt.show()


# In[39]:


sample2 = total_df[total_df.iloc[:,1].str.match('Z3015SZN')]
print('done')


# In[71]:


sample2 = total_df[total_df.iloc[:,1].str.match('Z3015SZN')]
indicator_list=['smart_1_raw','smart_7_raw','smart_240_raw','smart_242_raw']
for ind in indicator_list:
    plt.plot(sample2['date'], sample2[ind], ':r',lw=3)
    y_ticks=np.linspace(0,len(sample2[ind]),5)
    plt.yticks(y_ticks)
    plt.xlabel(ind)
    plt.show()


# As we can see, the indicators' values don't change as a significant shift but rise linearly?

# In[25]:


#because the first few samples don't have enough records
fail_name_list=fail_name_list[51::]


# In[47]:


import changepy
from changepy import pelt
from changepy.costs import normal_meanvar
for feature in featuresST:
    data = (pd.to_numeric(sample[feature])).values
    changepoint=np.mean(pelt(normal_meanvar(data), len(data)))    
    day_before_fail=len(data)-changepoint
    print(feature,day_before_fail)
    #print(feature,days)
    


# In[ ]:




