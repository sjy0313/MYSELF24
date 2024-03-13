# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:01:38 2024

@author: Shin
"""

# 사용자 예외처리(예외만들기 p238)
# Exception : 예외처리의 기반 클라스
# 예외발생: raise 예외클래스
# 상속받기
class BirdException(Exception):
    def __init__(self, errno, msg='', why=''):
        super().__init__(msg, why)
        self.errno = errno
        
    def error(self):
        return self.errno

#%%
# 예외발생 raise 예외클라스
def HiBird(hi):
    if hi == 'dead': # - 1->errno, msg->새가 죽었습니다, why-> 늙어서
        raise BirdException(-1, "새가 죽었습니다", "늙어서") # 예외발생
    print("[버드] 안녕?")
    
#%%

HiBird("잘 잤어") # [버드] 안녕?

#%%
try:
    HiBird('dead')
except BirdException as e:
    print("[예외발생]", e)
     # [예외발생] 새가 죽었습니다