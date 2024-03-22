#!/usr/bin/env python
# coding: utf-8

# # 5장 데이터 처리와 분석을 위한 라이브러리

# ## 5.2 표 데이터 처리에 강한 판다스(pandas)

# #### 엑셀 파일 읽고 쓰기

# [5장: 174페이지]

# In[ ]:


import pandas as pd

# 엑셀 파일 경로
folder = './data/'
excel_file = folder + 'CES마켓_주문내역.xlsx'

# 엑셀 파일을 읽어서 DataFrame 데이터 생성
df = pd.read_excel(excel_file)  # read_excel file이 openyxl을 쓰고 있음 .
# ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.
# 이런식으로 패키지 설치가 안된것이 발견이 되면 anaconda powershell에서 
# 본인이 마든 가상환경 anaconda navigator의 이름인 YSIT24 를 실행
# conda activate YSIT24
# pip install 다운이필요한 패키지 이름
df
'''
     주문번호 주문지역       주문일자  제품유형        고객ID 고객등급
0  351291   서울 2022-07-04    의류  EeNMuRpdzG    A
1  351292   경기 2022-07-05   컴퓨터  H7o4KJizTE    B
2  351293   강원 2022-07-06   식료품  OEA4cDdkyg    A
3  351294   호남 2022-07-07  주방제품  GGe6nkrlnV    C
4  351295   영남 2022-07-08    여행    jTrJPdZA    B
5  351296   충청 2022-07-09    도서   Fjs00aZuo    C
'''
# [5장: 175페이지]

# In[ ]:


df = pd.read_excel(excel_file, index_col='주문번호') 
# df = pd.read_excel(excel_file, index_col=0) # 이 방법도 가능

df

# [5장: 177페이지]

# In[ ]:


# 판다스 DataFrame 데이터 생성
df1 = pd.DataFrame({ '제품ID':['P1001', 'P1002', 'P1003', 'P1004'],
                     '판매가격':[5000, 7000, 8000, 10000],
                     '판매량':[50, 93, 70, 48]}  )

df2 = pd.DataFrame({ '제품ID':['P2001', 'P2002', 'P2003', 'P2004'],
                     '판매가격':[5200, 7200, 8200, 10200],
                     '판매량':[51, 94, 72, 58]}  )

df3 = pd.DataFrame({ '제품ID':['P3001', 'P3002', 'P3003', 'P3004'],
                     '판매가격':[5300, 7300, 8300, 10300],
                     '판매량':[52, 95, 74, 68]}  )

df4 = pd.DataFrame({ '제품ID':['P4001', 'P4002', 'P4003', 'P4004'],
                     '판매가격':[5400, 7400, 8400, 10400],
                     '판매량':[53, 96, 76, 78]}  )
df1


# [5장: 178페이지]

# In[ ]:


# 엑셀 파일 경로
folder = './data/'
excel_file = folder + '제품_판매현황_1.xlsx'

# DataFrame 데이터를 엑셀 파일로 쓰기
df1.to_excel(excel_file) 

print("생성한 엑셀 파일:", excel_file) # 생성한 파일 이름 출력


# [5장: 179페이지]

# In[ ]:


# 엑셀 파일 경로
folder = './data/'
excel_file = folder + '제품_판매현황_2.xlsx'

# DataFrame 데이터를 엑셀로 쓰기(옵션 지정)
df1.to_excel(excel_file, sheet_name='제품_라인업1', index=False) 

print("생성한 엑셀 파일:", excel_file) # 생성한 파일 이름 출력


# In[ ]:

# pip install xlswriter
# 엑셀 파일 경로
folder = './data/' 
excel_file = folder + '제품_판매현황_two_sheets.xlsx' 

# DataFrame 데이터를 엑셀 파일의 '제품_라인업1'와 '제품_라인업2' 시트에 쓰기
with pd.ExcelWriter(excel_file, engine='xlsxwriter') as excel_writer:
    df1.to_excel(excel_writer, sheet_name='제품_라인업1', index=False)
    df2.to_excel(excel_writer, sheet_name='제품_라인업2', index=False)
# context manager    
print("생성한 엑셀 파일:", excel_file) # 생성한 파일 이름 출력


# [5장: 180페이지]

# In[ ]:

# 출력할 엑셀 파일 경로
folder = './data/' 
excel_file = folder + '제품_판매현황_전체_one_worksheet.xlsx' 

# 1) 생성한 객체(excel_writer)를 이용해 DataFrame 데이터(df)를 쓰기
excel_writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

# 2) 여러 DataFrame 데이터를 하나의 엑셀 워크시트에 위치를 달리 해서 출력
df1.to_excel(excel_writer) # startrow=0, startcol=0 과 동일
df2.to_excel(excel_writer, startrow=0, startcol=5, index=False)
df3.to_excel(excel_writer, startrow=6, startcol=0)
df4.to_excel(excel_writer, startrow=6, startcol=5, index=False, header=False)

