# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:05:42 2024

@author: Shin
"""

# ## 파이썬으로 API 호출하기
# 도서관 정보나루
# https://www.data4library.kr/openDataV?libcode=4707
# 20대가 가장 좋아하는 도서 찾기
# In[23]:


import requests


# In[24]:
# http://data4library.kr/api/loanItemSrch : service url
# Option:
# format=json
# startDt=2021-04-01&endDt=2021-04-30
# age=20
# authKey=c01ec15e4574f74ee45cba2601bad15b82971e606e3b0740977ee4b363ce2fe2 : 인증키
# 이런식으로 만들어놓으면 나중에 수정하기 수월
svcurl = {
     "url": "http://data4library.kr/api/loanItemSrch",
     "options":
    {
     "format" : "json",
     "startDt" : "2021-04-01",
     "endDt" : "2021-04-30",
     "age" : 20,
     "authKey" : "c01ec15e4574f74ee45cba2601bad15b82971e606e3b0740977ee4b363ce2fe2"
    }
}
#%%
# 함수화
def get_service_url(svcurl): # 매개변수 svcurl 여기서 인수는 k로 예를들어 key값이 format 이면 v값은 해당
#key 값에 할당된 value값으로 json이 되고 kv는 dict 형태("format" : "json")를 문자열포멧팅을 활용하여 반환해준다.
# urls는 url이 반환될 떄 마다 객체의 요소를 하나의 문자열로 연결해주는 join()을 활용하여 &를 붙여 반환함.
# urls = svcurl['url'] -> http://data4library.kr/api/loanItemSrch" 에 반환된 url 즉, urls를 연결시켜주라는 의미


    url = []
    options = svcurl['options']
    for k in options.keys():
        v = options[k]
        kv = f"{k}={v}"
        url.append(kv)
        
    urls = '&'.join(url)
    urls = svcurl['url'] + urls 
    
    return urls

urlx = get_service_url(svcurl) 
print(urlx)
    
    
#%%

# 인증키를 발급받아 문자열 맨 끝에 추가해 주세요.
url = "http://data4library.kr/api/loanItemSrch?format=json&startDt=2021-04-01&endDt=2021-04-30&age=20&authKey=c01ec15e4574f74ee45cba2601bad15b82971e606e3b0740977ee4b363ce2fe2"


# In[25]:


r = requests.get(url)


# In[26]:


data = r.json()

print(data)


# In[27]:


data


# In[28]:


data['response']['docs']


# In[29]:


books = []
for d in data['response']['docs']:
    books.append(d['doc'])


# In[30]:

# 내포형식
books = [d['doc'] for d in data['response']['docs']]


# In[31]:


books


# In[32]:
import pandas as pd

books_df = pd.DataFrame(books)

books_df


# In[33]:


books_df.to_json('20s_best_book.json')
books_df.to_json('20s_best_book.json', force_ascii=False)
#%%
#orient='records': 행을 리스트 형태로 
books_df.to_json('20s_best_book.json',
                 orient='records',
                 indent=4,
                 force_ascii=False)