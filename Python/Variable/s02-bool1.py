# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:08:40 2024

@author: Shin
"""

# 논리형(boolean) : bool
# TRUE : 참
# FALSE : 거짓

#%%

t= True
f= False

print(type(t), t) #<class 'bool'> True
print(type(f), f) #<class 'bool'> False
#%%
tf = t == f
ft = f != t 
print(tf) # False
print(ft) # True
#%%
a = 1 == 2
b = 1 != 2
print(a, b) # False True

             