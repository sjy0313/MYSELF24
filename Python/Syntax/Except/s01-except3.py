# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:56:59 2024

@author: Shin
"""
# 예외처리(Exception)
# try ~ except
# 
#예외:
#   -잘못된 동작을 했을 떄
#   -실행할 떄 발생
#   -프로그램 종료
#
#예외처리:
#   -비정상적 상황으로 인해서 프로그램이 중단없이 실행 가능하도록 처리


#%%
x = 10
y = 0
z = 0 
"""
try:
    z = x / y
    file = open("./없는파일txt", 'r')
    print("정상처리")
except ZeroDivisionError as e:
    print("[예외발생]나누기 오류", e)
except FileNotFoundError as e:
    print("[예외발생]파일처리 오류", e)
 """

#%%
"""
try:
      z = x / y
      file = open("./없는파일txt", 'r')
      print("정상처리")
except (ZeroDivisionError, FileNotFoundError) as e:
       print("[예외발생]나누기 오류", e)
"""     
#%%
try:
      z = x / y
      file = open("./없는파일txt", 'r')
      print("정상처리")
except: # 모든 예외처리
       print("[예외발생]")
       
       

                