# Section09
# 파일 읽기, 쓰기

# 읽기 모드 r, 쓰기 모드(기존 파일 삭제) w, 추가 모드(파일 생성 또는 추가) a
# 기타 : https://docs.python.org/3.7/library/functions.html#open
# 상대 경로('../', './'), 절대 경로 확인('C:\...')

# 파일 읽기
# 예제1
f = open('./resource/review.txt', 'r')
contents = f.read()
print(contents)
# print(dir(f))
# 반드시 close 리소스 반환
f.close()

print('----------------------------------')
print('----------------------------------')

# 예제2
with open('./resource/review.txt', 'r') as f:
# f = open('./resource/review.txt', 'r')랑 똑같은 구문 단지 with는 저절로 파일을 닫아줌
  c = f.read()
  print(iter(c))
  print(list(c))
  print(c)

print('----------------------------------')
print('----------------------------------')

# read : 전체 내용 읽기, read(10) : 10글자 읽기 

# 예제3
with open('./resource/review.txt', 'r') as f:
  for c in f: # 라인단위로 가져옴 
    # print(c)
    print(c.strip())

print('----------------------------------')
print('----------------------------------')


# 예제4
with open('./resource/review.txt', 'r') as f:
  contents = f.read()
  print('>', contents)
  contents = f.read()
  print('>', contents) # empty
  f.seek(0, 0) # return to starting point? 
  contents = f.read()
  print('>', contents)

print('----------------------------------')
print('----------------------------------')


# 예제5
# readline : 한 줄씩 읽기, readline(문자수) : 문자수 읽기
with open('./resource/review.txt', 'r') as f:
  line = f.readline()
  while line:
    print(line, end='')
    line = f.readline()
  

print('----------------------------------')
print('----------------------------------')


# 예제6
# readlines : 전체 읽은 후 라인 단위 리스트 저장
with open('./resource/review.txt', 'r') as f:
  contents = f.readlines()
  print(contents)
  print()
  for c in contents:
    print(c, end='')

print()
print('----------------------------------')
print('----------------------------------')


# 예제7
with open('./resource/score.txt', 'r') as f:
 score = []
 for line in f: # 라인단위로 가져옴 
   score.append(int(line)) 
   # 텍스트파일에서 가져온건 무조건 문자로 취급되기 때문에 형변환
  
 print(score)
 print('Average : {:6.3f}'.format(sum(score)/len(score)))
 # 여섯자리고 소수점 셋째자리까지 

 # 파일 쓰기

 # 예제1
with open('./resource/test.txt', 'w') as f:
# 없는 파일도 열어주기 
  f.write('niceman!\n')

 # 예제2
with open('./resource/test.txt', 'a') as f:
  f.write('niceman!!\n')

 # 예제3
from random import randint # 파이썬에서 만들어놓은 패키지 (빌트인같은)

with open('./resource/score2.txt', 'w') as f:
  for cnt in range(6): # 0부터 5까지 총 여섯번 반복
    f.write(str(randint(50, 100))) # 50~100이하의 랜덤숫자
    # write(무조건 str이어야함)
    f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/test2.txt', 'w') as f:
  list = ['Kim\n', 'Park\n', 'Lee\n']
  f.writelines(list)

# 예제5
with open('./resource/test3.txt', 'w') as f:
  print('Test Contents!', file=f)
  print('Test Contents!!', file=f)
