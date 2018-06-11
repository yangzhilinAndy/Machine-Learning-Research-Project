
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# In[19]:


train_df=pd.read_csv('/Users/zhilinyang/Desktop/x_train.csv',header=None)
train_df=train_df.iloc[1:]
train_df.head()


# In[28]:


len(train_df)


# In[27]:


df=pd.read_csv("/Users/zhilinyang/Desktop/STA_combine.csv",header=None)
colname = df.iloc[0]
df = df.iloc[1:]
df.columns = colname
df.head()


# In[29]:


sample_list=df['serial_number'].unique()


# In[37]:


fail_list=df[df['failure'].astype('int64')==1].iloc[:,1]
len(fail_list)


# In[44]:


state=(pd.Series(sample_list)).isin(fail_list)
state[state==False]=0
train_df['state']=state[:15031]
train_df.head(8)


# In[46]:


healthy_sample=train_df[train_df['state']==0]
print(len(healthy_sample))
fail_sample=train_df[train_df['state']==1]
print(len(fail_sample))


# In[49]:


healthy_train_x=healthy_sample.iloc[:,:24]
healthy_train_x.head()


# In[50]:


k_means=KMeans(n_clusters=100,n_init=10,max_iter=300,tol=1e-04,random_state=0)
dist=k_means.fit_transform(healthy_train_x)
x_dist=pd.DataFrame(dist)


# In[51]:


x_dist.head()


# In[ ]:


down_sample=np.array([])
for center in range(0,100):
    arrange=x_dist.sort_values(by=center, axis=0, ascending=True, inplace=False)
    down_sample=np.append(down_sample,arrange[center].index.values[:10])
down_sample


# In[60]:


train_x_A=healthy_train_x.iloc[down_sample]
train_x_A=train_x_A.append(fail_sample.iloc[:,:24])
len(train_x_A)


# 1000 healthy sample with 480 failed sample

# In[65]:


train_x_A.to_csv(path_or_buf='/Users/zhilinyang/Desktop/train_x_A.csv',index=False)

