#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Importing pandas profile
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Importing dataset
mtcars=pd.read_csv("D:\cars-1.csv")
mtcars.head()


# In[3]:


# rename column
mtcars=mtcars.rename(columns={'Unnamed: 1':'model'})
mtcars


# In[4]:


mtcars.info()


# In[ ]:




