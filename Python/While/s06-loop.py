# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:50:47 2024

@author: Shin
"""

# 문제 
# 구구단 프로그램을 작성하라
for n in range(1,10):
    print(f"{n}단")
    for s in range(1,10):
        result = n * s
        print(f"{n} * {s} = {result}")
    print()
    
# 2번쨰 방법
for x in range(2,10):
    for y in range(1,10):
        print("%2d" % (x * y), end=' ')
    print()

# 3번쨰 방법
for x in range(2,10):
    print(f"[{n}단]", end=' ')
    for y in range(1,10):
        print(f"{x*y}", end=' ')
    print()
    
    \\