#!/usr/bin/env python
# coding: utf-8

# # Assignment 1 Q-11

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


x = pd.Series([34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56])
x


# # mean

# In[5]:


x.mean()


# # median

# In[6]:


x.median()


# # varience

# In[7]:


x.var()


# # Standard Deviation

# In[8]:


x.std()


# In[9]:


plt.boxplot(x)


# In[ ]:




