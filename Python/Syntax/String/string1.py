# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:26:42 2024

@author: Shin
"""
# 문자열(string) : str
#%%
s1 = "문자열" # 큰따옴표/ 작은따옴표
print(type(s1))  # <class 'str'>
#%%
# 멀티(다중)라인
# Enter: \n newline(Window : CRLF/ Mac : CR / Linux : LF) enter키에 할당된 코드 
# CR(\r) : carriage return 커서를 맨 앞으로 이동
# LF(\f) : form feed 줄바꿈, 다음 줄로 이동

sml = """안녕하세요?
반갑습니다.
뭐하세요?
"""
print(sml) 
# 안녕하세요?
#반갑습니다.
#뭐하세요?
#%%
ssml = "안녕하세요?\n반갑습니다.\n뭐해요?\n"
print(ssml)
# 안녕하세요?
#반갑습니다.
#뭐해요?

