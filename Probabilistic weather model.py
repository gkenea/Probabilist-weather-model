#!/usr/bin/env python
# coding: utf-8

# In[52]:


import numpy as np
from matplotlib import pyplot as plt


# In[53]:


A = np.array([[0.5, 0.5, 0.25], [0.25, 0, 0.25], [0.25, 0.5, 0.5]])


# In[54]:


print(A)


# In[55]:


xtoday = np.array([[1], [0], [0]])


# In[56]:


print(xtoday)


# In[57]:


print(A@xtoday)


# In[58]:


the_weather = np.zeros((3, 50))
the_weather[:,0] = xtoday[:,0]
for k in range(50):
    xtommorow = A@xtoday
    the_weather[:,k] = xtommorow[:,0]
    print(k)
    print(xtommorow)
    xtoday = xtommorow


# In[59]:


plt.plot(the_weather.transpose())
plt.grid(True)


# Goshu kenea

# In[ ]:





# In[ ]:




