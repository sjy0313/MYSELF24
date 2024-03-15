# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:03:34 2024

@author: Shin
"""

# 파일 입출력
# 함수: open(), close(), read(), write(), readline(), readlines()
# 파일 입출력 순서: 
#   - 오픈
#   - 읽거나 쓰기
#   - 닫기
# 파일의 종류:
#   -택스트:(ASCII, UTF-8), txt, csv, py, java, c, cpp, xml, html, sql, json
#   -바이너리: doc, hwp, xls, pdf, jpg, gif, exe, dll
#%%
# 택스트 파일 처리

# 파일객체 얻기 : 쓰기용
# 파일이름, 모드, 인코딩
# 모드 ('w'): 파일이 존재하지 않으면 새로 생성, 존재하면 기존의 내용을 다 지우고 덮어 씀.
score_file = open("./score.txt", 'w', encoding="utf8")
print("수학: 77", file=score_file)
print("영어: 88", file=score_file)
score_file.close()
#%%
score1_file = open("./score-1.txt", 'w', encoding="utf8")
score1_file.write("국어: 100\n")
score1_file.write("수학: 70\n")
score1_file.write("영어: 80\n")# write 하나의 문자열로 출력가능
score1_file.close() 
#%%
# 모드('a') : 파일이 존재하지 않으면 새로 생성, 존재하면 기존의 내용 뒤에 추가
# a = append(확장의 의미)
score2_file = open("./score-2.txt", 'a', encoding="utf8")
score2_file.write("국어: 100\n")
score2_file.write("수학: 70\n")
score2_file.write("영어: 80\n")
score2_file.write("과학: 60\n")
# write 하나의 문자열로 출력가능
score2_file.close() 


