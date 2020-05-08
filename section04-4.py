# Section 04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key(가져오고자하는정보), Value(값) (Json) -> MongoDB
# 선언
a = {'name': 'Kim', 'Phone': '010-777-7777', 'birth': 870214}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr' : [1, 2, 3, 4, 5]}
# key: 'arr' value: [1,2,3,4,5] item: {'arr' : [1, 2, 3, 4, 5]}

print(type(a))

# 출력
print(a['name']) 
print(a.get('name'))
print(a.get('address')) # 코딩할때 추천하는 방법
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul' # 순서가 바껴서 나올수도 있음 순서x때문에  
print(a)
a['rank'] = [1, 3, 4] # list
a['rank2'] = (1, 2, 3) # tuple
print(a)

# keys, values, items 
print(a.keys()) # 생긴건 리스트지만 아님 
print(list(a.keys())) # 리스트로 형변환을 해야 인덱싱 가능 

temp = list(a.keys())
print(temp[1:3]) 

print(a.values())
print(list(a.values()))

print(a.items()) # key와 value를 한쌍으로 가져옴 
print(list(a.items())) # list안에 tuple이 있는 형식으로 반환됨
print(2 in b)
print('name2' not in a)

# 집합(Sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c) # 중복을 허용하지 않기때문에 6을 한번만 출력 

t = tuple(b)
print(t)
l = list(b)
print(l)

print()
print()

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8])

#교집합
print(s1.intersection(s2))
print(s1 & s2)

#합집합
print(s1 | s2)
print(s1.union(s2)) 

#차집합
print(s1 - s2)
print(s1.difference(s2))

# 추가 & 제거
s3 = set([7, 8, 10, 15])

s3.add(18)
s3.add(7) # 중복 x

print(s3)

s3.remove(15)
print(s3)

print(type(s3))
