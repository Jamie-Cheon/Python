# Section04-1
# 파이썬 데이터 타입(자료형)
# 데이터 타입, 숫자형, 숫자형 연산 

'''
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전

bytearray
byte
frozenset
'''

# 데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7 
v_set = {7, 8, 9}

# 데이터 타입 출력
print(type(v_tuple))
print(type(v_set))
print(type(v_int))
print(type(v_bool))
print(type(v_list))
print(type(v_dict))
print(type(v_str1))
print(type(v_str2))

# Numeric Operation (숫자형 연산자)
# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
"""
+ 
- 
* 
/ 
// : 몫 
% : 나머지
abs(x) 
int(x) 
float(x) 
complex(x)
pow(x, y) 
x ** y : 제곱
....
"""

# 정수 선언
i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999999999999
big_int2 = 7777777777777777777777777777777777777777

# 실수 선언
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

# 정수 출력 
print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2)

result = f3 + i2
print(result, type(result))

a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a + b 
print(result2)

# 형변환
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True))
print(int(False))
print(int('3'))
print(complex(False))


y = 100
y *= 100
print(y)

# 수치 연산 함수

print(abs(-7)) # abs: 절대값구해주는 함수
n, m = divmod(100, 8)
print(n, m)

import math

print(math.ceil(5.1))  # x 이상의 수 중에서 가장 작은 정수
print(math.floor(3.874)) # x 이하의 수 중에서 가장 큰 정수

#pi
print(math.pi)

# 그 밖에 함수는 아래 URL 참조
# https://docs.python.org/3/library/math.html


# 2진수 변환
print(bin(50)) #0b로 시작
