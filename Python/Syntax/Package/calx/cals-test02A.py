# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:53:33 2024

@author: Shin
"""

# from 패키지.모듈명 import 목록
# 패턴 5
from calx import * # calc에 있는 모든 함수, 변수를 사용(전체모듈 가져오기)

#폴더 이름을 생략하고 사용
#모듈.함수()
a = 10
b = 20
print(f"더하기({a} + {b}): ", calx.add(a,b))
print(f"뺴기({b} - {a}): ", calx.sub(b,a))
print(f"원주율(PI): {calx.PI}")

