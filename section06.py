# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def function_name(parameter):
#     code

# 함수 호출
# function_name()
# 함수 선언 위치 중요 

# practice 1 
def hello(world):
  print("Hello,", world)

param1 = "Niceman"

hello(param1)

# practice 2
def hello_return(world):
  value = "Hello, " + str(world)
  return value

str1 = hello_return("Niceman")

print(str1)

# practice 3 (다중리턴)
def func_mul1(x):
  y1 = x * 2
  y2 = x * 4
  y3 = x * 6
  return y1, y2, y3

val1, val2, val3 = func_mul1(3)

print(val1, val2, val3)

# 튜플 리턴
def func_mul2(x):
  y1 = x * 2
  y2 = x * 4
  y3 = x * 6
  return y1, y2, y3 # 튜플로 리턴 (default)

tup = func_mul2(4)

print(type(tup), tup, list(tup))

# 리스트 리턴
def func_mul3(x):
  y1 = x * 2
  y2 = x * 4
  y3 = x * 6
  return [y1, y2, y3]

lis = func_mul3(6)

print(type(lis), lis, set(lis))

# dictionary return 
def func_mul4(x):
  y1 = x * 2
  y2 = x * 4
  y3 = x * 6
  return {'ret1': y1, 'ret2': y2, 'ret3': y3}

dic = func_mul4(8)

print(type(dic), dic, dic.get('ret3'), dic.items(), dic.keys(), dic.values())
print()

# practice 4
# *args, **kwargs 

# *args 
# 여러개의 매개변수를 함수로 받고자 할때 (매개변수가 몇개가 넘어갈지 모를때 사용) 
# 튜플 형태로 넘어옴 

def args_func(*args): # 매개변수명 자유롭게 변경 가능
  for idx, val in enumerate(args): # enumerate() 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용합니다.
    # tuple 에서 몇번째 index에 있는 value 인지 
    print('{}'.format(idx), val, end=' ')

args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')

print()

# **kwargs
# (keword = value) 형태로 함수를 호출할때 

def kwargs_func(**kwargs): # 매개변수병 자유롭게 변경 가능
  for v in kwargs.keys():
    print('{}'.format(v), kwargs[v], end=' ')

kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2='Park')
kwargs_func(name1='Kim', name2='Park', name3='Lee')

print() 

# 전체 혼합
def example(arg_1, arg_2, *args, **kwargs):
  print(arg_1, arg_2, args, kwargs)

example(10, 20, 'park', 'kim', 'lee', age1=33, age2=34, age3=44)

# practice 5
# 중첩함수
def nested_func(num): 
  def func_in_func(num): # 부모펑션이 실행되고나서 자동으로 실행되는게 아니라 부모에서 자식함수를 불러줘야 실행되는구낭 
    print(num)
  
  print("In func")
  func_in_func(num + 100)

nested_func(1)

# 실행불가
# func_in_func(1)

# practice 6
# Hint
def tot_length1(word: str, num: int) -> int:
  return (len(word) * num)

print('hint exam1 :', tot_length1("I love you", 10))

def tot_length2(word: str, num: int) -> None:
  print('hint exam2 : ', len(word) * num)

tot_length2("niceman", 10)

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당 
# 람다는 즉시 실행 함수(heap 초기화) -> 메모리 초기화

# practice 7
# def mul_10(num):
#   return num * 10

# def mul_10_one(num): return num * 10 

# lambda x: x * 10

# 일반적 함수 -> 변수 할당
def mul_10(num):
  return num * 10

mul_func = mul_10

print(mul_func(5))
print(mul_func(6))

# 람다 함수 -> 할당
lambda_mul_func = lambda x: x * 10

def func_final(x, y, func):
  print(x * y * func(10))

func_final(10, 10, lambda_mul_func)