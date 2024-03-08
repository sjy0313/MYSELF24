# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:19:30 2024

@author: Shin
"""

# 반복문 : while
# 조건이 만족하는 동안 반복해서 블럭의 문장을 실행한다
# while 조건식:
#   실행문
#%%

treeHit = 0 
while treeHit < 10 : 
    treeHit += 1
    print("나무를 %02d번 찍었습니다" %treeHit)
    if treeHit  == 10:
        print("나무가 넘어갑니다")
        