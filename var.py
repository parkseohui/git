a=[1,2,3]

id(a) # 주소값 추적 함수

b=a # 완전복사/주소까지 같음

# 다르게 복사하는법

b=a[:]

from copy import copy

b=copy(a)

# 같은지 확인하는법

a is b #true/false 값을 반환해줌

# 여러변수에 저장

(python, java)=(1,2)

