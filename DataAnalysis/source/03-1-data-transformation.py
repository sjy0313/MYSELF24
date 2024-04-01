# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:53:38 2024

@author: Shin
"""

#!/usr/bin/env python
# coding: utf-8

# # 03-2 잘못된 데이터 수정하기

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/03-2.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/03-2.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 데이터프레임 정보 요약 확인하기

# In[ ]:


import gdown

gdown.download('https://bit.ly/3GisL6J', './data/ns_book4.csv', quiet=False)


# In[ ]:


import pandas as pd

ns_book4 = pd.read_csv('./data/ns_book4.csv', low_memory=False)
ns_book4.head()


# In[ ]:


ns_book4.info() # 열마다 NaN이 아닌 값이 몇 개나 있는지 확인 가능.


# In[ ]:


ns_book4.info(memory_usage='deep')
# memory usage: 298.2 MB
#  Pandas의 info() 메서드가 데이터 프레임의 메모리 사용량을 보고할 때 보다 정확한 값을 제공
# 이 모드에서는 문자열 열의 경우 실제 문자열 데이터를 계산하고, 파이썬 객체를 구성하는 더 많은 세부 정보를 고려
# ## 누락된 값 처리하기

# In[ ]:
# ns_book4.columns !=
# isna() 매서드는 각 행이 비어 있는지를 나타내는 boolean array 를 반환 
# notna() 정상적인 값들을 반환
# 정리하자면, num(NaN)>1 -> dropna()매서드를 활용하며 열을 삭제할 떄는 
# axis= 1 지정하고 how 매개변수에 all을 지정하면 NaN이 들어간 모든 열을 삭제함
# drop()으로 열을 삭제하려면 axis= 1과 삭제하려는 열을 지정해주어야함.
# ns_book = ns_df.drop(['부가기호','Unnamed: 13'], axis=1)
# 삭제할 열이 여러 개 일떄 ex) [col1,col2] 리스트안에 열 지정

# 행을 삭제할 떄도 drop()매서드를 활용할 수 있으며 axis= 0 으로 지정(but, 기본값이 0이므로 지정할 필요x)
# []연산자에 slicing/boolean 을 전달하면 행을 선택가능 ex)  slicing -> ns_book[2:]/[0:2]
# boollean array -> 선택_열 = ns_df['출판사'] == '한빛미디어'->  생성될df = 기존df[선택열] 

# 출판사가 '한빛미디어'인 행만 출력
# groupby() 그룹핑을 할 떄 dropna는 NaN의 포함여부에 따라 나뉘는데 false를 지정하면 NaN값 유지
# duplicated()로 boolean 연산자를 생성할 떄 (위에 행 선택하여 boolean 나열만드는 로직과 동일)
# 중복된 행을 True로 표시 df.duplicated(subset=[col1,col2,col3]) -> 
# 중복되지 않은 고유의 행을 True 표시 = ~df.duplicated(subset=[col1,col2,col3])
# 새로운_df = 기존df[~df.duplicated(subset=[col1,col2,col3])]copy() -> 고유한 행만 선택
# copy()를 사용x -> df이 별도의 메모리 공간에 저장되는지 보장x -> 데이터가 바뀔 수도 있어
# 일부 열/행을 선택하여 업데이트 할 떄는 항상 복사하는 것이 좋음.

#%%

ns_book4.isna().sum()
'''
번호              0
도서명           403
저자            198
출판사          4641
발행년도           14
ISBN            0
세트 ISBN    328015
부가기호        74205
권          321213
주제분류번호      19864
도서권수            0
대출건수            0
등록일자            0
dtype: int64
'''
ns_notna_sum = ns_book4.notna().sum()
print(ns_notna_sum)
'''
번호         384591
도서명        384188
저자         384393
출판사        379950
발행년도       384577
ISBN       384591
세트 ISBN     56576
부가기호       310386
권           63378
주제분류번호     364727
도서권수       384590
대출건수       384591
등록일자       384591
dtype: int64
'''
# In[ ]:

# int64
ns_book4.loc[0, '도서권수'] = None
ns_book4.loc[0, '도서권수'] # nan
ns_book4['도서권수'].isna().sum() # 1


# In[ ]:


ns_book4.head(2)


# In[ ]:
# 특정컬럼의 자료형 확인
# DataFrame['컬럼'].dtype
ns_book4.loc[0, '도서권수'] # 1
print('도서권수의 자료형:', ns_book4['도서권수'].dtype) # 도서권수의 자료형: int64
print('대출건수의 자료형:', ns_book4['대출건수'].dtype) # 대출권수의 자료형: float64
ns_book4.info() #  10  도서권수     384591 non-null  int64  
#%%

# 자료형 변환
# astype을 활용하여 자료형을 변환할 수 있다.
ns_book4.loc[0, '도서권수'] = 1
ns_book4 = ns_book4.astype({'도서권수':'int32', '대출건수': 'int32'})
ns_book4.head(2)


# In[ ]:

# 자료형이 문자열(object)에 None을 넣으면 값은 None
ns_book4.loc[0, '부가기호'] = None
ns_book4.head(2)


# In[ ]:

# numpy package에서 np.nan을 가져왔음 위의 none-> nan처리 
# pandas에서는 NaN이라는 값을 따로 가지지 않음. 
import numpy as np

ns_book4.loc[0, '부가기호'] = np.nan
ns_book4.head(2)


# In[ ]:
# 누락된 값 바꾸기 : loc, fillna()매서드
# isna()는 각행이 비어 있는지를 나타내는 boolean 배열로 반환
# sum()을 이어서 호출하면 boolean 배열의 True개수로 비어있는 행의 개수를 얻음. 
set_isbn_na_rows = ns_book4['세트 ISBN'].isna() # 누락된 값을 찾아 불리언 배열로 변환
ns_book4.loc[set_isbn_na_rows, '세트 ISBN'] = '' # 누락된 값을 빈 문자열로 바꿈. 

ns_book4['세트 ISBN'].isna().sum() # 329015


# In[ ]:
# nan을 지정된 값으로 모두 채움
# nan -> '없음'


ns_book4.fillna('없음').isna().sum()


# In[ ]:
# 지정된 column에서 nan을 지정된 값으로 채움
# isna().sum()을 수행하면 zero 
ns_book4['부가기호'].fillna('없음').isna().sum() # 0


# In[ ]:

# 지정된 column에서 nan을 지정된 값으로 채우고 
# 전체 df을 대상으로 isna,sum처리
ns_book4.fillna({'부가기호':'없음'}).isna().sum()
'''
번호                 0
도서명              403
저자               198
출판사             4641
발행년도            14
ISBN               0
세트 ISBN          328015
부가기호  @@@@@@@@   0      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
권          321213
주제분류번호      19864
도서권수            1
대출건수            0
등록일자            0
dtype: int64
'''
# In[ ]:
# 여러값을 대상으로 처리
# np.nan -> '없음'
# '2021' -> '21'
# 리스트 형태로 지정
ns_book4.replace(np.nan, '없음').isna().sum()


# In[ ]:

# 지정된 column만 변경 : 리스트 형태로 지정
# np.nan -> '없음'
# '2021' -> '21'
ns_book4.replace([np.nan, '2021'], ['없음', '21']).head(2)


# In[ ]:

# 딕셔너리 형태로 지정 
# np.nan -> '없음'
# '2021' -> '21'
ns_book4.replace({np.nan: '없음', '2021': '21'}).head(2)


# In[ ]:

# 열이름으로 지정하고 특정한 값을 대체
# replace({열이름: 원래값}, 새로운 값)
ns_book4.replace({'부가기호': np.nan}, '없음').head(2)


# In[ ]:

# 다중의 열이름으로 지정하고 특정한 값을 대체
ns_book4.replace({'부가기호': {np.nan: '없음'}, '발행년도': {'2021': '21'}}).head(2)
