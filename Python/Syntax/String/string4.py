# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:31:19 2024

@author: Shin
"""

# 문자열 슬라이싱(slicing)
# 특정한 범위를 지정하여 추출(원본변화X)
# 추출된 문자열은 새로운 변수에 할당
# 변수 = 문자열[시작번호: 종료번호:스탭]
# 시작번호 0부터 시작
# 종료번호 : 종료번호 -1 까지 참조
# 스탭간격 : 건너뛰기 -> :: 


# 문자열 포맷팅 (p71)

#%%
# 문제
# 아래 숫자 문자열에서 각각 홀수와 짝의 문자를 추출하라
# 단 슬라이싱을 이용하라.

nums = "0123456789"
even = nums[::2]
print(even) # 02468
odd = nums[1::2]
print(odd) # 13579
# 모범
# 홀수 
print(f"문자열({nums})에서 짝수는 ({nums[::2]})")

start = 0
end = len(nums)
step = 2 # 건너뛰기
even = nums[start:end:step]
print(f"문자열({nums})에서 짝수는 ({even})")
#%%
#문자열 포멧팅을 쓰지 않으면
print("문자열(", nums,")에서 홀수는 (",nums[1::2],")",sep = ' ')



#%%
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

s[2] # 'C'
s[0:4] # 'ABCD'
sl = len(s)
s2= s[:]
s0= s[0:26]
s1= s[0:sl]
print(s) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(s0)
print(s1)
print(s2)
#%%
# 종료번호에 -1을 주면 마지막 요소 이전까지 지정
s3 = s[0:-1]
print(s3) # ABCDEFGHIJKLMNOPQRSTUVWXY

#%%
s4 = s[1:5] # 1~4
print(s4) # BCDE
#%%
 # 참조 슬라이싱을 사용하지 않음
print(s[ -1 ]) # Z
# 슬라이싱을 사용하여 맨 마지막 요소를 추출
print(s[sl-1:sl]) # Z
print(s[-1:] ) # Z
