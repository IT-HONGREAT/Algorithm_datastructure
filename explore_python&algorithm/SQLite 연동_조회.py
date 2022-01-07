import sqlite3



#DB 파일 조회 (없으면 새로 생성)

conn = sqlite3.connect('/explore_python&algorithm/resource/database.db')

# 커서 바인딩

c = conn.cursor()

# 데이터 조회(전체)

c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택

# print('One -> \n', c.fetchone())
#
#
# # 지정 로우 선택
#
# print('Three -> \n', c.fetchmany(size=3))
#
# # 전체 로우 선택
#
# print('ALL -> \n', c.fetchall())
#
#
# print('ALL -> \n', c.fetchall())


# 순회 1

# rows = c.fetchall()
# for row in rows:
#     print(row)

# 순회 2
# for row in c.fetchall():
#     print("이게더 빠름",row)


# 순회 3

# for row in c.execute("SELECT * FROM users ORDER BY id desc "):
#     print("코드가독성 안좋음",row)


# WHERE

param1 = (3,)
c.execute("SELECT * FROM users WHERE id=?",param1)
print(c.fetchone())
print(c.fetchall()) # 이거는 테스트 한거임


# WHERE 2 포매팅으로 출력

param2 = 4
c.execute("SELECT * FROM users WHERE id='%s'" %param2)  # %f %s %d
print(c.fetchone())
print(c.fetchall()) # 이거는 테스트 한거임

# WHERE 3 딕셔너리로 이용


c.execute("SELECT * FROM users WHERE id=:ID", {'ID':5})
print(c.fetchone())
print(c.fetchall()) # 이거는 테스트 한거임


# WHERE 4

param4 = (1,2)
c.execute("SELECT * FROM users WHERE id IN(?,?)",param4)

print(c.fetchall())


# WHERE 5

param5 = (4,3)
c.execute("SELECT * FROM users WHERE id IN('%d', '%d')" %param5)

print(c.fetchall())

# WHERE 6

c.execute("SELECT * FROM users WHERE id=:ID1 OR id=:ID2", {'ID1':5,'ID2':2})

print(c.fetchall())



# DUMP 출력

with conn:
    with open('/explore_python&algorithm/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' %line)

        print("Dump complete")

# f.close()