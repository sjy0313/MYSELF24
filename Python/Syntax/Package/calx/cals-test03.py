# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:53:33 2024

@author: Shin
"""


# from 모듈명 import 목록 
# 해당 모듈애서 목록을 지정 
# from cals import * 
from cals import add, sub, PI


a = 10
b = 20
print(f"더하기({a} + {b}): ", add(a,b))
print(f"뺴기({b} - {a}): ", sub(b,a))
print(f"원주율(PI): {PI}")

