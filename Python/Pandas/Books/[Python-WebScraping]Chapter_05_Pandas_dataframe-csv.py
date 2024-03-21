# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:25:40 2024

@author: Shin
"""

#!/usr/bin/env python
# coding: utf-8

# # 5장 데이터 처리와 분석을 위한 라이브러리

# ## 5.2 표 데이터 처리에 강한 판다스(pandas)

# ### 5.2.2 표 형식의 데이터 파일 읽고 쓰기

# #### CSV 파일 읽고 쓰기

# [5장: 168페이지]

# In[ ]:
# jupyter notebook
'''
get_ipython().run_cell_magic('writefile', 'C:/myPyScraping/data/ch05/A_product_sales.csv', '연도,1분기,2분기,3분기,4분기\n2016,2412,4032,5183,1139\n2017,2725,4986,6015,1242\n2018,2925,5286,6497,1596\n2019,2691,5813,7202,1358\n2020,2523,6137,7497,1512\n')
'''

# [5장: 169페이지]

# In[ ]:

import pandas as pd

#  CSV 파일 경로
folder = './Books/Data/ch05/' # 폴더 지정
csv_file = folder + 'A_product_sales.csv' # 파일 경로 지정

# CSV 파일을 읽어와서 DataFrame 데이터 생성
df = pd.read_csv(csv_file, encoding = "utf-8") 
df 
'''
 연도   1분기   2분기   3분기   4분기
0  2016  2412  4032  5183  1139
1  2017  2725  4986  6015  1242
2  2018  2925  5286  6497  1596
3  2019  2691  5813  7202  1358
4  2020  2523  6137  7497  1512
'''

# In[ ]:

# 연도 index지정
df = pd.read_csv(csv_file, index_col="연도")
df


# [5장: 171페이지]

# In[ ]:


df = pd.DataFrame({ '고객ID': ['C5001', 'C5002', 'C5003', 'C5004'],
                     '국가':['한국', '미국', '영국', '독일'],
                      '주문금액':[1152000, 2507000, 3698000, 4504100] })
df


# In[ ]:

# 데이터프레임 CSV 파일로 저장
# DataFrame.to_csv(filename)
# CSV 파일 경로 
folder = './Data/ch05/'    # 폴더 지정
csv_file = folder + 'sales_info_x.csv'  # 파일 경로 지정    
# 파일 경로 지정(오른쪽 파일위치 명시적으로 지정 = 저장하고 싶은 위치를 우선적으로
# 지정한 후에 저장가능하다. (여기서 위치는 폴더 위치를 말한다))

df.to_csv(csv_file)                      # DataFrame 데이터를 CSV 파일로 쓰기
print("생성한 CSV 파일:", csv_file)      # 생성한 파일 이름 출력
# excel file 로 읽어올 떄 인코딩이 맞지않아 한글이 꺠진 채 출력됨.
# 파일 포멧을 지정필요(인코딩은 지정불가)
# 한국어로 지정하고 싶다면 파일이름을 sales_info_x_euc-kr.csv 로 변경 후
# edit with notepad -> 인코딩 -> ANSI로 변경
# [5장: 172페이지]

# In[ ]:


# CSV 파일 경로
folder = './Data/ch05/'  
csv_file = folder + 'sales_info_cp949_encoding.csv'

# DataFrame 데이터를 CSV 파일로 쓰기(인코딩은 'cp949', index 포함 안 함)
# encoding: cp949(Windows), (euc-kr)호환, 더 많은 한글 문자를 지원)
# index : False, 인덱스를 생성하지 않고 저장( df 안에 인덱스를 csv_file에 포함x)
df.to_csv(csv_file, encoding="cp949", index=False)
print("생성한 CSV 파일:", csv_file) # 생성한 파일 이름 출력
