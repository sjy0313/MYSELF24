# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:34:10 2024

@author: Shin
"""

# genre_creator는 년도 별 액셀파일에 따라 달라지는 장를 추출 module이다
# excel파일을 웹에서 다운받아 '판매상품ID'에 해당하는 열을 교보문고에서 
#상세페이지로 이동할 수 있는 https://product.kyobobook.co.kr/detail/ 과 결합하여
# 상세페이지에서 장르 정보만 따와서 excel 파일로 저장해주는 모듈이다.

# 변수 line: 
#   19 : 저장된 액셀파일


# 제품코드 추출위해(제품코드가 html상 존재x) 액셀파일 불러오기:
import pandas as pd
df = pd.read_excel("C:/Users/신정윤/Documents/Python/새 폴더/MYSELF24/DataAnalysis/project/Genrelist_of_bestseller2020.xlsx") # 교보문고 액셀파일 불러오기

#%%
# 1위 부터 100위까지 상세페이지 링크 리스트자료형으로 변환.
# glist = 판매상품ID를 list자료형으로 변환
glist = df['판매상품ID'].tolist()
# 상세페이지 format
# [https://product.kyobobook.co.kr/detail/] + ['판매상품ID']   
# genre_link(glist) : 100개의 상세페이지 링크 완성하는 함수 
# genre_data : 상세페이지 링크

def genre_link(glist):
    genre_data = []
    sampleurl = "https://product.kyobobook.co.kr/detail/"
    for pid in glist:
        genre_data.append(sampleurl + str(pid))
    return genre_data

genre_data = genre_link(glist)
print(len(genre_data))
  
#%%
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 
from selenium.webdriver.chrome.options import Options 

# 크롬옵션객체를 생성하여 파이썬 내부에서 작업처리
chrome_options = Options()
chrome_options.add_argument("--headless") 
driver = Chrome(options=chrome_options)


genre_list = []
chunk = genre_data

url_cnt = 0

for url in chunk:
    url_cnt += 1
    print("url_cnt:", url_cnt, url)
    driver.get(url)
    driver.implicitly_wait(3)
            
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    print('soup:', soup != None)
            
    genre_elements = soup.find_all('a', attrs={'class': 'btn_sub_depth'})
    print(len(genre_elements))
    if genre_elements != None:
        if len(genre_elements) >= 2: 
            second_genre = genre_elements[1].text.strip()
            genre_list.append({'장르': second_genre})
    else:
        genre_list.append({'장르': '절판'})
    

driver.quit()

#%%

# excel 파일로 변환
Genre_dataframe = pd.DataFrame(genre_list)
Genre_dataframe.to_excel("C:/Users/신정윤/Documents/Python/새 폴더/MYSELF24/DataAnalysis/project/Genrelist_of_bestseller2020.xlsx", index=False)