#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = input()


# In[2]:


numz = num.split(",")


# In[3]:


print (numz)


# In[4]:


print (numz[0])


# In[5]:


numz= num.split(',')


# In[6]:


print (numz[0])


# In[10]:


c= 50
h = 30
outno = []
for i in numz :
    d = int(i)
    y= (2*c*d)/h
    outno.append(y)
    


# In[11]:


print (outno)


# In[ ]:




