#!/usr/bin/env python
# coding: utf-8

# # visualize the data
# mtcars.csv dataset with various plots.
# 

# In[1]:


# Importing all required packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import pandas_profile

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Importing dataset
mtcars=pd.read_csv("D:\cars-1.csv")
mtcars.head()


# In[3]:


mtcars.describe()


# In[4]:


mtcars.head(10)


# In[5]:


mtcars.tail()


# In[6]:


mtcars.tail(10)


# In[7]:


mtcars.shape


# In[8]:


#print concise summary of the columns
mtcars.info(null_counts=True)


# In[9]:


mtcars.mean


# In[10]:


mtcars.median


# In[11]:


#standard deviation
mtcars.std()


# In[12]:


#maximum of each attribute
mtcars.max()


# In[13]:


#minimum of each attribute 
mtcars.min()


# In[14]:


# number of non-null records in each column
mtcars.count()


# In[15]:


# rename column
mtcars=mtcars.rename(columns={'Unnamed: 1':'model'})
mtcars


# # GENERATINF PLOT OF MODEL VS HP

# In[16]:


# creating plot
y=mtcars['hp']
x= mtcars['model']
plt.plot(x,y)
plt.xlabel("model")
plt.ylabel("hp")
plt.title("Model Names vs Horse Power")
plt.figure(figsize=(32, 12))
display(plt.plot(x, y))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




