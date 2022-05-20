#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import pickle 


# In[11]:


df = pd.read_csv('cardio_train.csv' , sep=';')
df


# In[12]:


df.info()


# In[13]:


df['cardio'].value_counts()


# In[14]:


x = df[['age' , 'gender' , 'height' , 'weight' , 'ap_hi' , 'ap_lo' , 'cholesterol' , 'gluc' , 'smoke' , 'alco' ,'active']]
x


# In[15]:


y=df['cardio']
y


# In[16]:


from sklearn.neighbors import KNeighborsClassifier 


# In[17]:


clf= KNeighborsClassifier (n_neighbors= 33,weights="distance")
clf.fit(x,y)


# In[18]:


clf.predict(x[69296:])


# In[19]:


print(clf.predict(np.array([5 ,2 , 150 ,50.5 ,110 , 75 , 2 ,2 , 1 , 1, 1]).reshape(1,-1)))


# In[22]:


pickle .dump(clf ,open('trainedModel.sav' , 'wb'))


# In[23]:


model= pickle.load(open('trainedModel.sav' , 'rb'))