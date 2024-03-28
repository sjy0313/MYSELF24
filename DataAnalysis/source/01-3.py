#!/usr/bin/env python
# coding: utf-8

# # 01-3 이 도서가 얼마나 인기가 좋을까요?

# <table class="tfo-notebook-buttons" align="left">
#   <td>
#     <a target="_blank" href="https://nbviewer.jupyter.org/github/rickiepark/hg-da/blob/main/01-3.ipynb"><img src="https://jupyter.org/assets/share.png" width="61" />주피터 노트북 뷰어로 보기</a>
#   </td>
#   <td>
#     <a target="_blank" href="https://colab.research.google.com/github/rickiepark/hg-da/blob/main/01-3.ipynb"><img src="https://www.tensorflow.org/images/colab_logo_32px.png" />구글 코랩(Colab)에서 실행하기</a>
#   </td>
# </table>

# ## 도서 데이터 찾기

# [공공데이터포털](https://www.data.go.kr/)
# 
# 도서관 정보나루의 [남산도서관 장서/대출 목록](https://www.data4library.kr/openDataV?libcode=4707)

# ## 코랩에서 데이터 확인하기

# In[4]
# 패키지 설치 목록
#conda activate YSIT24
#pip install gdown
#pip install xlsxwriter
import gdown

gdown.download('https://www.data4library.kr/openDataV?libcode=4707', 
               './data/서울특별시교육청남산도서관 장서 대출목록 (2024년 02월).csv', quiet=False)
# quiet= 이 모드는 스크립트를 실행할 때 특히 유용하며, 보다 간결한 출력을 원할 때 사용
# 일반적으로 "False" 상태는 더 간결한 것을 의미합니다
# ## 파이썬으로 CSV 파일 출력하기

# In[5]:


with open('./data/남산도서관 장서 대출목록 (2021년 04월).csv') as f:
    print(f.readline())


# In[11]:

# open() 함수는 파일 경로와 함께 사용되며, 파일의 경로는 파일이 위치한 디렉토리와 파일 이름을 지정합니다. 
# './data/남산도서관 장서 대출목록' 이 파일을 읽을 때 r(읽기모드), w(쓰기[편집]모드: 덮어쓰기), 
#a(쓰기[편집]모드: 내용추가) 모드들을 적용가능하며

# readline()은 파일에서 한 줄씩만 읽기 때문에 for 루프를 사용하여 각 줄을 처리해야 합니다.

fp = open('./data/남산도서관 장서 대출목록 (2021년 04월).csv')
for rd in fp.readline():
    print(rd)
fp.close()



# In[ ]:

#  mode='rb': 파일 내용은 이진 데이터로 처리 (이진 모드는 텍스트가 아닌 데이터를 처리할 때 사용)
# 파일 인코딩 형식 확인

# readline() 함수는 파일 객체의 메서드 중 하나로, 파일에서 한 줄을 읽어옵니다.
#  readline() 함수 대신 readlines() 메서드를 사용하여 한 번에 모든 줄을 읽어올 수도 있습니다. 
# 이 경우 반환되는 값은 각 줄을 요소로 가지는 리스트입니다.
import chardet

with open('./data/남산도서관 장서 대출목록 (2021년 04월).csv', mode='rb') as f:
    d = f.readline()

print(chardet.detect(d))
# {'encoding': 'EUC-KR', 'confidence': 0.99, 'language': 'Korean'}

# In[ ]:


with open('./data/남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr') as f:
    print(f.readline()) 
#   번호,도서명,저자,출판사,발행년도,ISBN,세트 ISBN,부가기호,권,주제분류번호,도서권수,대출건수,등록일자,
    print(f.readline())
#   "1","인공지능과 흙","김동훈 지음","민음사","2021","9788937444319","","","","","1","0","2021-03-19",

# In[ ]:


