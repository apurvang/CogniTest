#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Example: sample input = [1,2,2,3,3,4,5]; expected output = [1,2,3,4,5,2,3]


# In[22]:


##sol for 1
list1=[2,1,2,2,3,3,4,5]
s1=set(list1)
list2=[]
for i in s1:
    list2.append(i)

for s in s1:
    if(list1.count(s)>1):
        for i in range(list1.count(s)-1):
            list2.append(s)
        

print(list2)       


# In[18]:


list2


# In[2]:


#Example: input = [1,2,3,4,5]; expected output = [5,4,3,2,1]


# In[1]:


####sol for 2
list1=[1,2,3,4,5,2]
#list1[::-1]
list2=[]
#for i in list1

def reverse(list1):
    #print(list1)
    if(len(list1)>0):
        #print("in")
        list2.append(list1.pop())
        reverse(list1)
    else:
        exit()

reverse(list1)
print(list2)


# In[ ]:




