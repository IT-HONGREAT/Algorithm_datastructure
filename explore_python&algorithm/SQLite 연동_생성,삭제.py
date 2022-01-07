# 테이블 생성 및 데이터 삽입

import sqlite3
import datetime

print(sqlite3.version)
print(sqlite3.sqlite_version)

# 삽입날짜 생성
now = datetime.datetime.now()
print(now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M%S')
print(nowDatetime)

# DB 생성 & Auto Commit(rollback도 알아두면 좋다)

conn = sqlite3.connect('/explore_python&algorithm/resource/database.db',
                       isolation_level=None)


# Cursor

c = conn.cursor()
print(type(c))

"""생성"""
# 테이블 생성( 데이터 타입 : TEXT, NUMERIC INTEGER REAL BLOB )
# c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text,regdate text)")
#
# # 데이터 삽입
#
# c.execute("INSERT INTO users VALUES(1, 'Hong','hongreat95@gmail.com','010-0000-0000' , 'winter.com', ?) ",(nowDatetime,))
# c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)",(2, 'winter','winter@naver.com','010-1111-1111','winter.com',nowDatetime))
#
#
# # Many 삽입(튜플, 리스트 두가지 형식으로 가능)
#
# userlist = (
#     (3,'karina','karina@gmail.com','010-3333-3333','karina.com',nowDatetime),
#     (4,'nayeon','nayeon@gmail.com','010-4444-4444','nayeon.com',nowDatetime),
#     (5,'sana','sana@gmail.com','010-5555-5555','sana.com',nowDatetime)
# )
#
# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)",userlist)

"""삭제"""
# 데이터 삭제

# conn.execute("DELETE FROM users")

# 삭제하고 몇개인지 확인

# print("user db deleted : ",conn.execute("DELETE FROM users").rowcount)



# 커밋

# conn.commit()

# 롤백
# conn.rollback()

# 접속해제, 항상 닫아줘야한다.
# conn.close()





