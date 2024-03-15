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
# 파일생성위치: Spyder IDE(Browser a working directory)
# 파일객체 얻기 : 읽기용('r')
# 파일이름, 모드, 인코딩
# 파일 읽기 함수: 파일의 모든 데이터를 한 번에 읽어서 리턴
# 읽은 데이터 = 파일객체.read()

score = open("./score.txt", 'r', encoding="utf8")
data = score.read()
score.close()

print(data)
#%%
# ex: txt파일에서 추가한 내용 + enter해주어야함.
# 파일 읽기 함수: 파일을 라인 단위로 읽어서 리턴
# 읽은 데이터 = 파일객체.readline()
sfl = open("./score.txt", 'r', encoding='utf8')
while True:
    txtline = sfl.readline() # 한 라인 씩 읽기(라인의 끝: \n)
    if not txtline:
        print("\n[END OF FILE]")
        break
    
    print(txtline, end='')

sfl.close()
#%%
# 파일 읽기 함수: 파일을 라인 단위로 전체를 한 번에 읽어서 리턴
# 리스트 = 파일객체.readlines()

sfls = open("./score.txt", 'r', encoding='utf8')

txtlines = sfls.readlines()
print(txtlines)  # ['수학: 77\n', '영어: 88\n', '국어: 100\n', '과학: 23\n']
#%%

for txtline in txtlines:
    print(txtline, end='')

sfls.close()
#수학: 77
#영어: 88
#국어: 100
#과학: 23