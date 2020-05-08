# Section08
# 파이썬 모듈과 패키지

# 패키지 예제1
# 상대 경로 패키지
# .. : 부모 디렉토리
# .  : 혀냊 디렉토리

# 사용1(클래스)
# from 파일명 import 가져올 클래스명
from pkg.fibonacci import Fibonacci

Fibonacci.fib(100)

print("ex1 :", Fibonacci.fib2(200))

# 인스턴스화 시켜줘야 __init__ 메소드가 실행됨 
# -> fibonacci().title (o)
# -> fibonacci.title (x)
print("ex1 :", Fibonacci().title)

# 사용2 권장 (x)
#fibonacci.py 파일에 있는 모든 클래스를 가져오겠다 
from pkg.fibonacci import *

Fibonacci.fib(300)

print("ex2 :", Fibonacci.fib2(400))
print("ex2 :", Fibonacci().title)

# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(500)

print("ex3 :", fb.fib2(600))
print("ex3 :", fb().title)

#사용4(함수) : 파일 Alias
# calculations.py 파일에 있는 모든 함수들을 가져오겠다 (함수만 있는 파일)
import pkg.calculations as c  

print("ex4 :", c.add(10, 10))
print("ex4 :", c.mul(10, 4))


# 사용5
# from 을 사용하면 가지고오고싶은 필요한 함수만 가져올수 있음
from pkg.calculations import div as d

print("ex5 :", int(d(100,10)))

# 사용6
import pkg.prints as p
import builtins

p.prt1()
p.prt2()
print(dir(p))
print(dir(builtins))