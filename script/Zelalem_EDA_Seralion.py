#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install findspark


# In[2]:


import findspark 
findspark.init() 
findspark.find() 


# In[3]:


from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc=SparkContext.getOrCreate()
spark=SparkSession(sc)


# In[4]:


import pyspark
import pandas as Pd
import numpy as np
import seaborn as sns
from scipy import stats


# In[5]:


df=spark.read.csv(
path="sierraleone-bumbuna.csv",
header=True,
inferSchema=True,)


# In[6]:


df.distinct().count()


# In[7]:


df.show()


# In[8]:


df.columns[:]


# In[9]:


df=df.dropna(how="any")


# In[ ]:




