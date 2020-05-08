# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# 1 (list comprehension)
print(''.join(q1[s] for s in q1 if s == '가을'))

#2
for k in q1.keys():
  if k == "가을":
    print(q1[k])

# 3
for k, v in q1.items():
  if k == "가을":
    print(v)

# ___________My Code____________
# for i in q1:
#   if i == "가을":
#     print("가을 과일: ", q1[i])
#     break
#______________________________

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

#1
hasApple = ['Apple found!' for key, val in q2.items() if key == '사과' or val == '사과']

if len(hasApple) > 0:
  print(hasApple)
else:
  print('No Apple')

#2
for k,v in q2.items():
  if v == '사과':
    print(k, v)
else:
  print("사과 없음")

# ___________My Code____________
# for i in q2:
#   if q2[i] == "사과":
#     print(q2[i], "found!!!")
#     break
# else:
#   print("There is no apple...")

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

# ___________My Code____________

a = 77

if a >= 81:
  print("A")
elif a >= 61:
  print("B")
elif a >= 41:
  print("C")
elif a >= 21:
  print("D")
else:
  print("E")


# i = 68

# if i in range(81, 101):
#   print("A학점")
# elif i in range(61, 81):
#   print("B학점")
# elif i in range(41, 61):
#   print("C학점")
# elif i in range(21, 41):
#   print("D학점")
# else:
#   print("E학점")

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a, b, c = 12, 6, 18

best = a

if b > a:
  best = b
if c > b:
  best = c
print('best : ', best)

# ___________My Code____________

# i = [12, 6, 18]
# n = 0
# max_num = 0

# while n < len(i):
#   if max_num < i[n]:
#     max_num = i[n]
#   n += 1

# print(max_num)
  

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

s = '891022-3473837'

if int(s[7]) % 2 == 1: # %2 == 0 이면 짝수번호
  print("Male")
else:
  print("Female")

# ___________My Code____________

# if s[7] == '1' or s[7] == '3':
#   print("Male")
# elif s[7] == '2' or s[7] == '4':
#   print("Female")

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정", "을"]

#1
print(''.join([v for v in q3 if v != '정']))

#2
for v in q3:
  if v == "정":
    continue
  else:
    print(v, end='')

print()
# ___________My Code____________

# for i in q3:
#   if i == "정":
#     continue
#   else:
#     print(i)

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

#1
print(''.join([str(s) for s in range(1, 101) if int(s) % 2 != 0]))

#2
for n in range(1, 101):
  if n % 2 != 0:
    print(n, end=',')

# ___________My Code____________
# for i in range(1, 101, 2):
#   print(i)

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

#1
print([v for v in q4 if len(v) >= 5])

#2
print()
for v in q4:
  if len(v) >= 5:
    print(v, end=' ')

# ___________My Code____________

# n = 0

# while n < len(q4):
#   if len(q4[n]) >= 5:
#     print(q4[n])
#   n += 1

print()
# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

#1
print([v for v in q5 if v.islower()])

#2
print()
for v in q5:
  if v.isupper():
    continue
  else:
    print(v, end=' ')

# ___________My Code____________

# n = 0

# while n < len(q5):
#   if q5[n].islower():
#     print(q5[n])
#   n += 1 

# print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

#1
print([s.upper() if s.lower() else s.lower() for s in q5])

#2
for v in q6:
  if v.isupper():
    print(v.lower())
  else:
    print(v.upper())

# ___________My Code____________

# n = 0

# while n < len(q6):
#   if q6[n].islower():
#     print(q6[n].upper())
#   else:
#     print(q6[n].lower())
#   n += 1

