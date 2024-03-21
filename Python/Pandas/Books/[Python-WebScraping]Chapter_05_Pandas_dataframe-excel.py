# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:25:03 2024

@author: Shin
"""

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