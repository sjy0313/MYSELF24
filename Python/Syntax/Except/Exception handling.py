# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 21:52:03 2024

@author: 신정윤
"""

try:
    # 예외가 발생할 수 있는 코드
    x = int(input("정수를 입력하세요: "))
    result = 10 / x
    print("결과:", result)

except ZeroDivisionError:
    # 0으로 나누는 경우의 예외 처리
    print("Error: 0으로 나눌 수 없습니다.")

except ValueError:
    # 유효하지 않은 정수 입력 시의 예외 처리
    print("Error: 올바른 정수를 입력하세요.")

except Exception as e:
    # 그 외의 예외에 대한 처리
    print(f"Error: {e}")

else:
    # 예외가 발생하지 않은 경우 실행
    print("예외가 발생하지 않았습니다.")

finally:
    # 예외 발생 여부와 관계없이 항상 실행
    print("항상 실행되는 부분")