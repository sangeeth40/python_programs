#!/usr/bin/env python
# coding: utf-8

# In[3]:


try:
    f=open("file2.txt","w")
   
    try:
        f.write("additional text")
    finally:
        f.close()
        print("file is closed")
except:
    print("error")
    


# In[ ]:




