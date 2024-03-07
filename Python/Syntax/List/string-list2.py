# -*- coding: utf-8 -*-
# list()
# 여러 형태의 자료들의 연속된 모임
# 변경가능(mutable)
#%%
odd = [1,3,5,7,9]
print(odd) # [1,3,5,7,9]
#%%
# 참조: 인덱스 참조
odd = [1,3,5,7,9]
print(odd[0]) # 첫번 쨰 요소 
print(odd[-1]) # 마지막 요소

# 리스트의 길이 : len(list)
olen = len(odd)
print("길이:", olen) #  5 

print(odd[olen])
# IndexError: list index out of range # 인덱스의 범위를 넘어서면 예외발생
# 마지막 요소 : 길이 -1 또는 -1
print(odd[olen-1])   # 9
#%%

# 수정
#마지막 요소의 값 9를 10으로 변경
odd[-1] = 10
print(odd)  # [1, 3, 5, 7, 10]
