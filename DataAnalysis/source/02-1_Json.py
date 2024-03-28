# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:25:05 2024

@author: Shin
"""

#!/usr/bin/env python
# coding: utf-8

# # 02-1 API 사용하기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/02-1.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/02-1.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 파이썬에서 JSON 데이터 다루기

# In[1]:


# dict
d = {"name": "혼자 공부하는 데이터 분석"}

print(d['name'])


# In[2]:
# 파이썬 객체를 json문자열로 변환
# json.dumps()
# json.dump() 함수는 다음과 같은 매개변수를 받습니다:
'''
obj: 직렬화할 Python 객체입니다.

fp: JSON 데이터를 쓸 파일 객체입니다.

skipkeys: 딕셔너리의 키가 비 원시형(숫자, 문자열, 불리언, None)이 아닌 경우 에러를 발생시키지 않고 
건너뜁니다(기본값은 False).
ensure_ascii: False로 설정하면 ASCII 이외의 문자도 출력됩니다. 기본값은 True입니다.
check_circular: 객체의 순환 참조를 확인할지 여부를 결정합니다(기본값은 True).
allow_nan: NaN, Infinity 및 -Infinity와 같은 비유효한 숫자 값을 허용할지 여부를 결정합니다(기본값은 True).
indent: JSON 출력의 들여쓰기 수준입니다. None이 아닌 경우, 값이 주어진 만큼 들여쓰기됩니다. 
들여쓰기 수준이 0보다 큰 경우, 들여쓰기로 표시된 각 수준당 1개의 탭 문자가 사용됩니다. 
정수 값은 들여쓰기 수준을 나타내고 문자열 값은 해당 문자열이 사용됩니다(기본값은 None).
separators: 항목과 항목, 키와 값, 및 구분 기호 사이의 문자열을 각각 지정합니다(기본값은 (', ', ': ')).
'''
import json



# In[3]:
# dict -> json
d_str = json.dumps(d)
# ensure_ascii=False: ascii문자 외에 다른 문자는 16진수로 출력되는 막음
# 일반적으로 JSON 라이브러리는 문자열을 JSON으로 인코딩할 때 ASCII 문자 이외의
# 문자를 유니코드 이스케이프 시퀀스로 변환합니다. 이는 ASCII 이외의 문자를 안전하게 
#전송하고 저장하기 위한 방법

d_str = json.dumps(d, ensure_ascii=False)
print(d_str)
# {"name": "혼자 공부하는 데이터 분석"}

# In[4]:


print(type(d_str)) # <class 'str'>


# In[5]:


d2 = json.loads(d_str)

print(d2['name']) # 혼자 공부하는 데이터 분석


# In[6]:


print(type(d2)) # <class 'dict'>


# In[7]:


d3 = json.loads('{"name": "혼자 공부하는 데이터 분석", "author": "박해선", "year": 2022}')

print(d3['name']) # 혼자 공부하는 데이터 분석
print(d3['author'])# 박해선
print(d3['year']) # 2022


# In[8]:
# 띄어쓰기 조심 " 한칸 띄워주고 \ 
#파이썬에서는 여러 줄 문자열을 사용할 때 역슬래시(\)를 사용하여 줄을 연결해야 합니다
# 문자열이 길어서 다음 라인으로 연결 : 역슬래시(\)
d3 = json.loads('{"name": "혼자 공부하는 데이터 분석", \
                "author": ["박해선","홍길동"],\
                  "year": 2022}')

print(d3['author'][1]) # 홍길동
print(d3['author'][0]) # 박해선


# In[9]:

# \n 줄바꿈 문자열
d4_str = """ 
[
  {"name": "혼자 공부하는 데이터 분석", "author": "박해선", "year": 2022},
  {"name": "혼자 공부하는 머신러닝+딥러닝", "author": "박해선", "year": 2020}
]
"""
d4 = json.loads(d4_str)

print(d4[0]['name']) # 혼자 공부하는 데이터 분석
print(d4[1]['name']) # 혼자 공부하는 머신러닝+딥러닝
# In[10]:


import pandas as pd
# json 문자열 -> 판다스 데이터프레임으로 생성
pd_d4 = pd.read_json(d4_str)
print(pd_d4)


# In[11]:

# 결과는 같음.
#[pd_d4_11 = pd.DataFrame(d4)] = [pd_d4 = pd.read_json(d4_str)]
