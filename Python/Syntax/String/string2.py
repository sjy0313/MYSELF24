# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:41:30 2024

@author: Shin
"""

# 문자열(string) : str
# 멀티(다중)라인
# Enter: \n newline(Windows: CRLF/ Mac : CR / Linux : LF) enter키에 할당된 코드 
# \n 자체가 \n기능을 포함하기 때문에 \n\r 잘안씀 
# CR(\r) : carriage return 커서를 맨 앞으로 이동
# LF(\f) : form feed 다음 페이지 
#%%
cr= ord('\r') # carriage return
lf= ord('\n') # line feed 
ff= ord('\f') # form feed 
ht= ord('\t') # horizontal tab
bs= ord('\b') # Backspace

print(cr, hex(cr)) #13(0x0d)
print(lf, hex(lf)) #10(0x0a)
print(ff, hex(ff)) #12(0x0c)
print(ht, hex(ht)) #(0x09)
print(bs, hex(bs)) #(0x08)
#%%
ss1 = "안녕하세요?\r반갑습니다.\r뭐해요?\r"
print(ss1) #뭐해요?다.
#%%
ss2 = "안녕하세요?\f반갑습니다.\f뭐해요?\f"
print(ss2) 
#%%
# Windows: CRLF
ss3 = "어서오세요.\r\n안녕히가세요.\r\n"
print(ss3)
#%%
# Horizontal Tab (수평탭)
# 8칸 
print("1234567890" * 5)
print("ABC\tDEFGHIJK\tLMNOPQ\tEND")
#%%
#BS(Backspace)
print("ABC\bD") # ABD
print("ABC\b\b\bD") #DBC 자리이동 
#%%
# 멀티(다중)라인 주석 
print("# 멀티라인 주석: 시작")
"""다중라인 주석 시작입니다. 

"""
print("# 멀티라인 주석: 종료")
#  # "앞에 공백있으면 들여쓰기(indentation)오류뜸.
#%%
smx = """안녕하세요
 반갑습니다
 환영
"""
print(smx)
#%%
# \(백슬래시)를 이용하여 문자열을 연결 
smy =" 안녕하세요\
 반갑습니다\
 환영"
print(smy) #  안녕하세요 반갑습니다 환영
#%%
# +=: 더해서 할당
sme = "안녕"
sme += "누구니?"
sme += "난 ?야"
print(sme)  # 안녕누구니?난 ?야


