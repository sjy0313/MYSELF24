# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:12:58 2024

@author: Shin
"""

# zip()
# zip(*iterable) : 동일한 개수로 이루어진 데이터를 묶어서 리턴하는 함수
#%%

a = [1,2,3]
b = [1,3,5]
c = [2,4,6]
abzip = zip(a,b,c)
ablst= list(abzip)
print(abzip)
print(ablst) # [(1, 1, 2), (2, 3, 4), (3, 5, 6)]

#%%
# 갯수가 다르면?
d = [10,11,12,13]
adlst = list(zip(a,d))
print(adlst) # [(1, 10), (2, 11), (3, 12)] 13은 누락됨.
#%%
kw = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
ew = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weeks = list(zip(kw,ew))
print(weeks)
#[('월요일', 'Monday'), ('화요일', 'Tuesday'), ('수요일', 'Wednesday'),
# ('목요일', 'Thursday'), ('금요일', 'Friday'), ('토요일', 'Saturday'), ('일요일', 'Sunday')]
week = tuple(zip(kw,ew))
print(week)
(('월요일', 'Monday'), ('화요일', 'Tuesday'), ('수요일', 'Wednesday'), 
 ('목요일', 'Thursday'), ('금요일', 'Friday'), ('토요일', 'Saturday'), ('일요일', 'Sunday'))
days = dict(zip(kw,ew))
print(days)

days['청요일'] = 'skyday'
days
"""
{'월요일': 'Monday',
 '화요일': 'Tuesday',
 '수요일': 'Wednesday',
 '목요일': 'Thursday',
 '금요일': 'Friday',
 '토요일': 'Saturday',
 '일요일': 'Sunday',
 '청요일': 'skyday'}
"""

del days['청요일']
days






