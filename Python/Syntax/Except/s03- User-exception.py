# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:01:38 2024

@author: Shin
"""

# 사용자 예외처리(예외만들기 p238)
# Exception : 예외처리의 기반 클라스
# 예외발생: raise 예외클래스
# 상속받기
#class BirdException(Exception):
class BirdException:
    pass
#  catching classes that do not inherit from BaseException is not allowed
# 상속받지 않는 클래스들은 사용불가.

#%%
def HiBird(hi):
    if hi == 'dead':
        raise BirdException("새가 죽었습니다") # 예외발생
    print("[버드] 안녕?")
    
#%%

HiBird("잘 잤어") # [버드] 안녕?

#%%
try:
    HiBird('dead')
except BirdException as e:
    print("[예외발생]", e)
     # [예외발생] 새가 죽었습니다