# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 13:59:42 2024

@author: Shin
"""
#%%
s= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sl = len(s)

# 스탭: 기본값 1칸
s0 = s[::]
s1 = s[::1]
print(s0) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(s1) # ABCDEFGHIJKLMNOPQRSTUVWXYZ

#%%
# 처음부터 끝까지 2칸 간격으로 건너뛰기 
s2 = s[::2]
print(s2) # ACEGIKMOQSUWY
