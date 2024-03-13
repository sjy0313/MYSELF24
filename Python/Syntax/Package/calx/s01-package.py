# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:07:08 2024

@author: Shin
"""

# 패키지(package)
#   -폴더(folder)
# 파이썬 파일들을 모아놓은 폴더
#   -여러 모듈(module)을 모아 놓은 폴더(folder)


# [패턴1]
"""
import 폴더.폴더.모듈

폴더.폴더.모듈.함수(...)
폴더.폴더.모듈.변수
"""




# [패턴2]
"""
from 폴더.폴더 import 모듈
모듈.함수(...)
모듈.변수
"""
# [패턴3]
"""
해당 모듈을 지정하면 모듈명 생략
기능: 함수, 변수, 클래스
from 폴더.폴더.모듈 import 기능

사용할 떄 모듈 생략 가능
함수(...)
변수
""""

# [패턴4]
"""
최상위 폴더1을 지정
import 폴더1

사용할 떄 모듈 생략 가능
폴더1.폴더2.모듈.함수(...)
"""

# [패턴5]
"""
해당 모듈이 있는 폴더까지만 지정
from 폴더.폴더 import *

사용할 떄 폴더 생략 가능
모듈.함수(...)
"""
# [패턴6]
"""
해당 모듈이 있는 폴더까지만 지정
from 폴더.폴더 import *

사용할 떄 모듈 생략 가능
함수(...)
"""

