# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수 

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재 인스턴스 생성 후 사용 

# 예제1

class UserInfo:
  def __init__(self, name): # 인스턴스 생성시에 호출되는 함수
    self.name = name
  
  def print_info(self):
    print("Name: " + self.name)

  def __del__(self): # 인스턴스가 종료가 될때 호출되는 함수
    print("Instance removed!") # 왜 저절로 호출되는겨???


user1 = UserInfo("Kim")
user2 = UserInfo("Park")

print(id(user1))
print(id(user2))

user1.print_info()
user2.print_info()

print('user1 : ', user1.__dict__) # 클래스 네임스페이스 확인
print('user2 : ', user2.__dict__)

print(user1.name)
print()

# practice2
# self의 이해 

class SelfTest:
  def function1(): #클래스 함수 (클래스만 호출가능)
    print("function1 called")

  def function2(self):
    print(id(self))
    print("function2 called!")

f = SelfTest() # 인자를 받는 생성자 함수가 클래스내에 없어서 인자없이 생성도 가능한듯
# print(dir(f))
print(id(f))
# f.function1() 예외 발생
f.function2()
print(SelfTest.function1())
print(SelfTest.function2(f))

# print(SelfTest.function2()) 예외 발생 


# 예제3
# 클래스 변수, 인스턴스 변수

class Warehouse:
  # 클래스 변수
  stock_num = 0

  def __init__(self, name):
    # 인스턴스 변수
    self.name = name
    Warehouse.stock_num += 1

  def __del__(self):
    Warehouse.stock_num -= 1

user1 = Warehouse("Kim")
user2 = Warehouse("Park")

print()

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(Warehouse.__dict__) # 클래스 네임스페이스, 클래스 변수 (공유)

# Warehouse.stock_num = 50  # 직접 접근 가능 

print(user1.stock_num) # 자기 네임스페이스에 없으면 클래스 네임스페이스가 가서 변수를 찾음
print(user2.stock_num)