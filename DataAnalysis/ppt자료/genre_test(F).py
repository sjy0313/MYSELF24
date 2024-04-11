# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:54:33 2024

@author: Shin
"""

# genre_creator는 년도 별 액셀파일에 따라 달라지는 장를 추출 module이다
# excel파일을 웹에서 다운받아 '판매상품ID'에 해당하는 열을 교보문고에서 
#상세페이지로 이동할 수 있는 https://product.kyobobook.co.kr/detail/ 과 결합하여
# 상세페이지에서 장르 정보만 따와서 excel 파일로 저장해주는 모듈이다.

# 변수 line: 
#   19 : 저장된 액셀파일
#   197: 저장할 액셀파일 이름 변경(연도)


# 제품코드 추출위해(제품코드가 html상 존재x) 액셀파일 불러오기:
import pandas as pd
df = pd.read_excel("./project/Genrelist_of_bestseller2023(1).xlsx") # 교보문고 액셀파일 불러오기
df.head()
#%%
# 1위 부터 100위까지 상세페이지 링크 리스트자료형으로 변환.
# glist = 판매상품ID를 list자료형으로 변환
glist = df['판매상품ID'].tolist()
# 상세페이지 format
# [https://product.kyobobook.co.kr/detail/] + ['판매상품ID']   
# genre_link(glist) : 100개의 상세페이지 링크 완성하는 함수
# genre_data : 100개 상세페이지 링크

def genre_link(glist):
    genre_data = []
    sampleurl = "https://product.kyobobook.co.kr/detail/"
    for pid in glist:
        genre_data.append(sampleurl + str(pid))
    return genre_data

glist = df['판매상품ID'].tolist()
genre_data = genre_link(glist)
print(genre_data)
#%%

# spyder 과부화 방지를 위해 상세페이지링크 20개씩 끊어줌. 
# s_list 20개씩 리스트로 변환(list안에 list) 
split_data = [
    genre_data[0:20],
    genre_data[20:40],
    genre_data[40:60],
    genre_data[60:80],
    genre_data[80:100]
]
print(split_data)
#%%
# 0~20개 상세페이지에서 장르 추출(dict자료형으로 추출)
# genre_list1 : 상세페이지에서 장르(0~20개)에 대한 정보를 담을 []
# chunk1 : 상세페이지 링크 20개
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 

driver = Chrome() 

genre_list1 = []
chunk1 = split_data[0]

for url in chunk1:
    driver.get(url) 
    driver.implicitly_wait(3) # 3초대기(웹로드)
            
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
            
    genre_elements = soup.find_all('a', attrs={'class': 'btn_sub_depth'})
    # 구성요소값 4개 구성
    if len(genre_elements) >= 2: # 구성요소 2개 이상일 떄
        second_genre = genre_elements[1].text.strip() # 요소값 중 2번 째 값 공백제거 후 추출
        genre_list1.append({'장르': second_genre})

driver.quit()

#%%  
# 21~40개 상세페이지링크에 대한 장르정보
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 
from selenium.webdriver.chrome.options import Options 

# 크롬옵션객체를 생성하여 파이썬 내부에서 작업처리
chrome_options = Options()
chrome_options.add_argument("--headless") 
driver = Chrome(options=chrome_options)

genre_list2 = []
chunk2 = split_data[1]


for url in chunk2:
    driver.get(url)
    driver.implicitly_wait(3)
            
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
            
    genre_elements = soup.find_all('a', attrs={'class': 'btn_sub_depth'})
    if len(genre_elements) >= 2: 
        second_genre = genre_elements[1].text.strip()
        genre_list2.append({'장르': second_genre})

driver.quit()

#%%
# 41~60개 상세페이지링크에 대한 장르정보
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = Chrome(options=chrome_options)

genre_list3 = []
chunk3 = split_data[2]

for url in chunk3:
    driver.get(url)
    driver.implicitly_wait(3)
            
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
            
    genre_elements = soup.find_all('a', attrs={'class': 'btn_sub_depth'})
    if len(genre_elements) >= 2: 
        second_genre = genre_elements[1].text.strip()
        genre_list3.append({'장르': second_genre})

driver.quit()

#%%
# 61~80개 상세페이지링크에 대한 장르정보
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = Chrome(options=chrome_options)

genre_list4 = []
chunk4 = split_data[3]

for url in chunk4:
    driver.get(url)
    driver.implicitly_wait(3)
            
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
            
    genre_elements = soup.find_all('a', attrs={'class': 'btn_sub_depth'})
    if len(genre_elements) >= 2: 
        second_genre = genre_elements[1].text.strip()
        genre_list4.append({'장르': second_genre})

driver.quit()

#%%
# 81~100개 상세페이지링크에 대한 장르정보
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = Chrome(options=chrome_options)


genre_list5 = []
chunk5 = split_data[4]

for url in chunk5:
    driver.get(url)
    driver.implicitly_wait(3)
            
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
            
    genre_elements = soup.find_all('a', attrs={'class': 'btn_sub_depth'})
    if len(genre_elements) >= 2: 
        second_genre = genre_elements[1].text.strip()
        genre_list5.append({'장르': second_genre})

driver.quit()

#%%
# excel 파일로 변환
import pandas as pd
combined_data = genre_list1 + genre_list2 + genre_list3 + genre_list4 + genre_list5
Genre_dataframe = pd.DataFrame(combined_data)

Genre_dataframe.to_excel('./Project/Genrelist_of_bestseller2023(1).xlsx', index=False)