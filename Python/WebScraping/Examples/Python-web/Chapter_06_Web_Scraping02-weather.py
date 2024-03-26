# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:11:54 2024

@author: Shin
"""

# ## 6.2 웹 사이트에서 데이터 가져오기

# ### 6.2.1 날씨 정보 가져오기

# #### 웹 사이트 분석해 날씨 정보 가져오기

# [6장: 241페이지]
# pip install schedule
# In[ ]:


import requests  
from bs4 import BeautifulSoup 

location = "서울시 종로구 청운동"
search_query = location + " 날씨"
search_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="
url = search_url + search_query
# 결과값 웹창에 입력 (url)
# request.get()통한 데이터 수집
html_weather = requests.get(url).text
soup_weather = BeautifulSoup(html_weather, "lxml")
print(url)


# In[ ]:


txt_temp = soup_weather.select_one('strong.txt_temp').get_text()
txt_temp #  '14℃'


# In[ ]:


txt_weather = soup_weather.select_one('span.txt_weather').get_text()
txt_weather # '11시 현재, 구름조금'


# In[ ]:


dl_weather_dds = soup_weather.select('dl.dl_weather dd')
dl_weather_dds #  [<dd>2.5m/s</dd>, <dd>33%</dd>, <dd class="dust_type2">보통 (45㎍/㎥)</dd>]


# [6장: 244페이지]

# In[ ]:


[wind_speed, humidity, pm10] = [x.get_text() for x in dl_weather_dds]

print(f"현재 풍속: {wind_speed}, 현재 습도: {humidity}, 미세 먼지: {pm10}")
# 현재 풍속: 2.5m/s, 현재 습도: 33%, 미세 먼지: 보통 (45㎍/㎥)

# In[ ]:

location = "서울시 종로구 청운동"
search_query = location + " 날씨"
search_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="
url = search_url + search_query


import requests  
from bs4 import BeautifulSoup 
import time

def get_weather_daum(location):
    search_query = location + " 날씨"
    search_url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="
    url = search_url + search_query
    html_weather = requests.get(url).text
    time.sleep(2)    
    soup_weather = BeautifulSoup(html_weather, "lxml")
    
    txt_temp = soup_weather.select_one('strong.txt_temp').get_text()
    txt_weather = soup_weather.select_one('span.txt_weather').get_text()

    dl_weather_dds = soup_weather.select('dl.dl_weather dd')
    [wind_speed, humidity, pm10] = [x.get_text() for x in dl_weather_dds]
    
    return (txt_temp, txt_weather, wind_speed, humidity, pm10)


# In[ ]:


location = "서울시 종로구 청운동" # 날씨를 알고 싶은 지역 
get_weather_daum(location)        # 함수 호출


# [6장: 245페이지]

# In[ ]:


location = "경기도 수원시" # 날씨를 알고 싶은 지역 

(txt_temp, txt_weather, wind_speed, humidity, pm10) = get_weather_daum(location)

print("-------[오늘의 날씨 정보] (Daum) ----------")
print(f"- 설정 지역: {location}")
print(f"- 기온: {txt_temp}")
print(f"- 날씨 정보: {txt_weather} ", )
print(f"- 현재 풍속: {wind_speed}, 현재 습도: {humidity}, 미세 먼지: {pm10}")


# #### 날씨 정보 주기적으로 가져오기

# [6장: 245페이지]

# In[ ]:
# 5초에 한번 씩 데이터 수집하여 업데이트

# pip install schedule
# 패키지 3가지 이용
import schedule
import time
from datetime import datetime

# 작업을 위한 함수 지정
def job():
    now = datetime.now() # 현재시간함수
    print("[작업 수행 시각] {:%H:%M:%S}".format(now))
    location = "경기도 수원시" # 날씨를 알고 싶은 지역 

    (txt_temp, txt_weather, wind_speed, humidity, pm10) = get_weather_daum(location)

    print("-------[오늘의 날씨 정보] (Daum) ----------")
    print(f"- 설정 지역: {location}")
    print(f"- 기온: {txt_temp}")
    print(f"- 날씨 정보: {txt_weather} ", )
    print(f"- 현재 풍속: {wind_speed}, 현재 습도: {humidity}, 미세 먼지: {pm10}")

# 코드 테스트를 위해 5초마다 날씨 정보 가져와 출력하기 위한 스케줄 설정
schedule.every(5).seconds.do(job)  # 5초(second)마다 job() 함수 실행

# -- 매일 지정한 시각에 날씨 정보를 가져와 출력하기 위한 스케줄 설정
# schedule.every().day.at("07:00").do(job) # 매일 07시에 job() 함수 실행
# schedule.every().day.at("12:00").do(job) # 매일 12시에 job() 함수 실행
# schedule.every().day.at("18:00").do(job) # 매일 18시에 job() 함수 실행

while True:
    try:
        schedule.run_pending()
        time.sleep(1) # 객체가 만들어지는 동안 일정 시간 동안 반복 횟수를 줄여준다.
    except:
        print("작업 강제 종료")
        schedule.clear()  # 기본 스케줄러 객체를 제거          
        break            # while 문을 빠져 나옴
'''
[작업 수행 시각] 14:06:08
-------[오늘의 날씨 정보] (Daum) ----------
- 설정 지역: 경기도 수원시
- 기온: 15℃
- 날씨 정보: 13시 현재, 구름많음 
- 현재 풍속: 6.0m/s, 현재 습도: 43%, 미세 먼지: 보통 (46㎍/㎥)
작업 강제 종료
'''