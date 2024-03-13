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
        super().__init__(msg, why) #부모 클라스(Exception)의 메서드를 super()로 호춯
        self.errno = errno
        
    def error(self):
        return self.errno

#%%
# 예외발생 raise 예외클라스 if statement에서 애럴를 발생시키는 경우를 작성하고
# raise statement를 통해 애러를 발생시키는데 raise + 메세지 하여 원하는 메세지 출력가능 
def HiBird(hi):
    if hi == 'dead': # - 1->errno, msg->새가 죽었습니다, why-> 늙어서
        raise BirdException(-1, "새가 죽었습니다", "늙어서") # 예외발생
    print("[버드] 안녕?")
    
#%%

HiBird("잘 잤어") # [버드] 안녕?
# https://blockdmask.tistory.com/538
#%%
try:
    # 예외가 발생할 수 있는 코드
    HiBird('dead')
except BirdException as e:
    print("[예외발생]", e)
     # [예외발생] 새가 죽었습니다