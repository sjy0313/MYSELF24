# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:08:38 2024

@author: Shin
"""

# ## 8.2 API 키 없이 시간 관련 데이터 가져오기 

# ### 8.2.1 시간대 리스트와 현재 시각 데이터 가져오기

# [8장: 345페이지]

# In[ ]:


import requests  
import json

url = "https://timeapi.io/api/TimeZone/AvailableTimeZones" #문자열 형태

r = requests.get(url) # requests 를 이용해 응답결과를 받을 수 있다.
# 응답 객체 r에 대해 r.text는 문자열로 변환.
r.text[:70] # 문자열 중 앞의 일부만 출력
# r.text    # 문자열 전체를 출력


# [8장: 346페이지]

# In[ ]:


import requests  
import json

url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Seoul" #dict와 같이{}가 데이터를 감싸고 있다.
# ? 이후 값은 parameter 
r = requests.get(url)
print(r.text) 
'''
{"year":2024,"month":3,"day":26,"hour":10,"minute":13,"seconds":3,"milliSeconds":65,
 "dateTime":"2024-03-26T10:13:03.0658586","date":"03/26/2024","time":"10:13",
 "timeZone":"Asia/Seoul","dayOfWeek":"Tuesday","dstActive":false}
'''
# dst 서머타임.
# In[ ]:


url = "https://timeapi.io/api/Time/current/zone" # 요청 주소
parameters = {"timeZone": "Asia/Seoul"}          # 요청 매개 변수 생성

r = requests.get(url, params=parameters) # url + parameter로 분리하여 데이터 요청도 가능. 
print(r.text) 


# In[ ]:


json_to_dict = json.loads(r.text) # json.loads()를 이용해 json형태의 dict type으로 변환
type(json_to_dict) #  dict


# [8장: 347페이지]

# In[ ]:


json_to_dict = r.json() #r.json은 r.text + json.loads 한번에 처리
#JSON 형태의 데이터를 파이썬의 딕셔너리 타입으로 변환 
type(json_to_dict)  #  dict


# In[ ]:

# https://mommoo.tistory.com/60 # get 방식과 post방식의 차이 
# 클라이언트의 데이터를 URL뒤에 붙여서 보낸다
#간단한 데이터를 넣도록 설계되어, 데이터를 보내는 양의 한계가 있다.
#? 이후에 parameter 값 timeZone=Asia/Seoul 
import requests
import json
# Binary Data를 Character set에 영향을 받지 않는 공통 ASCII 영역의 문자로만 이루어진 문자열로 바꾸는 Encoding
# get 방식 
url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Seoul"

date_time_dict = requests.get(url).json()
type(date_time_dict) # dict


# In[ ]:


date_time_dict


# [8장: 348페이지]

# In[ ]:


date_time_dict["dateTime"], date_time_dict["timeZone"], date_time_dict["dayOfWeek"]
# ('2024-03-26T10:22:04.844305', 'Asia/Seoul', 'Tuesday')

# ### 8.2.2 시간대 변환 데이터 가져오기

# [8장: 349페이지]

# In[ ]:


import requests
import json

url = 'https://timeapi.io/api/Conversion/ConvertTimeZone' # 요청 주소

from_time_zone = "Asia/Seoul"
from_date_time = "2024-03-26 10:40:00"
#to_time_zone = "UTC" # GMT로 지정해도 결과는 동일
to_time_zone = "GMT" # GMT로 지정해도 결과는 동일

headers = {"Content-Type": "application/json"}
# dict -> json
# POST방식은 URL에 붙여서 보내지 않고BODY에다가 데이터를 넣어서 보낸다.  
#BODY에다가 데이터를 넣어서 보낸다.  따라서, 헤더필드중 BODY의 데이터에 요청변수 추가 
#Python 객체를 JSON 데이터로 쓰기, 직렬화, 인코딩 :  json.dumps()

json_data = json.dumps({"fromTimeZone": from_time_zone, # 원래 시간대
                        "dateTime": from_date_time, # 원래 시간대의 날짜와 시각
                        "toTimeZone": to_time_zone, # 변환 시간대
                        "dstAmbiguity": " "})

print(json_data)
'''
{"fromTimeZone": "Asia/Seoul", "dateTime": "2024-03-26 10:50:00", "toTimeZone": "GMT", "dstActive": false}
'''
r = requests.post(url, headers=headers, data=json_data) # POST 방법으로 요청해 응답받음
# requests.post(url, json=dict_data)를 활용하게 되면
# headers = {"Content-Type": "application/json"} 이 자동설정됨.
ctz_json_to_dict = r.json()
ctz_json_to_dict

# Response
# 400 Bad Request

# [8장: 350페이지]

# In[ ]:


import requests
import json

url = 'https://timeapi.io/api/Conversion/ConvertTimeZone' # 요청 주소

from_time_zone = "Asia/Seoul"
from_date_time = "2022-10-03 10:03:00"
to_time_zone = "GMT" # UTC로 지정해도 결과는 동일

dict_data = {"fromTimeZone": from_time_zone,
              "dateTime": from_date_time,
              "toTimeZone": to_time_zone,
              "dstAmbiguity":" "
              }

r = requests.post(url, json=dict_data) # POST 방법으로 JSON 데이터를 서버에 전송
ctz_json_to_dict = r.json() # 메서드를 통해 파이썬 딕셔너리로 변환
ctz_json_to_dict


# [8장: 351페이지]

# In[ ]:
# 위의 딕셔너리 결과를 키를 지정해 단계별로 딕셔너리에 접근하면 원하는 데이터를 
# 추출가능. conversionResult 키로 값에 접근한 후 다시 dateTime키를 지정해 원하는
# 데이터 추출.

dateTime = ctz_json_to_dict['conversionResult']['dateTime'] # 변환된 날짜와 시각 데이터를 추출
to_date_time = f"{dateTime.split('T')[0]} {dateTime.split('T')[1]}"
from_date_time, to_date_time

