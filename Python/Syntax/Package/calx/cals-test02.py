# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:53:33 2024

@author: Shin
"""


# 모듈을 (import)
# from 모듈명 import 목록 (모듈이름 생략가능)
from cals import * # calc에 있는 모든 함수, 변수를 사용(전체모듈 가져오기)


a = 10
b = 20
print(f"더하기({a} + {b}): ", add(a,b))
print(f"뺴기({b} - {a}): ", sub(b,a))
print(f"원주율(PI): {PI}")

