#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
try:
    number=int(input("Enter a Number "))
except ValueError:
    print ("The entered value does not contain numbers\n")
result={}

if(number%3==0):
    result['flag']='G'
    if(number%5==0):
        result['flag']='GN'
elif(number%5==0):
    result['flag']='N'
else:
    result.clear
    result=number

with open('result.json','w') as jsonwriter:
    json.dump(result,jsonwriter)

