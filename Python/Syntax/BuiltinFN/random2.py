# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 11:31:52 2024

@author: Shin
"""

# random() , randint()
# 난수(규칙이 없는 임의의 수)를 발생시키는 모듈
#%%
# random() : 0~1.0 사이의 값, 1.0보다 작은 값

import random

for n in range(10):
    x = random.random()
    print(x)
    """
    0.7821153065588374
    0.6532051116238194
    0.5023584691621799
    0.49728720470666055
    0.8359896789676603
    0.8933671960105994
    0.2058847665847825
    0.9841879000291944
    0.9389339823293302
    0.3481986933102812
    """
    
#%%

# 1부터 6까지 숫자를 2번 발생시켜라 y.xf: 소수점 이하 x자리까지만 표현/ y는 문자의 자릿수의 개수설정
for n in range(2):
    x = random.random()
    y = x * 6 경우의 갯수 
    z = int(y) + 1
    print(f"{z}: {x:.5f}, {y:.5f}")
    
    
#%%
# 0부터 10까지 숫자를 20번 발생시켜라 
# 소숫점 5자리 이하 버리고 발생된 난수 출력: trunc() d = 정수/ f = 부동소수
# random() : 0~1.0 사이의 값, 1.0보다 작은 값
# import math # 수학 모듈     x = trunc(x, 5) # 소숫점 5자리 절사
# round(number[,ndigits]) 숫자를 입력받아 반올림해 리턴하는 함수 round(x, 5) 
# 소숫점 5자리 반올림
s = 10 # 시작값
e = 20 # 마지막값
m = 20 # 발생 횟수

for n in range(20):
    x = random.random() # 난수생성
    y = x * (e-s+1) # 경우의 갯수로 환산(0이상 10미만의 난수생성) 
    z = int(y) + s # 정수만 가져오기
    rx = round(x, 5) # 소숫점 5자리 반올림
    print(f"{z:2d}: {rx}, {y:.5f}")
    
#%% 
# 문제 
# 1부터 45까지 난수를 발생시켜 6개의 충돌되지 않는 조합을 만들어라 
ls = 1 # 시작값
le = 45 # 종료값
lc = 6 # 갯수
lotto = [] # 총 6개 난수를 저장할 리스트

import random


# Solution 1:
while len(lotto) < lc:
    number = random.randint(ls,le)
    if number not in lotto: # 중복허용 x
                lotto.append(number)
print("로또번호", lotto)
# 로또번호 [18, 8, 31, 9, 17, 21]

# Solution 2:
def generate_lotto_numbers(start, end, count):
    lotto = []  # 로또 번호를 저장할 리스트
    while len(lotto) < count:
        number = random.randint(start, end)  # 시작값과 종료값 사이의 난수 생성
        if number not in lotto:  # 중복되지 않는 난수인 경우에만 리스트에 추가
            lotto.append(number)
    return lotto

# 함수 테스트
start = 1
end = 45
count = 6
lotto_numbers = generate_lotto_numbers(start, end, count)
print("로또 번호:", lotto_numbers)

           
# solution 3        
i = 0
while i < lc:
    num = random.randint(ls, le)  # ls부터 le까지의 난수 생성
    if num not in lotto:
        lotto[i] = num
        i += 1

print("로또 번호:", lotto)




# solution teacher
import random
s = 1 # 시작값
le = 45 # 종료값
lc = 6 # 갯수
ls = 1
lotto = [0,0,0,0,0,0] # 총 6개 난수를 저장할 리스트

nx = 0 
n = 0 
while True:
    if n >= lc:
        break
    x = random.random() # 난수
    y = x * (le-ls+1) # 경우의 갯수 환산(45개)
    z = int(y) + ls
    rx = round(x,5)
    print(f"[{nx}] {z:2d}: {rx}, {y:.5f}")
    if z not in lotto: # 동일한 번호 확인
        lotto[n] = z
        n += 1

    nx += 1
    
print("lotto:", lotto)

"""
[0] 23: 0.48988, 22.04456
[1] 36: 0.78545, 35.34524
[2] 16: 0.33791, 15.20596
[3]  4: 0.08041, 3.61853
[4]  9: 0.18729, 8.42803
[5] 25: 0.54127, 24.35710
lotto: [23, 36, 16, 4, 9, 25]
"""

# random 모듈활용
import random

def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))

# 꺼낸 요소는 pop 메서드에 의해 사라진다.

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number





    
    


    
    
    