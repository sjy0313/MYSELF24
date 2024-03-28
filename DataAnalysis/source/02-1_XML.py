# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:25:43 2024

@author: Shin
"""
# ## 파이썬에서 XML 다루기

# In[12]:

# XML 형식의 문자열
x_str = """
<book>
    <name>혼자 공부하는 데이터 분석</name>
    <author>박해선</author>
    <year>2022</year>
</book>
"""
#XML을 파이썬 객체로 변환하는 과정에서 xml.etree.ElementTree 라이브러리를 사용하여 파싱하고,
# 이를 통해 파이썬 객체로 변환할 수 있습니다. 

# In[13]:


import xml.etree.ElementTree as et
# xml 파싱
book = et.fromstring(x_str)
#위 코드는 주어진 XML 문자열을 파싱하여 Element 객체를 생성하고, 
#이를 book 변수에 할당합니다. 이렇게 생성된 Element 객체는 XML 트리의 루트 요소를 나타내며,
# 다양한 방법으로 이를 조작하고 검색할 수 있습니다.

#et.fromstring(x_str)은 xml.etree.ElementTree 모듈의 fromstring() 함수를 사용하여
# XML 문자열 x_str을 파싱하여 XML 요소(Element) 객체를 생성합니다.
# In[14]:


print(type(book)) # <class 'xml.etree.ElementTree.Element'>


# In[15]:

# 루트
print(book.tag) # book 


# In[16]:
# booktag의 자식 element(요소)를 리스트 객체로 변환
# 자식 객체들인 element들을 얻게됨.
book_childs = list(book)

print(book_childs)


# In[17]:
# 파이썬에서 XML데이터 처리
    
# etree.ElementTree.Element
name, author, year = book_childs

print(name.text) # 혼자 공부하는 데이터 분석
print(author.text)# 박해선
print(year.text)# 2022


# In[18]:


name = book.findtext('name')
author = book.findtext('author')
year = book.findtext('year')

print(name) # value 값으로 혼자 공부하는 데이터 분석 
print(author) # value 값으로 박해선
print(year) # value 값으로 2022


# In[19]:


x2_str = """
<books>
    <book>
        <name>혼자 공부하는 데이터 분석</name>
        <author>박해선</author>
        <year>2022</year>
    </book>
    <book>
        <name>혼자 공부하는 머신러닝+딥러닝</name>
        <author>박해선</author>
        <year>2020</year>
    </book>
</books>
"""


# In[20]:


books = et.fromstring(x2_str)

print(books.tag)


# In[21]:

# book에 element객체를 주는 것.
for book in books.findall('book'):
    print(type(book)) # <class 'xml.etree.ElementTree.Element'>
    name = book.findtext('name')
    author = book.findtext('author')
    year = book.findtext('year')
    
    print(name)
    print(author)
    print(year)
    print()
'''
혼자 공부하는 데이터 분석
박해선
2022

혼자 공부하는 머신러닝+딥러닝
박해선
2020
'''

# In[22]:


# 판다스에서 XML 형식 처리    
import pandas as pd
from io import StringIO
xml_data = StringIO(x2_str) # StringIO 객체 생성
pd_xml = pd.read_xml(x2_str) # read_xml() 함수에 StringIO 객체 전달 (read_xml()에서 내부적으로 처리)
print(pd_xml)
'''
               name               author  year
0    혼자 공부하는 데이터 분석    박해선  2022
1  혼자 공부하는 머신러닝+딥러닝  박해선  2020
'''
#이 경고는 Pandas의 read_xml() 함수를 사용할 때 발생하는 것으로,
# 향후 버전에서 문자열로 직접 XML을 전달하는 것이 제거될 예정이라는 경고입니다.
#이 경고를 해결하기 위해서는 read_xml() 함수에 문자열 대신 StringIO 객체를 전달하면 됩니다. 
#StringIO는 문자열을 파일과 같이 취급하여 Pandas의 데이터 읽기 함수에 전달할 수 있도록 해줍니다.

'''
C:\Users\Shin\AppData\Local\Temp\ipykernel_1436\4094031176.py:2: 
FutureWarning: Passing literal xml to 'read_xml' is deprecated and will 
be removed in a future version. To read from a literal string, wrap it in a 'StringIO' object.
pd_xml = pd.read_xml(x2_str)
'''

