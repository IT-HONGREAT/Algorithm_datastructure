# 테이블 데이터 수정 및 삭제

import sqlite3

conn = sqlite3.connect('/explore_python&algorithm/resource/database.db')

c = conn.cursor()

# 데이터 수정1
# c.execute("UPDATE users SET username = ? WHERE id = ? ", ('niceman',2))

# 데이터 수정2
c.execute("UPDATE users SET username = :name WHERE id = :id ", {'name': 'winter', 'id': 2})


# 데이터 수정3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s' " % ('karina(wife)',3))

# 커밋해야 반영됨
conn.commit()


# 데이터 확인

for i in c.execute("SELECT * FROM users"):
    print(i)

print("여기부터 삭제")
# 데이터 삭제1
c.execute("DELETE FROM users WHERE id=?",(3,))

# 데이터 삭제2
c.execute("DELETE FROM users WHERE id= :id", {'id': 5})

# 데이터 삭제3
c.execute("DELETE FROM users WHERE id= '%s'" % 4)


# 데이터 확인

for i in c.execute("SELECT * FROM users"):
    print(i)


# 데이터 전체삭제

print("데이터 몇개의 row를 삭제했는지? : ",c.execute("DELETE FROM users").rowcount)