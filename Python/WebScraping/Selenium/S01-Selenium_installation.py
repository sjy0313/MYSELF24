# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 09:15:45 2024

@author: Shin
"""
# selenium 과 beautifulsoup 을 활용한 데이터 스크레이핑.
# selenium은 웹 브라우저를 제어하기 위한 다양한 기능을 갖고 있다.
#   -static website -> request library -> HTML 소스 가져와 처리
#   -Dynamic website -> javascript code -> selenium으로 데이터 처리
'''
# selenium 설치
conda activate YSIT24
pip install selenium
pip install webdriver_manager
'''
'''
pip show selenium
import selenium
help(selenium)
 4.18.1
webdriver_manager 
Version: 4.0.1
 '''
#  webdriver_manager최신 버전 업그레이드 
'''
conda activate your_environment_name
pip install --upgrade webdriver-manager
'''
# selenium  4.18.1 에서는 ChromeDriver 를 설치 안해도 됨.
# 최신 크롬 브라우저를 지원.
#%%

'''
import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeDriver
from selenium_webdriver import ChromeDriverManager
from seleniuum.webdriver.common.by import By
'''
# 다운 
'''
conda activate YSIT24
pip install selenium
pip install webdriver_manager

# driver = webdriver.Chrome() # 크롬드라이버 객체 생성
# NuGet\Install-Package Selenium.WebDriver -Version 4.18.1

# driver.get("http://www.naver.com") # 웹 브라우저
'''
 # google.com 에서 python 검색결과:  

from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By

driver = Chrome() # 크롬드라이버 객체 생성
driver.set_window_size(800,600) # 웹 브라우저 창 크기를 최대로 설정 (width,height)
url = "http://www.google.com"
driver.get(url)
# 사이즈 설정 방법2
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('window-size=width,height')
driver=Chrome(options=options)
driver.get(url)

# driver.quit() # driver 객체로 연 웹브라우저 닫기

query = "python"
input_element = driver.find_element(By.NAME, "q") # By.속성의 입력값으로 입력창 찾기
# 속성과 입력값은 웹사이트마다 다름. 웹사이트 입력창은 (f12로 확인) input
# 태그를 갖고 있는데 input요소에 name속성에는 q가 지정된 것을 확인 가능. 
# 구글과 다음의 입력값은 q
# 네이버의 입력값은 query로 설정 되어있음.

input_element.send_keys(query) # ('문자열')
input_element.submit() # 문자열을 보낸결과 요청

print("접속할 웹 사이트 제목", driver.title)
print("웹사이트 url", driver.current_url)

#%%
from selenium.webdriver import Chrome 
driver = Chrome()
driver.set_window_size(800,600)

url = "http://www.naver.com"
driver.get(url)

query = "python"
input_element = driver.find_element(By.NAME, "query") 
input_element.send_keys(query)
input_element.submit()
#%%
#웹 사이트 문서 높이 가져오기 (웹 브라우저 스크롤)

import time 

scroll_height = driver.execute_script("return document.body.scrollHeight")
print("-웹 사이트 문서 높이:", scroll_height)

y = 0
y_step = 200

while(True):
    y = y + y_step
    script = "window.scrollTo(0,{0})".format(y)
    driver.execute_script(script)
    time.sleep(1) # 데이터를 받아올 떄까지 기다림
    
    if(y >=scroll_height):
        break
    

#%%
from selenium.webdriver import Chrome 
from selenium.webdriver.common.by import By
import time 

driver = Chrome() # 크롬드라이버 객체 생성
driver.set_window_size(800,700) # 웹 브라우저 창 크기를 최대로 설정 (width,height)
url = "http://www.google.com"
driver.get(url)

input_element = driver.find_element(By.NAME, "q") # 검색창 찾기
input_element.clear() # 검색창 내용 모두 지우기
query = "환율"
input_element.send_keys(query) # 검색창에 검색어 입력
input_element.submit() # 검색결과 요청

folder = "D:\WORKSPACE(SHIN)\Python\WebScraping\Selenium"
image_file = folder + "환율정보.png"
driver.save_screenshot(image_file) #웹 브라우저 내용을 캡처해 이미지 파일로 저장

time.sleep(1)
driver.quit()

print("-생성할 이미지 파일:", image_file) # 접속한 URL 제목 출력

#%%
# headless web browser 

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

options = Options()                  # 옵션 설정을 위한 객체 생성
options.add_argument('headless')     # 헤드리스 웹 브라우저로 옵션 설정
options.add_argument('window-size=1100,1000') # 웹 브라우저의 창 크기 설정

driver = Chrome(options=options)     # 옵션을 지정해 크롬 드라이버의 객체 생성

url = "https://finance.naver.com/"   # URL 지정
driver.get(url)                      # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)            # 웹 사이트의 내용을 받아오기까지 기다림

folder = "D:\WORKSPACE(SHIN)\Python\WebScraping\Selenium"   # 폴더 지정
image_file = folder + "네이버_금융.png" # 생성할 이미지 파일 이름 지정
driver.save_screenshot(image_file)      # 웹 브라우저 내용을 캡처해 이미지 파일로 저장

driver.quit() # 웹 브라우저 종료

print("- 생성한 이미지 파일:", image_file) # 접속한 URL의 제목 출력

from IPython.display import Image

Image(filename=image_file)              # 이미지 파일 이름을 지정
# Image(filename=image_file, width=800) # 이미지 파일 이름과 너비를 지정


# In[ ]:

import requests  
from bs4 import BeautifulSoup 

url = "https://www.starbucks.co.kr/menu/drink_list.do"

html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")

# 요소 검사를 수행한 결과의 상위 태그와 속성을 이용
products = soup.select('li.menuDataSet dl dd') 
products


# [7장: 307페이지]

# In[ ]:


products = soup.select('div.product_list dl dd')
products[0:3]


# [7장: 308페이지]

# In[ ]:


from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 

driver = Chrome() # 옵션을 지정해 크롬 드라이버의 객체 생성

url = "https://www.starbucks.co.kr/menu/drink_list.do" # URL 지정
driver.get(url)                    # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)          # 웹 사이트의 내용을 받아오기까지 기다림

html = driver.page_source          # 접속 후에 해당 page의 HTML 코드를 가져옴
soup = BeautifulSoup(html, 'lxml') # HTML 코드를 파싱함

print("- 접속한 웹 사이트의 제목:", driver.title) # 접속한 웹 사이트의 제목 출력
print("- 접속한 웹 사이트의 URL:", driver.current_url) # 접속한 웹 사이트의 URL 출력


# In[ ]:


drink_products = soup.select('div.product_list dl dd ul li.menuDataSet dl')
drink_products[0] # 첫 번째 음료 메뉴의 요소 출력


# [7장: 309페이지]

# In[ ]:


print(drink_products[0].prettify())


# In[ ]:


drink_menu_name = drink_products[0].select_one('dd').get_text()
drink_menu_name


# [7장: 310페이지]

# In[ ]:


drink_menu_photo_link = drink_products[0].select_one('a img')['src']
drink_menu_photo_link


# In[ ]:


from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup 
import pandas as pd

options = Options()
options.headless = True # 헤드리스 모드로 지정해 크롬을 GUI 없이 수행

driver = Chrome(options=options) # 옵션을 지정해 크롬 드라이버의 객체 생성

url = "https://www.starbucks.co.kr/menu/drink_list.do"  # URL 지정
driver.get(url)              # 웹 브라우저를 실행해 지정한 URL에 접속
driver.implicitly_wait(3)    # 웹 사이트의 내용을 받아오기까지 기다림

html = driver.page_source    # 접속 후에 해당 page의 HTML 코드를 가져옴
soup = BeautifulSoup(html, 'lxml') # HTML 코드 파싱

drink_products = soup.select('div.product_list dl dd ul li.menuDataSet dl')
driver.quit() # 웹 브라우저를 종료함

drink_menu_name_photo_links = [] 
for drink_product in drink_products:
    menu_name = drink_product.select_one('dd').get_text()
    menu_photo_link = drink_product.select_one('a img')['src']
    drink_menu_name_photo_links.append((menu_name, menu_photo_link))

drink_menu_name_photo_links[0:4]


# [7장: 311페이지]

# In[ ]:


len(drink_menu_name_photo_links) # 스타벅스 음료 메뉴의 개수


# In[ ]:


col_drink_menu = ["메뉴", "사진"]
df = pd.DataFrame(drink_menu_name_photo_links, columns=col_drink_menu)
df.head(4)


# In[ ]:


# 이미지의 링크를 HTML img 태그로 만드는 함수 
def make_HTML_image_tag(link):
    image_width = 80   # 이미지 크기(너비)를 지정
    image_tag = f'<img src="{link}" width="{image_width}">' # img 태그
    return image_tag  # img 태그를 반환


# df 가 가지고 있는 사진 columns 의 리턴값을 아래 df.to_html로 전달
make_HTML_image_tag(df["사진"][0])


# In[ ]:


html_table = df.head(4).to_html(formatters=dict(사진=make_HTML_image_tag), escape=False)
print(html_table)


# [7장: 314페이지]

# In[ ]:


from IPython.display import HTML

HTML(html_table) # HTML 코드의 내용을 웹 브라우저처럼 보여줌


# [7장: 315페이지]

# In[ ]:


# folder = "./"        # 폴더 지정 # 파일이름으로 내용저장 원할 시 
folder ="D:\WORKSPACE(SHIN)\Python\WebScraping\Selenium"
file_name = folder + "starbucks_drink_menu.html" # 생성할 HTML 파일 이름 지정 

df.to_html(file_name, formatters=dict(사진=make_HTML_image_tag), escape=False)

print("생성한 파일:", file_name)









   

#%%
# 카카오톡 웹사이트 로그인 자동화 p291
#%%
# 확장 프로그램 설치
# 설정 -> 확장프로그램 -> 웹스토어 selenium IDE chrome에 추가 (동적인 서칭자동화)
# create a new project -> 웹 주소 입력-> start recording -> ex) naver에서 -> 비트코인 -> 뉴스
# stop recording -> 해당 test 우클릭 -> export -> language(python pytest) 선택 후 export 


# google 실행
'''
from selenium.webdriver import Chrome
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://google.com")
'''