# 3) 객체를 닫고 엑셀 파일로 저장       
#excel_writer.save()
excel_writer.close()
print("생성한 엑셀 파일:", excel_file) # 생성한 파일 이름 출력


#%%
# ### 5.2.3 표 데이터 선택

# #### 행 데이터 선택

# [5장: 183페이지]

# In[ ]:


import pandas as pd
import numpy as np

index_data = ['a', 'b', 'c', 'd', 'e'] # index용 데이터
data = [0.0, 1.0, 2.0, 3.0, 4.0] # 데이터
s1 = pd.Series(data, index = index_data)
s1


# In[ ]:


s1.loc['a'] # index 라벨 지정으로 하나의 행 데이터 선택


# In[ ]:


s1.loc[['a', 'c', 'e']] # index 라벨 리스트 지정으로 여러 행의 데이터를 선택


# In[ ]:


s1.loc[['e', 'b', 'a']] # index 라벨 리스트 지정으로 여러 행의 데이터를 선택


# [5장: 184페이지]

# In[ ]:


s1.loc['b':'d'] # index 라벨 슬라이싱으로 여러 행의 데이터를 선택


# In[ ]:


s1.iloc[1] # index 위치 지정으로 하나의 행 데이터를 선택


# In[ ]:


s1.iloc[[0, 2, 4]] # index 위치 리스트 지정으로 여러 행의 데이터를 선택


# In[ ]:


s1.iloc[1:4] # index 위치 슬라이싱으로 여러 행의 데이터를 선택


# In[ ]:


s1.loc['a':'c'] = 10 # 여러 행의 데이터에 스칼라 값을 지정
s1


# [5장: 185페이지]

# In[ ]:


s1.iloc[3:5] = 20
s1


# In[ ]:


dict_data = {'A': [0, 10, 20, 30, 40],
             'B': [0, 0.1, 0.2, 0.3, 0.4],
             'C': [0, 100, 200, 300, 400]} # 딕셔너리 데이터

index_data = ['a', 'b', 'c', 'd', 'e'] # index 지정용 데이터

df1 = pd.DataFrame(dict_data, index=index_data) # 딕셔너리 데이터로부터 DataFrame 데이터 생성
df1


# In[ ]:


df1.loc['a'] # index 라벨 지정으로 하나의 행 데이터를 선택


# [5장: 186페이지]

# In[ ]:


df1.loc[['a', 'c', 'e']] # index 라벨 리스트 지정으로 여러 행의 데이터를 선택


# In[ ]:


df1.loc['b':'d'] # index 라벨 슬라이싱으로 여러 행의 데이터를 선택


# In[ ]:


df1.iloc[2] # index 위치 지정으로 하나의 행 데이터를 선택


# In[ ]:


df1.iloc[[1, 3, 4]] # index 위치 리스트 지정으로 여러 행의 데이터를 선택


# [5장: 187페이지]

# In[ ]:


df1.iloc[1:3] # index 위치 슬라이싱으로 여러 행의 데이터를 선택


# In[ ]:


df1.loc['a':'c'] = 50
df1


# [5장: 188페이지]

# In[ ]:


# Series 데이터 생성
s = pd.Series(range(-3, 6)) 
s


# In[ ]:


# DataFrame 데이터 생성
dict_data = {'지점': ['서울', '대전', '대구', '부산', '광주'],
             '1월': [558, 234, 340, 380, 213],
             '2월': [437, 216, 238, 290, 194], 
             '3월': [337, 196, 209, 272, 186]} # 딕셔너리 데이터

df = pd.DataFrame(dict_data) # 딕셔너리 데이터로부터 DataFrame 데이터 생성
df


# In[ ]:


s[s > 0] # 조건을 만족하는 행 데이터 가져오기


# [5장: 189페이지]

# In[ ]:


s[(s >= -2) & (s%2 == 0)] # 두 조건을 모두 만족하는 행 데이터 가져오기 


# In[ ]:


df[df['1월'] >= 300] # 조건을 만족하는 행 데이터 가져오기


# In[ ]:


df[(df['지점'] == '서울') | (df['지점'] == '부산')] # 둘 중 하나만 만족해도 행을 선택


# [5장: 190페이지]

# In[ ]:


df[df['지점'].isin(['서울','부산'])]


# In[ ]:


dict_data = { '제품ID':['P501', 'P502', 'P503', 'P504', 'P505', 'P506', 'P507'],
              '판매가격':[6400, 5400, 9400, 10400, 9800, 1200, 3400],
              '판매량':[63, 56, 98, 48, 72, 59, 43],
              '이익률':[0.30, 0.21, 0.15, 0.25, 0.45, 0.47, 0.32]}  # 딕셔너리 데이터

