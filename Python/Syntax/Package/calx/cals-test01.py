# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:53:33 2024

@author: Shin
"""

# 가장 많이 씀(한번에 바꾸기) . 개별 모듈을 바꾸는 경우는 잘 없음 .
# 모듈을 (import)
# cals.py 파이썬 코드를 사용 가능하도록 임포트 한다.
# 모듈명.함수()
import calx.cals # as 를 통해 별칭을 주는 것임
# import 모듈이름 as 별칭
# 별칭.함수(), 별칭.함수


a = 10
b = 20
print(f"더하기({a} + {b}): ", calx.cals.add(a,b))
print(f"뺴기({b} - {a}): ", calx.cals.sub(b,a))
print(f"원주율({calx.cals.PI}): ", calx.cals.PI)

