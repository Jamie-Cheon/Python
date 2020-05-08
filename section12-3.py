# Section12-3
# 파이썬 데이터베이스 연동(SQLite)
# Table Update & Delete

import sqlite3

# Create/Connect db file
conn = sqlite3.connect('./resource/database.db')

# Connect cursor
c = conn.cursor()

# Update data1
c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 1))

# Update data2
c.execute("UPDATE users SET username = :name WHERE id = :id", {"name": 'goodman', 'id': 3})

# Update data3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 5))

# Retrieve data 
for user in c.execute('SELECT * FROM users'):
  print(user)

# Row delete1
c.execute("DELETE FROM users WHERE id = ?", (1,))

# Row delete2
c.execute("DELETE FROM users WHERE id = :id", {"id": 2})

# Row delete3
c.execute("DELETE FROM users WHERE id = '%s'" % 9)

# Delete all data
print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

# commit
conn.commit()
# disconnect db
conn.close()