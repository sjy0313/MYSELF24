# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:53:33 2024

@author: Shin
"""


# 모듈을 (import)
# cals.py 파이썬 코드를 사용 가능하도록 임포트 한다.
# 모듈명.함수()
import cals
a = 10
b = 20
print(f"더하기({a} + {b}): ", cals.add(a,b))
print(f"뺴기({b} - {a}): ", cals.sub(b,a))
print(f"원주율({cals.PI}): ", cals.PI)

