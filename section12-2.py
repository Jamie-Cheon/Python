# Section12-1
# 파이썬 데이터베이스 연동 (SQLite)
# 테이블 조회 (retrieve data)
# CRUD (Create/Retrieve/Update/Delete)

import sqlite3

# DB 파일 조회 (없으면 새로 생성)
conn = sqlite3.connect('./resource/database.db') # 이미 존재하는 파일이라 오토커밋안해줌

# Cursor binding
c = conn.cursor()

# 데이터 조회(전체)
c.execute("SELECT * FROM users")

# 커서 위치가 변경 된다 
# 1개 로우 선택
# print('One -> \n', c.fetchone()) # now cursor is located at second data

# Choose row (3 rows from cursor locates)
# print('Three -> \n', c.fetchmany(size=3))

# Choose all rows (the rests from cursor locates)
# print('All -> \n', c.fetchall()) # return 5th data
# print('All -> \n', c.fetchall()) # return empty list []

print()

# iteration1
# rows = c.fetchall()
# for row in rows:
#   print('retrieve1 >', row) # 조회 없음 

# iteration2
# for row in c.fetchall():
#   print('retrieve2 >', row) # 조회 없음

# iteration3
# for row in c.execute("SELECT * FROM users ORDER BY id desc"):
#   print('retrieve3 >', row)  

print()

# WHERE retrieve1
param1 = (1,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('param1', c.fetchone())
print('param1', c.fetchall()) # return empty data: cursor is only pointed id == 1

print('-------')

# WHERE retrieve2
param2 = 1
c.execute("SELECT * FROM users WHERE id='%s'" % param2)
print('param2', c.fetchone())
print('param2', c.fetchall())

print('-------')

# WHERE retrieve3 (dictionary{"key" : Value})
c.execute("SELECT * FROM users WHERE id= :Id", {"Id": 1})
print('param3', c.fetchone())
print('param3', c.fetchall())

print('-------')

# WHERE retrieve4
param4 = (1, 4)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print('param4', c.fetchall())

print('-------')

# WHERE retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d', '%d')" % (1, 4))
print('param5', c.fetchall())

print('-------')

# WHERE retrieve6
c.execute("SELECT * FROM users WHERE id= :id1 OR id= :id2", {"id1": 1, "id2": 4})
print('param6', c.fetchall())

print('-------')

# Use with (automatically disconnect db & close file)
with conn:
  # Dump 출력 (!important when backup Database)
  with open('./resource/dump.sql', 'w') as f:
    for line in conn.iterdump():
      f.write('%s\n' % line)
    print('Dump Print Complete.')