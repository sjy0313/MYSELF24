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
if score >= 0 and score <= 100: # 0부터 100까지
    message = "failure"
    if score>=60:
        message = "success"
else: 
    message = '오류'

print(f"점수는 ({score})이며 ({message})입니다.")
# 점수는 (-1)이며 (오류)입니다.
