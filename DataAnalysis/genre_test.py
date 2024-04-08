# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:29:57 2024

@author: Shin
"""

import pandas as pd
df = pd.read_excel("./source/data/bestseller_books_2023.xlsx") # 교보문고 액셀파일 불러오기
df.head()

#%%
df_id = df[['판매상품ID']]
# glist = 판매상품 아이디를 list자료형으로 변환
glist = df['판매상품ID'].tolist()
print(glist)


pid1 = df_id.iloc[0].values[0]  
pid1
url2 = f"https://product.kyobobook.co.kr/detail/{pid1}"  # URL 생성

print(url2) # https://product.kyobobook.co.kr/detail/S000200746091

#%%

from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 

driver = Chrome() # 옵션을 지정해 크롬 드라이버의 객체 생성

driver.get(url2)                    # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)          # 웹 사이트의 내용을 받아오기까지 기다림

html = driver.page_source 
soup = BeautifulSoup(html, "lxml")

print("- 접속한 웹 사이트의 제목:", driver.title) # 접속한 웹 사이트의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url) # 접속한 웹 사이트의 URL 출력

#%%
# 아래 코드는 너무 정보가 많다 더 안쪽에 위치한 요소찾기 필요
#soup.select(".container_wrapper .breadcrumb_item") 

s1 =  soup.find('a', attrs={'class': 'btn_sub_depth'}) # <a> 요소의 첫 번쨰값 '국내도서' 출력.
print(s1) # <a class="btn_sub_depth" href="https://product.kyobobook.co.kr/KOR">국내도서</a>
topic = soup.find_all('a', attrs={'class': 'btn_sub_depth'}) # <a> 요소인 속성값 모두 출력

# 속성값 html내용(BeautifulSoup의 'text'속성 사용하여 요소의 콘텐츠 추출)
genre = []
for t in topic:
    genre.append(t.text)
    print(t.text)

print(genre) # ['국내도서', '자기계발', '성공/처세', '자기관리/처세']
genre[1] # '자기계발'
#%%

# glist = 판매상품 아이디를 list자료형으로 변환
glist = df['판매상품ID'].tolist()
#%%
# 1위 부터 100위까지 상세페이지 링크 리스트자료형으로 변환.
def genre_link(glist):
    genre_data = []
    sampleurl = f"https://product.kyobobook.co.kr/detail/"
    for pid in glist:
        genre_data.append(sampleurl + str(pid))
    return genre_data

glist = df['판매상품ID'].tolist()
genre_data = genre_link(glist)
print(genre_data)



   
def genre_features(genre_data):
    genre_ft = []
    
    

    
        
    r = requests.get(url.format(goods_id))
    
    
  
 
  for genre_item in soup.find_all("ul", attrs={"class":"tabs swiper-wrapper ui-tabs-nav ui-corner-all ui-helper-reset ui-helper-clearfix ui-widget-header"}):
    genre = genre_item.find("span", attrs={"class":"tab_text"})
    main_links = genre_item.find('button', class_='tab_link')
    if genre is not None:
      genre_data.append({"Genre": genre.text})
    else:
      genre_data.append({"Genre": "NA"})

    if main_links is not None:
        # 'A' 메인 링크가 존재하는 경우
      genre_data.append({"Links": 'https://product.kyobobook.co.kr/bestseller/total?period=004#?page=1&per=50&period=004&ymw=&bsslBksClstCode' + main_links.get('href')})
    else:
        # 'A' 메인 링크가 없는 경우
      genre_data.append({"Links": "NA"})

  df = pd.DataFrame(genre_data)
  df['Genre'] = df['Genre'].str.replace('_nav_books_', '')
  df_links_sub = df.iloc[1:]
  df_links = df_links_sub.copy()
  df_links['Page2'] = df_links.Links.str.replace('_nav_books_1', '_pg_2?ie=UTF8&pg=2')

  return df_links



