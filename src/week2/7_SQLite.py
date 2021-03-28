# 파이썬 db 연동
# 파이썬 일정 버전 이상에는 포함되어있음

import sqlite3

print(sqlite3.version)  # version
print(sqlite3.sqlite_version)  # eb engine ver
print(sqlite3.sqlite_version_info)  # version tuple

# 삽입 날짜 생성
import datetime

now = datetime.datetime.now()  # 많이 쓰니까 알아두자
print(now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# DB 생성 & auto commit, rollback
# auto commit on
conn = sqlite3.connect('./resource/database.db', isolation_level=None)

# cursor 얻기
c = conn.cursor()
print(type(c))

# drop table if iexists
c.execute('DROP TABLE IF EXISTS users  ')

# 테이블 생성
# filed type : TEXT, NUMERIC, INTEGER, REAL, BLOB
c.execute('CREATE TABLE IF NOT EXISTS users(\
        id INTEGER PRIMARY KEY,\
        username TEXT,\
        email TEXT,\
        phone TEXT,\
        website TEXT,\
        regdate TEXT)')

# data 삽입
# ''안에서 문자열은 ""로 묶을것 (아니면 반대로 하던지)
# nowdatetime : 넣으면 문자열이므로 파라미터 치환 필요
print(type(nowDatetime))
print(type((nowDatetime)))
print(type((nowDatetime,)))  # tuple

# 모든 data 순서대로 insert
c.execute('INSERT INTO users VALUES(\
    1,"Kim","Kim@naver.com","010-1234-1234","kim.com",?)', (nowDatetime,))
# 다른 방법
c.execute('INSERT INTO users(id,username,email,phone,website,regdate) VALUES(?,?,?,?,?,?)',
          (2,
          "Park",
          "Park@naver.com",
          "010-0000-0000",
          "Park.net",
          nowDatetime,))

# 복수 삽입(튜플, 리스트)
userList=(
    (3,"Yoo","Yoo@naver.com","010-0000-0000","Yoo.net",nowDatetime,),
    (4, "Lee", "Lee@naver.com", "010-0000-0000", "Lee.net", nowDatetime,),
    (5, "Cho", "Cho@naver.com", "010-0000-0000", "Cho.net", nowDatetime,)
)
c.executemany('INSERT INTO users(id,username,email,phone,website,regdate) VALUES(?,?,?,?,?,?)',userList)

# 데이터 삭제
# c.execute('DELETE FROM users') # 작동함
# conn.execute('DELETE FROM users') # 작동함
# print('Delete rows : ', conn.execute('DELETE FROM users').rowcount)


# 커밋 : DB Isolatiaon_level = none  -> 무조건 반영 , 오토 커밋
# conn.commit()
# conn.rollback()

conn.close()