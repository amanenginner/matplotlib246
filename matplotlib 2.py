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


mtcars.describe()


# In[6]:


# rename column
mtcars=mtcars.rename(columns={'Unnamed: 1':'model'})
mtcars


# # Generating Bar plot of columns  carbs and gear

# In[9]:


# creating plot
y=mtcars['gear']
x= mtcars['carb']
plt.plot(x,y)
plt.xlabel("Number of carburetors")
plt.ylabel("Number of forward gears")
plt.title("carb vs gear")
plt.show()


# In[14]:


#creating bar plot
sns.barplot(x='carb', y='gear', data=mtcars)
plt.xlabel("Number of carburetors")
plt.ylabel("Number of forward gears")
plt.title("carb vs gear")
plt.show()


# In[ ]:




