
# coding: utf-8

# In[37]:


import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score


# In[38]:


X_train=pd.read_csv('/Users/zhilinyang/Desktop/train_x_A.csv',header=None)
X_train=X_train.iloc[1:]
len(X_train)


# In[39]:


X_train.head()


# In[40]:


y=[0 for i in range(0,1000)]+[1 for i in range(0,480)]
y_train=np.array(y)
y_train


# In[44]:


y_train_df=pd.DataFrame(y_train,index=range(1,1481))
y_train_df.head()


# In[45]:


dataset=pd.concat([X_train,y_train_df],axis=1,ignore_index=True)
dataset.head()


# In[21]:


from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()


# In[5]:


scores=cross_val_score(estimator=lr,X=X_train,y=y_train,cv=100,n_jobs=2)
print('CV accuracy: %.3f +/- %.3f' % (np.mean(scores),np.std(scores)))


# In[6]:


X_train_norm=X_train[[0,2,4,6,10,12,14,16,18,20]]
X_train_raw=X_train[[1,3,5,7,8,9,11,13,15,17,19,21,22,23]]
print(X_train_norm.shape)
print(X_train_raw.shape)


# In[7]:


scores=cross_val_score(estimator=lr,X=X_train_raw,y=y_train,cv=100,n_jobs=2)
print('x_train_raw CV accuracy: %.3f +/- %.3f' % (np.mean(scores),np.std(scores)))


# In[8]:


scores=cross_val_score(estimator=lr,X=X_train_norm,y=y_train,cv=100,n_jobs=2)
print('x_train_norm CV accuracy: %.3f +/- %.3f' % (np.mean(scores),np.std(scores)))


# In[44]:


scores=cross_val_score(estimator=lr,scoring='precision',X=X_train_norm,y=y_train,cv=100,n_jobs=2)
print('CV precision: %.3f +/- %.3f' % (np.mean(scores),np.std(scores)))


# As we can see, using normalised features makes a little improvement in the accuracy score of Logistic Regression. But the precision is 0!!! What happened? Let's improve some parameters by GridSearch. For LR, the most commonly used parameter may be about regularisation.

# In[9]:


from sklearn.model_selection import GridSearchCV


# In[10]:


param_range=[0.0001,0.001,0.01,0.1,1.0,10.0,100.0,1000.0]
param_grid=[{'C':param_range}]
gs=GridSearchCV(estimator=lr,param_grid=param_grid,cv=10,n_jobs=-1)
gs=gs.fit(X_train, y_train)
print(gs.best_score_)


# Still too low! Let's try another algorithm

# In[11]:


from sklearn.ensemble import RandomForestClassifier
forest=RandomForestClassifier()
RFscores=cross_val_score(estimator=forest,scoring='precision',X=X_train_norm,y=y_train,cv=100,n_jobs=2)
print('RF CV precision: %.3f +/- %.3f' % (np.mean(RFscores),np.std(RFscores)))


# In[12]:


from sklearn.tree import DecisionTreeClassifier
DT=DecisionTreeClassifier()
DTscores=cross_val_score(estimator=DT,scoring='precision',X=X_train_norm,y=y_train,cv=100,n_jobs=2)
print('DT CV precision: %.3f +/- %.3f' % (np.mean(DTscores),np.std(DTscores)))


# In[13]:


from sklearn.ensemble import GradientBoostingClassifier
GBDT=GradientBoostingClassifier()
GBDTscores=cross_val_score(estimator=GBDT,scoring='precision',X=X_train_norm,y=y_train,cv=100,n_jobs=2)
print('GBDT CV precision: %.3f +/- %.3f' % (np.mean(GBDTscores),np.std(GBDTscores)))


# In[14]:


from sklearn.svm import SVC
SVM = SVC()
SVMscores=cross_val_score(estimator=SVM,scoring='precision',X=X_train_norm,y=y_train,cv=100,n_jobs=2)
print('SVM CV precision: %.3f +/- %.3f' % (np.mean(SVMscores),np.std(SVMscores)))


# In[15]:


from rgf.sklearn import RGFClassifier


# In[ ]:


RGF = RGFClassifier(max_leaf=400,algorithm="RGF_Sib",test_interval=100,verbose=True)
RGFscores=cross_val_score(estimator=RGF,scoring='accuracy',X=X_train_norm,y=y_train,cv=100,n_jobs=2)


# In[21]:


print('RGF CV accuracy: %.3f +/- %.3f' % (np.mean(RGFscores),np.std(RGFscores)))


# In[ ]:


from sklearn.learning_curve import learning_curve
import matplotlib.pyplot as plt
train_sizes, train_scores, test_scores =learning_curve(estimator=RGF, X=X_train_norm, y=y_train, 
               train_sizes=np.linspace(0.7,1.0,10),cv=10,n_jobs=1)
train_mean=np.mean(train_scores, axis=1)
test_mean=np.mean(test_scores, axis=1)


# In[29]:


plt.plot(train_sizes, train_mean, color='blue', marker='o',label='training accuracy')
plt.plot(train_sizes, test_mean, color='red', marker='s',label='validation accuracy')
plt.grid()
plt.xlabel('Number of training samples')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()


# In[50]:


dataset=dataset.sample(frac=1)
X_train2=dataset.iloc[:,0:24]
y_train2=dataset[24]


# In[51]:


y_train2=np.array(y_train2)
print(y_train2)


# In[52]:


from sklearn.svm import SVC
SVM = SVC()
SVMscores=cross_val_score(estimator=SVM,scoring='precision',X=X_train2,y=y_train2,cv=100,n_jobs=2)
print('SVM CV precision: %.3f +/- %.3f' % (np.mean(SVMscores),np.std(SVMscores)))


# In[53]:


from sklearn.ensemble import GradientBoostingClassifier
GBDT=GradientBoostingClassifier()
GBDTscores=cross_val_score(estimator=GBDT,scoring='precision',X=X_train2,y=y_train2,cv=100,n_jobs=2)
print('GBDT CV precision: %.3f +/- %.3f' % (np.mean(GBDTscores),np.std(GBDTscores)))

