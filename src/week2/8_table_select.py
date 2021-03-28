# 테이블 조회
# 7번 파일의 db 설정 필요

import sqlite3

conn = sqlite3.connect('./resource/database.db')  # isolation 설정 없음

# cusor binding
c = conn.cursor()

# select 전체
c.execute('SELECT * FROM users')
# 커서 위치 변경

# 1개 row 선택
print('One -> \n', c.fetchone())
# size 지정
print('three -> \n', c.fetchmany(size=3))

# 전체 row
print('all -> \n', c.fetchall())  # 전체 다 출력 된 상황
print('all -> \n', c.fetchall())  # 다시 출력하려 하면 빈 리스트

print('----------------------------------')

# 순회 테스트


# 순회1
c.execute('SELECT * FROM users')
rows = c.fetchall()
print(type(rows))
for row in rows:
    print('순회1 > ', row)

print('----------------------------------')

# 순회2
c.execute('SELECT * FROM users')
for row in c.fetchall():
    print('순회2 > ', row)

# 순회3
# 가독성이 내려갈 수 있음 : SQL이 길어질 수 있으므로

for row in c.execute('SELECT * FROM users ORDER BY id desc'):
    print('순회3 > ', row)

print('----------------------------------')

# where
# Retrieve1
param1 = (3,)
c.execute('SELECT * FROM users WHERE id=?', param1)
print('Retrieve1: ', c.fetchone())  # 3이 하나이므로
print('Retrieve1: ', c.fetchall())  # 다음 데이터가 없음
print('----------------------------------')

# 순회2 : integer binding
# % 구문 다시 잘 생각해보자
# %s, %f, %d
param2 = 4
c.execute('SELECT * FROM users WHERE id="%s"' % param2)
print('Retrieve2: ', c.fetchone())
print('Retrieve2: ', c.fetchall())
print('----------------------------------')

# 순회3 딕셔너리
c.execute('SELECT * FROM users WHERE id=:Id', {'Id': 5})
print('Retrieve3: ', c.fetchone())
print('Retrieve3: ', c.fetchall())
print('----------------------------------')

# Retrieve4
param4 = (3, 5)
c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)
print('Retrieve4: ', c.fetchall())
print('----------------------------------')
# 같은 데 다른 표현
c.execute('SELECT * FROM users WHERE id IN("%d","%d")' % (3, 4))
print('Retrieve4: ', c.fetchall())
print('----------------------------------')

# Retrieve5 : dict
c.execute('SELECT * FROM users WHERE id=:id1 OR id=:id2', {'id1': 3, 'id2': 5})
print('Retrieve5: ', c.fetchall())

c.close()


# Dump 출력  : DB 백업등
# 파일 open과 conn 전부 close가 자동 : with
with conn:
    with open('./resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump print complete....')