df2 = pd.DataFrame(dict_data)
df2


# [5장: 191페이지]

# In[ ]:


df2.head() # 처음 5개의 행 데이터 선택


# In[ ]:


df2.head(2) # 처음 2개의 행 데이터 선택


# [5장: 192페이지]

# In[ ]:


df2.tail() # 마지막 5개의 행 데이터 선택


# In[ ]:


df2.tail(3) # 마지막 3개의 행 데이터 선택


# In[ ]:


with pd.option_context('display.max_rows',4):
    pd.set_option("show_dimensions", False)
    display(df2)


# #### 열 데이터 선택

# [5장: 193페이지]

# In[ ]:


df2['제품ID']


# [5장: 194페이지]

# In[ ]:


df2[['제품ID']]


# In[ ]:


df2[['제품ID', '이익률', '판매가격']]


# [5장: 195페이지]

# In[ ]:


# 지정한 열 데이터의 모든 값을 스칼라 값으로 변경
df2['이익률'] = 0.5 # '이익률' 열 데이터를 0.5로 변경
df2


# #### 행과 열 데이터 선택

# In[ ]:


dict_data = {'A': [0, 1, 2, 3, 4],
             'B': [10, 11, 12, 13, 14],
             'C': [20, 21, 22, 23, 24]} # 딕셔너리 데이터

index_data = ['a', 'b', 'c', 'd', 'e'] # index 지정용 데이터

df = pd.DataFrame(dict_data, index=index_data) # DataFrame 데이터 생성
df


# [5장: 196페이지]

# In[ ]:


df.loc['a', 'A'] # loc 이용


# In[ ]:


df.iloc[0, 0] # iloc 이용


# In[ ]:


df.loc['a':'c', ['A', 'B']] # loc 이용


# In[ ]:


df.iloc[0:3, 0:2] # iloc 이용


# [5장: 197페이지]

# In[ ]:


df.loc[:, ['A', 'B']] # loc 이용


# In[ ]:


df.iloc[:, 0:2] # iloc 이용


# In[ ]:


df.loc[df['A']>2, ['A', 'B']] # loc 이용


# [5장: 198페이지]

# In[ ]:


df.loc['a':'c', ['A', 'B']] = 50 # 스칼라 값 지정
df


# In[ ]:


df.iloc[3:5, 1:3] = 100 # 스칼라 값 지정
df


# In[ ]:


df.loc[df['B']<70, 'B'] = 70 # 스칼라 값 지정
df


# [5장: 199페이지]

# In[ ]:


df.loc[df['C']<30, 'D'] = 40 # loc 이용. 스칼라 값 지정
df


# ### 5.2.4 표 데이터 통합

# [5장: 200페이지]

# In[ ]:


import pandas as pd

s1 = pd.Series([10, 20, 30])
s1


# In[ ]:


s2 = pd.Series([40, 50, 60])
s2


# In[ ]:


s3 = pd.Series([70, 80, 90])
s3


# In[ ]:


# 세로 방향으로 연결
pd.concat([s1, s2])


# [5장: 201페이지]

# In[ ]:


# 기존 index를 무시하고 새로운 index를 생성
pd.concat([s1, s2], ignore_index=True) 


# In[ ]:


# 기존 index를 무시하고 새로운 index를 생성
pd.concat([s1, s2, s3], ignore_index=True) 


# [5장: 202페이지]

# In[ ]:


df1 = pd.DataFrame({'물리':[95, 92, 98, 100],
                    '화학':[91, 93, 97, 99]})
df1


# In[ ]:


df2 = pd.DataFrame({'물리':[87, 89],
                    '화학':[85, 90]})
df2


# In[ ]:


df3 = pd.DataFrame({'물리':[72, 85]})
df3


# In[ ]:


df4 = pd.DataFrame({'생명과학':[94, 91, 94, 83],
                    '지구과학':[86, 94, 89, 93]})
df4


# [5장: 203페이지]

# In[ ]:


# 세로 방향으로 연결(기존 index를 무시)
pd.concat([df1, df2], ignore_index=True)


# In[ ]:


# 세로 방향으로 연결(기존 index를 무시)
pd.concat([df2, df3], ignore_index=True) 


# [5장: 204페이지]

# In[ ]:


# 세로 방향으로 공통 데이터만 연결(기존 index를 무시)
pd.concat([df2, df3], ignore_index=True, join='inner')


# In[ ]:


# 가로 방향으로 연결
pd.concat([df1, df4], axis=1)


# In[ ]:


# 가로 방향으로 모든 데이터 연결
pd.concat([df2, df4], axis=1) 


# [5장: 205페이지]

# In[ ]:


# 가로 방향으로 공통 데이터만 연결
pd.concat([df2, df4], axis=1, join='inner')


# ## 5.3 정리
