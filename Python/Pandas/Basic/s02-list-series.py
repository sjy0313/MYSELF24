    `# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 11:15:17 2024

@author: Shin
"""
# Pandas p152 파이썬 webscraping 완벽가이드

import pandas as pd 

lst = ['2024-03-20', 3.14, 'ABC', 100, True]
# 원하는 인덱스 지정시 시리즈에서 index= [], []안에 원하는 값 넣어주기
sr = pd.Series(lst, index=['날짜', '원주율', '알파벳', '숫자', '존재'])
# series 기본형 = pd.Series(lst[,index = index_data])
#  기본형 = pd.Series(lst) # index 지정하지 않으면 0~ 정수형으로 index 출력
print(sr)
"""
날짜     2024-03-20
원주율          3.14
알파벳           ABC
숫자            100
존재           True
dtype: object
"""
 # 리스트는 시리즈의 값으로 지정
 # 인덱스 : 0부터 순차적으로 지정
 # 값 : 리스트가 지정
 #%%
 # 시리즈에서 인덱스 속성 참조
print(sr.index) # Index(['날짜', '원주율', '알파벳', '숫자', '존재'], dtype='object')

#%%
# 시리즈에서 값 속성 참조
print(sr.values) # ['2024-03-20' 3.14 'ABC' 100 True] 
#%%
# reindex() : 재배열
# 새로운 인덱스 지정
# 기존 데이터는 바뀌지 않고 새로운 시리즈를 생성. 
sr.reindex(['존재', '날짜', '원주율', '알파벳', '숫자'])
"""
존재           True
날짜     2024-03-20
원주율          3.14
알파벳           ABC
숫자            100
dtype: object
"""
#%%

#loc
# 인덱스로 값을 참조
print(sr['원주율']) # 3.14 
print(sr.loc['원주율']) # 3.14 location

#%%

#iloc
# 순번으로 값을 참조
print(sr.iloc[1]) # iloc = index location # 3.14

#%%
# 권고하지 않음 명시적으로 순서로접근하는 것인지 순서로 접근하는 것인지 
# 위 sr.loc[] or sr.loc[]를 활용하여 명시적으로 명령을 해주어야함.
print(sr[1]) 
# 3.14
'''
C:\Users\Shin\AppData\Local\Temp\ipykernel_10292\2091009225.py:1
: FutureWarning: Series.__getitem__ treating keys as positions is deprecated.
 In a future version, integer keys will always be treated as labels 
 (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`
  print(sr[1])
'''

#%%
sr1 = pd.Series(lst, index=[1,2,3,4,5])
print(sr1)
'''
1    2024-03-20
2          3.14
3           ABC
4           100
5          True
dtype: object
'''
print(sr1[2]) # 3.14
print(sr1[0]) # KeyError: 0 # 인덱스로 값을 참고한 것은 맞으나 애러발생
# 인덱스값을 문자열로 지정되어있지만 default 값이 0~4로 인덱싱 되어있음.
print(sr[0]) #  2024-03-20
#%%
# 인덱스 다중 선택 
print(sr['원주율', '알파벳'])
# KeyError: 'key of type tuple not found and not a MultiIndex'
print(sr[['원주율', '알파벳']]) # series 에게 하나의 값으로 전달 []으로 한번 더 
# 묶어주기
'''
원주율    3.14
알파벳     ABC
dtype: object
'''

#%%
# 인덱스 다중 선택 : 범위지정
print(sr['원주율':'숫자'])
























