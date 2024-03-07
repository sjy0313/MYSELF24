# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:33:49 2024

@author: Shin
"""
#독립적으로 쓸 수 있는 것을 함수, 리스트뒤에 .을 붙여서
#종속적으로 사용가능한 것을 메서드라고 합니다.
#메서드는 자료구조 자체가 가지고 있는 기능입니다.

# 리스트 추가 : append()
# 기존에 있는 리스트에 요소를 추가하여 확장(extend)
# 기존에 있는 리스트에 하나의 요소를 추가(append)
# 리스트 객체 자체를 변경
# 리턴값? # None

lst = ['삼성', 'SK', 'LG']
# 리스트 변수(lst)가 가리키고 있는 주소를 복사
# 데이터를 복사한 것이 아님
bst =lst  # 다른 메모리에 기억시킴(변수 = 메모리 주소) 

print(id(bst)) # 1701814304960
print(id(lst)) # 1701814304960
lst = lst.append(['APPLE', 'HD'])
    
# lst : None
            
print(lst)
print(bst)
