#!/usr/bin/env python
# coding: utf-8

# In[9]:


import csv
with open('movies.csv','r') as file:
    reader= csv.reader(file, delimiter="\t")
    for row in file:
        print(row)


# In[ ]:




