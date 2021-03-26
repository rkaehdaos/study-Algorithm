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
# 테이블 생성
# filed type : TEXT, NUMERIC, INTEGER, REAL, BLOB
c.execute('CREATE TABLE IF NOT EXISTS users(\
        id INTEGER PRIMARY KEY,\
        username TEXT,\
        email TEXT,\
        phone TEXT,\
        website TEXT,\
        regdate TEXT)')
# 테이블 삽입
