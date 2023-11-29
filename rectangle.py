#!/usr/bin/env python
# coding: utf-8

# In[8]:


class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth= breadth
    def area(self):
        return(self.length*self.breadth)
    def perimeter(self):
        return(2*(self.length+self.breadth))
ob = rectangle(10,20)
ar=ob.area()
print(ar,ob.perimeter())   


# In[ ]:




