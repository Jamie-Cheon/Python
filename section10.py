# Section10
# 파이썬 예외처리의 이해 

# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError...
# 문법적으로 에러가 없지만 코드 실행 프로세스에서 발생하는 예외 처리 중요

# SyntaxError : 잘못된 문법

# print('test)
# print('Hello'))
# if True
#    pass
# a = 20; b = 30; a+ = b
# x => y


# NameError : 참조 변수 없음

a = 10
b = 15

# print(c)


# ZeroDivisionError : 0 나누기 에러

# print(10 / 0)


# IndexError : 인덱스 범위 오버

x = [10, 20, 30]

# print(x[1])
# print(x[3]) # 예외 발생
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop()) # 예외 발생
# print(x.pop(50)) # 예외 발생


# KeyError

dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}

# print(dic['hobby'])     # 키가 존재하지 않으면 예외
# print(dic.get('hobby')) # 안전


# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시 예외처리 권장(EAFP 코딩 스타일)


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

# print(time.time())
# print(time.month()) # 예외 발생

x = [1, 2, 3]
# print(x.append(4))
# print(x.add(10)) # 예외 발생 : list object has no attr 'add'

# ValueError : 참조 값이 없을 때 예외

x = [1, 5, 9]

# x.remove(5)
# print(x)

# x.remove(100)
# print(x) # 예외 발생

t = (10, 100, 1000)

print(t.index(100))
# print(t.index(7)) # 예외 발생


# FileNotFoundError

# f = open('test.txt') # 얘외 발생


# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우

x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y) # 예외 발생
# print(x + z) # 예외 발생
# print(y + z) # 예외 발생
# print(sum([1,2,3],10,1)) # 예외 발생

# print(x + list(y))
# print(x + list(z)


# 예외 처리 기본
# try               에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1:    에러(예외)가 발생할 경우.여러 개 가능(에러 처리)
# except 에러명2: 
# else:             try 블록의 에러가 없을 경우 실행
# finally:          항상 실행

# practice1

name = ['Kim', 'Lee', 'Park']

try: 
  z = 'Kim' # 'Cho' error occur
  x = name.index(z) # kim이 있는 index 반환, x = 0
  print('{} found it! {} in name'.format(z, x+1))
except ValueError: 
  # 값이 없어서 에러가 발생했을 경우
  print('Not found it! - Occured ValueError')
else: 
  # 에러가 발생하지 않았을 경우 실행 
  # 트라이문이 정상적으로 실행됬을 경우만 실행
  print('ok! else!')


# practice2

try:
  z = 'Kim' 
  x = name.index(z)
  print('{} found it! {} in name'.format(z, x+1))
except: 
  # 모든 에러를 처리(exception), 어떤 에러가 발생할지 모를경우
  print('Not found it! - Occured Error')
else:
  print('ok! else!')


# practice3

try:
  z = 'Kim' 
  x = name.index(z)
  print('{} found it! {} in name'.format(z, x+1))
except Exception as e: 
  # 에러 내용 출력
  # pass # 임시로 에러 해결 시 예외 처리
  print(e)
else:
  print('ok! else!')
finally:
  # 무조건 실행 (에러가 발생하던 발생하지 않던)
  print('ok! finally!')

print('-----------------------------')

# practice4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
  a = 'Park'
  if a == 'Kim':
    print('Ok! pass')
  else:
    # try구문에서 발생한 에러가 파이썬에서 규정하는 ValueError가 아니지만 사용자가 직접 지금 발생한 에러가 벨류에러라고 raise하는것
    raise ValueError 
except ValueError:
  print('Raise! Occured ValueError')
except Exception: 
  # 이것도 저것도 아니면 얘가 잡겠다 
  # 무조건 다른 에러들 보다 순서가 마지막에 와야함 
  # 먼저오면 얘가 모든 에러를 다잡음 
  print('Occured Exception')
else:
  print('ok! else!')
    
