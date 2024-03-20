# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:52:50 2024

@author: Shin
"""

# 판다스 (데이터프레임은 python기본 패키지에 존재 x)
# 데이터프레임 : Dataframe
# 2차원 배열, 행열(matrix)
# 행 : 인덱스, row index
# 열 : column, Series
# 
# 형식:
# df = pd.DataFrame(data[,index=index_data, columns=columns_data])
# 행/열 삭제

#%%
import pandas as pd
# list
data = [
    # 0    1       2
    [15, '남', '장안중'], # 0행
    [16, '여', '수성중']  # 1행      
        ]

df = pd.DataFrame(data)
print(df)
'''
   0  1    2
0  15  남  장안중
1  16  여  수성중
'''
#%%
# 새로운 인덱스 지정
df.index=['정윤', '희애']
'''
   나이 성별   학교
정윤  15  남  장안중
희애  16  여  수성중
'''
# 새로운 컬럼 지정
df.columns = ['나이', '성별', '학교']
print(df)
'''
    나이 성별   학교
정윤  15  남  장안중
희애  16  여  수성중
'''
#%%
# 인덱스 변경
ndf = df.rename(index={'희애' :'정희'})
print(ndf)
'''
    나이 성별   학교
정윤  15  남  장안중
정희  16  여  수성중
'''
# 원하는 컬럼 변경
ndf = df.rename(columns={'학교':'중학교'})
print(ndf)
'''
  나이 성별  중학교
정윤  15  남  장안중
희애  16  여  수성중
'''
#%%

# 원본 변경 : inplace=True 여러개의 index, colum 값을 바꾸고 싶을 떄 dict형태 + , 활용
# 리턴: None
xdf = ndf.rename(index={'정윤' :'신정윤', '희애':'신정희'},
           columns={'나이':'연령'}, inplace=True)
print(ndf)
'''
 연령 성별  중학교
신정윤  15  남  장안중
신정희  16  여  수성중
'''
print(xdf)  # None 

#%%
# 축(axis)는 n차원 배열을 구성하는 요소
# 행 삭제 : axis = 0 은 행을 의미 / 3차원 배열에서 axis=0은 높이를 의미
# 사실 axis = n으로 불리는 축은 그냥 바깥 리스트에서 안쪽 리스트 순으로 0부터
# 이름 붙인것에 불과합니다.
ndf = df.drop('희애')
print(ndf)
'''
     나이 성별   학교
정윤  15  남   장안중
'''

ndf = df.drop('희애', axis=0)
print(ndf)
#%%

# 열 삭제 : axis = 1 열방향으로 동작하여 axis=1 앞에 index를 지정하여 삭제가능
ndf = df.drop('학교', axis=1)
print(ndf)
'''
    나이 성별
정윤  15  남
희애  16  여
'''











