# 파일명 처리 방식
# MacOS : NFD: ㅎ ㅏ ㄴ ㄱ ㅡ ㄹ  "Normalization Form Canonical Decomposition"의 약어입니다. 
# 이는 유니코드 문자열을 정규화하는 방법 중 하나입니다. 유니코드는 문자를 다양한 방식으로 표현 할 수 있다
# NFD는 문자를 정규화할 때, 기본 문자와 결합 문자를 분리하여 표현합니다.
# 예를 들어, "한글"이라는 문자열은 "ㅎ"과 "ㅏ", "ㄴ", "ㄱ", "ㅡ", "ㄹ" 등으로 구성됩니다

# Windows, Linux : NFC(Normalization Form Canonical[표준적인] Composition):한글
#
import os
import glob
import unicodedata

for filename in glob.glob('./data/*.csv'):
  nfc_filename = unicodedata.normalize('NFC', filename)
  os.rename(filename, nfc_filename) # filename ->  nfc_filename 변환
  print("filename:", filename) # ./data\남산도서관 장서 대출목록 (2021년 04월).csv
  print("nfc_filename:", nfc_filename)


# ## 데이터프레임 다루기: 판다스

# In[ ]:


import pandas as pd


# In[ ]:


df = pd.read_csv('./data/남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr')
# 컬럼정보(5,6,9)
# 컬럼 5 : ISBN
# 컬럼 6 : 세트 ISBN
# 컬럼 9 : 주제분류번호(정수, 실수들이 섞여있음)
'''
DtypeWarning: Columns (5,6,9) have mixed types. 
Specify dtype option on import or set low_memory=False.
위 경고가 나오는 이유
판다스에서 CSV 파일을 읽을 떄 분활해서 읽음(csv는 데이터타입을 따로 구분해서 읽어오진 않는다)
데이터타입을 자동으로 인식을 한다
그 때 분활해서 읽은 데이터들의 자료형이 일치하지 않으면 발생되는 경고
'''
# df = pd.read_csv('your_file.csv', dtype={'column_name1': str, 'column_name2': int, ...})
# dtype 매개변수를 이용해 명시적으로 데이터 타입을 지정해줄 수 있다.
# In[ ]:


df = pd.read_csv('./data/남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr',
                 low_memory=False) 
# low_memory -> 데이터를 분활해서 읽지말고 한번에 읽기

# In[ ]:


df.head()


# In[ ]:
# dtype : 
# 파일을 읽을 떄 자동으로 컬럼의 자료형을 유추하지 않도록 
# 명시적으로 칼럼의 타입을 지정
df = pd.read_csv('./data/남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr',
                 dtype={'ISBN': str, '세트 ISBN': str, '주제분류번호': str})
df.head()


# In[ ]:

#csv 파일로 다시 읽기

df.to_csv('./data/ns_202104.csv')

#인코딩(utf-8)로 저장
# 추가
import chardet

with open('./data/ns_202104.csv', mode='rb') as f:
    d = f.readline()

print(chardet.detect(d))
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
# In[ ]:

    
with open('./data/ns_202104.csv', encoding="utf-8") as f:
    for i in range(3):
        print(f.readline(), end='')


# In[ ]:

# Unnamed : 0 -> index_col=0 -> 0
ns_df = pd.read_csv('./data/ns_202104.csv', low_memory=False)
ns_df.head()


# In[ ]:

# 첫 번쨰(0) 컬럼을 인덱스로 지정
ns_df = pd.read_csv('./data/ns_202104.csv', index_col=0, low_memory=False)
ns_df.head()


# In[ ]:

# 저장할 떄 인덱스를 제외 = 원본과 같아짐(quatation mark 사라짐"")
df.to_csv('./data/ns_202104_noindex.csv', index=False)


# In[ ]:


# 코랩을 사용하는 경우 xlsxwriter 패키지를 설치해 주세요.
# get_ipython().system('pip install xlsxwriter')


# In[ ]:


ns_df.to_excel('./data/ns_202104.xlsx', index=False, engine='xlsxwriter')

print("엑셀 파일 생성 종료")
#%%

ns_df.to_html('./data/ns_202104.xlsx', index=False)






