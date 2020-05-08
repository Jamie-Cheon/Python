# Section11
# 파이썬 예외처리의 이해 
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

import csv

# practice1
with open('./resource/sample1.csv', 'r') as f:
  reader = csv.reader(f)
  # next(reader) Header 스킵 (1번째 라인 스킵, 보통 첫번째라인은 머릿글임(칼럼))
  # 확인
  print(reader) # reader object 
  print(type(reader)) # reader is a class in csv
  print(dir(reader)) # check all methods inside reader class # __iter__ 확인
  print()

  # for c in reader: # retrieve each line in list [] format 
  #    print(c) # unicodeError 

  
# practice2
with open('./resource/sample2.csv', 'r') as f:
  reader = csv.reader(f, delimiter='|') # 구분자 선택, |로 구분되 있는걸 ,로 바꿔라 
  # UnicodeError
  # for c in reader:
  #   print(c)

# practice3 (Dict 변환)
with open('./resource/sample1.csv', 'r') as f:
 reader = csv.DictReader(f) # key와 value 형태로 반환, 즉 딕셔너리 형태로 각줄을 반환 
 
#  UnicodeError
#  for c in reader:
#    for k, v in c.items():
#      print(k, v)
#    print('------')


# practice4
w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15]] # 이중리스트

with open('./resource/sample3.csv', 'w') as f:
  wt = csv.writer(f)
  print(dir(wt))
  print(type(wt))
  for v in w: # 리스트들을 순회해서 씀 (한줄씩 if문을 써서 검증한 다음 파일에 쓸때 보통씀)
    wt.writerow(v) # 하나의 리스트는 한줄로 들어감, 총 6줄


# practice5
with open('./resource/sample4.csv', 'w', newline='') as f:
  wt = csv.writer(f)
  print(dir(wt))
  print(type(wt))
  wt.writerows(w) # 한번에 쓸때 (보통 검증이 된 정보일때)


# XSL, XLSX : MIME - applications/vnd.excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
# pip install pandas 설치 필요
# pip install xlrd   설치 필요
# pip install openpyxl 설치 필요

# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 등 있으나 pandas를 주로 사용(openpyxl, xlrd) 포함

import pandas as pd

xlsx = pd.read_excel('./resource/sample.xlsx')
# sheetname='시트명' 또는 숫자(시트에 이름을 지어줄떄, 시트가 여러개일떄는 숫자로 해주는게 조음), header=3(몇번쨰열을 헤더로 지정할건지), skiprow=1 (몇번째행은 가져오지않을껀지)실습

# 상위 데이터 확인
print(xlsx.head()) # retrieve from 1st ~ 5th line 
print()

# 하위 데이터 확인
print(xlsx.tail()) # retrieve last 5 lines 
print()

# 데이터 구조
print(xlsx.shape) # 행, 열

# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False) # 인덱스는 열에다가 숫자를 붙여주는것 0, 1, 2 이런식으로 
xlsx.to_csv('./resource/result.csv', index=True)
