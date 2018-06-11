
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


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


# In[3]:


df=pd.read_csv("/Users/zhilinyang/Desktop/STA_combine.csv",header=None)
colname = df.iloc[0]
df = df.iloc[1:]
df.columns = colname
df.head()


# In[4]:


x_train=pd.DataFrame()
sample_list=df['serial_number'].unique()
len(sample_list)


# In[7]:


sample=df[df.iloc[:,1].str.match('Z3029FAS')]
for i in range(1,len(sample)):
    arr=(sample['smart_7_normalized'].ewm(span=i).mean()).values
    print(arr[-1])


# By observation, the weighted average will not be affected largely by the choice of window width. Hence, I intend to choose the mean value of possible width.

# In[ ]:


num=9300
x_train=pd.DataFrame()
for sample_name in sample_list[9300:]:
    sample=df.groupby(['serial_number']).get_group(sample_name)
    train_sample=[]
    i=(1+len(sample))/2
    for feature in featuresST:
        arr=(sample[feature].ewm(span=i).mean()).values
        train_sample.append(arr[-1])
    train_vals=(pd.DataFrame(train_sample)).T
    x_train=x_train.append(train_vals,ignore_index=True)
    num=num+1
    print(num)


# In[6]:


x_train.to_csv(path_or_buf='/Users/zhilinyang/Desktop/x_train.csv',index=False, mode='a')
print('done')

