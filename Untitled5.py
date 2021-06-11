#!/usr/bin/env python
# coding: utf-8

# In[65]:


n = 8
x=0
dict = {}


# In[71]:





# In[80]:


def dictfunc (n) :
     if n ==1 :
        dict[n] = n
        return dict
     else :     
        x = n*n 
        dict[n]=x
       
        return dictfunc(n-1)
       
        


# In[81]:


f =dictfunc(n)


# In[82]:


print (f)


# In[ ]:




