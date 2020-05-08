# Section13-1.py
# Typing game 
# Complete basic structure 

# Import 
import random
import time
import sqlite3          # DB 
import datetime         # To read a record time 

# Variables
words = []              # Store words
cnt = 1                 # Game count
val = ''                # Input value
cor_cnt = 0             # Number of correct answer

# Create/Connect DB & Autocommit
conn = sqlite3.connect('./resource/records.db', isolation_level=None)
# connect cursor 
c = conn.cursor()       
# Create Table (Datatype : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record TEXT, regdate TEXT)")


# Connect words file 
with open('./resource/word.txt', 'r') as f:
    for i in f:                       # Store words to variable 'words'  
      words.append(i.strip())         # Strip() : remove white spaces  

# print(words)                         # Check words list  
input("Ready? Press Enter Key!!")     
st = time.time()                      # Store start time after enter 

# Game Start
while cnt <= 5:
  random.shuffle(words)               # shuffle words in the list 
  q = random.choice(words)            # extract word randomly

  print()
  print("Question {}".format(cnt))
  
  val = input(q + '\n')               # store input
  
  if str(val).strip() == str(q).strip():
    print("pass!!")
    cor_cnt += 1                      # increase number of correct answer
  else:
    print("Wrong!!")

  cnt += 1                            # increase game count 


et = time.time()

tt = et - st
tt = format(tt, ".3f")
# Insert records to DB
c.execute(
  "INSERT INTO records('cor_cnt','record','regdate') VALUES(?,?,?)",
  (
     cor_cnt, tt, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
  )
)

# Disconnect DB
conn.close()

# Show game result
print("\nCorrect Answer : {}".format(cor_cnt), "\nTotal time : ", tt, "sec")

# start point
if __name__ == '__main__':
  pass