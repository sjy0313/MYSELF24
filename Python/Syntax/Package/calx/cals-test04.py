# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:53:33 2024

@author: Shin
"""

# 모듈에서 함수나 변수의 이름을 변경해서 사용할 수 있다.

# from 모듈명 import 함수 as 별칭 
# from 모듈명 import 변수 as 별칭

from cals import PI as pi
from cals import add as plus
from cals import sub as minus


a = 10
b = 20
print(f"더하기({a} + {b}): ", plus(a,b))
print(f"뺴기({b} - {a}): ", minus(b,a))
print(f"원주율(PI): {pi}")

