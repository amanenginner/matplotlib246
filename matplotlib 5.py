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


# # AREA CHART FOR THE COLUMNS AM AND CARB

# In[4]:


# creating plot
x= mtcars['wt']
y=mtcars['carb']
plt.stackplot(x,y)
plt.xlabel("Transmission")
plt.ylabel("Number of carburetors")
plt.title("Transmission vs Number of carburetors")
plt.show()


# In[ ]:




