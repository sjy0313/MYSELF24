# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:51:41 2024

@author: Shin
"""

# if문
# 조건부 표현식(conditional expression)
# 결과(bool) = 참인경우 if 조건식 else 거짓인경우
# 조건식에 참이면 : 참인경우의 값이 결과에 할당
# 조건식이 거짓이면 : 거짓인 경우의 값이 결과에 할당


score = -1 # 0부터 100까지

if score >= 60:  
    message = "success"
elif score >= 0:
    message = "failure"

print(f"점수는 ({score})이며 ({message})입니다.")
# NameError: name 'message' is not defined 
# 해결 if2-error 
#%%
#위의 코드를 조건부 표현식(conditional expression)으로 바꾸면
msg = "합격" if score >= 60 else "불합격"
print(f"점수는 ({score})이며 ({msg})입니다.")
#%%
#조건부 표현식을 여러 개 사용
grade = 70
grade = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else "D"

print(f"점수는 ({score})이며 등급은 ({grade})입니다")
#%%
# 조건부 표현식을 여러개 사용하고 여러 줄에 기술 : 
# 역슬래시(\)를 이용하영 명령문을 연결
# 열슬래시 뒤에는 어떤 문자도 기술되어선 안됨.
# 주의: 공백(스페이스)
grade = 'A' if score >= 90 else\
        'B' if score >= 80 else\
        'C' if score >= 70 else 'D'
print(f"점수는 ({score})이며 등급은 ({grade})입니다")