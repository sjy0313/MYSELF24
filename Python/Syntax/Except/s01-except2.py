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
# 파일을 읽기용으로 오픈 

# file = open("없는파일.txt", 'r')
#FileNotFoundError: [Errno 2] No such file or directory: '없는파일.txt'

#%%

try:
    file = open("./없는파일", 'r')
except FileNotFoundError as e:
    print("[예외발생]", e)
    print("작업완료")
    
                