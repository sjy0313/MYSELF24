# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:52:46 2024

@author: Shin
"""

# 자료형 지정
# 힌트(hint): 제약 조건은 아니며 참고사항
# 파이썬 3.5부터 지원하는 어노테이션
# typing모듈의 활용하여 디테일한 타입 설정을 할 수 있다

# 변수나 인수의 경우 변수명과 = 사이에 : 타입을 적어서 표시하고, 
#함수의 반환값의 경우 함수 블록이 시작하기 직전에 -> 타입으로 적어서 표시합니다.
# def something(num: int = 10) -> Time: # something의 인수는 num이고 어노테이션 된 타입은 int
#     w: Watch = notExistFunction()# 지역변수 w 어노테이션 된 타입 Watch
#     return w.time + num
#%%
# 어떤 타입이든 가능
from typing import Any
x: Any = 100
y: Any = 0.123
print(x,type(x)) # 100 <class 'int'>
print(y,type(y)) # 0.123 <class 'float'>

# 정수
age: int = 100
# 실수
px: float = 0.1234
# 불리언
tf: bool = True
# 문자열
tel: str = "010-1234=5678"

print(age,px,tf,tel) # 100 0.1234 True 010-1234=5678

#%%
# list
from typing import List
# 리스트형의 요소는 정수
# type은 리스트형이지만 []안에 정수 int처리 하여 도출
lst: List[int] = [1,3,5,7,8]
print(lst,type(lst))  # [1, 3, 5, 7, 8] <class 'list'>
#%%
# tuple
from typing import Tuple
# 튜플형의 요소는(문자열,실수)
tp: Tuple[str,float] = ('원주율', 3.14159)
print(tp,type(tp)) # ('원주율', 3.14159) <class 'tuple'>
#%%
# dict
from typing import Dict
# 딕셔너리형의 요소는 
user: Dict[str,str] = {"이름": "홍길동", "주소":"한양"}
print(user)# {'이름': '홍길동', '주소': '한양'}
#%%
# set
from typing import Set
st: Set[int] = {2,4,6,8,10}
print(st) # {2, 4, 6, 8, 10}

#%%

# 파라미터: 리스트[정수]
# 리턴 : 정수
def sumx(nums: List[int]) -> int: # -> int 정수라는 힌트를 알려줌. sumx의 인수는 nums이고 어노테이션 된 타입은
# list[]이며 []의 객체는 int 임을 명시, 함수의 반환값은 int
    tot: int = 0
    for n in nums:
        tot += n
    return tot
   
print(sumx([1,3,5,7,9])) # 25