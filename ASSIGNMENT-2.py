#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
ecom = pd.read_csv('Ecommerce Purchases.csv')
ecom


# In[2]:


ecom.head()


# In[3]:


ecom.info()


# In[4]:


ecom['Purchase Price'].mean()


# In[5]:


ecom['Purchase Price'].max()


# In[6]:


ecom['Purchase Price'].min()


# In[7]:


ecom[ecom['Language']=='en'].count()


# In[8]:


ecom[ecom['Job'] == 'Lawyer'].info()


# In[9]:


ecom['AM or PM'].value_counts()


# In[11]:


ecom['Job'].value_counts().head(5)


# In[12]:


ecom[ecom['Lot']=='90 WT']['Purchase Price']


# In[13]:


ecom[ecom["Credit Card"] == 4926535242672853]['Email']


# In[14]:


ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()


# In[15]:


sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25')


# In[16]:


ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)


# In[ ]:




