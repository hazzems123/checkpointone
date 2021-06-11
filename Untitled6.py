#!/usr/bin/env python
# coding: utf-8

# In[1]:


def missing_char(word,index) :
    x = word.split("")
    x.pop(index)
    x.join()
    


# In[17]:


name = 'kitten'
ind = 1
x= ''


# In[34]:


def missing_char(word,index) :
    x = list (word)
    x.pop(index)
    x= ''.join(x)
    return x
    


# In[35]:


missing_char(name,ind)


# In[ ]:





# In[ ]:




