# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:06:01 2024

@author: Shin
"""

# 내장함수(Built-In-Function)
# 파이썬을 설치할 떄 기본적으로 제공하는 모듈

# enumerate : 열거
lst = ['body', 'foo','bar']
#%%
# 리스트에서 요소를 하나씩 꺼내줌
for l in lst:
    print(l)
    
#%%
# 리스트의 인덱스 처리
for n in range(len(lst)): # n: 0,1,2
    val = lst[n] #리스트에 인덱스를 통해서 값을 참조
    print(f"인덱스({n}), ({val})")
   # 인덱스(0), (body)
   # 인덱스(1), (foo)
   # 인덱스(2), (bar)
#%%

# enumerate를 통해서 인덱스와 요소의 값을 동시에 처리
#Enumerate 메서드는 파이썬의 Enumerate 목록에 있는 각 항목에 대한 
#자동 카운터/인덱스와 함께 제공됩니다. 
#첫번째 인덱스 값은 0부터 시작합니다. enumerate에서 선택적 
#매개변수 startIndex를 사용하여 인덱스의 시작점을 지정할 수도 있습니다.

for n, val in enumerate(lst):
    print(f"인덱스({n}), ({val})")
    