#!/usr/bin/env python
# coding: utf-8

# In[23]:


class Bank:
    def __init__(self,name,typeOfBank,balance):
        self.name=name
        self.typeOfBank=typeOfBank
        self.balance=balance
    def deposit(self,dep):
        self.balance+=dep
        print("money deposited succesfully")
    def withdraw(self,amt):
        if amt>self.balance:
            print("insuffient balance")
        else:
            self.balance-=amt
            print("money withdrawed")
person1=Bank("a","sbi",2000)
print(person1.balance)
person1.deposit(100)
print(person1.balance)
person1.withdraw(500)
print(person1.balance)

        


# In[ ]:




