# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:28:28 2024

@author: Shin
"""

# 문자열 포멧팅(string formatting)
# 문자열 포멧 코드 
""" 
%s : 문자열 string
%c : 문자 character 
%d : 정수 10진수, decimal
%f : (부동소수)실수(float)
%o : 8진수 octal
%x : 16진수 hexa-decimal
%% : Literal% (문자 % 자체)
""" 
# 형식 :
# 포멧문자열 % 변수
# 포멧문자열 % (변수, ...)

#%%
# 정렬 
n= 12345
s= "Hello"
f= 0.12345

print("#정수")
print(f"정수: ({n:>10})") # 정수: (     12345) 
print(f"정수: ({n:<10})") # 정수: (12345     )
print(f"정수: ({n:^10})") # 정수: (  12345   )
print(f"정수: ({n:>10d})")# 정수: (     12345)
print(f"정수: ({n:>10x})") # 16진수 
print(f"정수: ({n:>10o})") # 8진수

#%%
print("실수")
print(f"실수: ({f:>10})")   # 실수: (   0.12345)
print(f"실수: ({f:<10})")  # 실수: (0.12345   )
print(f"실수: ({f:10.3})") # 전체 10자리(소숫점 포함), 소숫점 이하 3자리 
print(f"실수: ({f:>10.3f})")  # 실수: (     0.123)
print(f"실수: ({f:^10.3})")  # 실수: (  0.123   )
#%%
print("#문자열")
print(f"문자 : ({s:<10})") # 문자 : (Hello     )
print(f"문자 : ({s:^10})") # 문자 : (  Hello   ) 
print(f"문자 : ({s:^10s})") #문자 : (  Hello   )
#%%

# 문자열.format() 함수
# format() 인자의 대입 순서 지정
print("정수 : ({0:^10})".format(n)) # 가운데 정렬
print("실수 : ({0:^10})".format(f)) # 가운데 정렬
print("문자 : ({0:^10})".format(s)) # 가운데 정렬
print("전체 : ({0:^10})({1:^10})({2:^10})".format(n, f, s)) # 가운데 정렬
#%%

# 인자의 순번을 생략
print("전체 : ({:^10})({:^10})({:^10})".format(n, f, s)) # 가운데 정렬
print("전체 : ({})({})({})".format(n, f, s)) 
print(f"전체 : ({n})({f})({s})") # (12345)(0.12345)(Hello) 

#%%

# 가변처리(동적처리)
# 고객정보 처리
name = "홍길동"
age = 34

msg = "고객님의 이름은 {0}이며 나이는 {1}입니다.".format(name, age)
print(msg)

fmt = "고객님의 이름은 {0}이며 나이는 {1}입니다."
print(fmt.format(name, age)) # 고객님의 이름은 홍길동이며 나이는 34입니다.

