# 데이터 수정 삭제


import sqlite3

conn = sqlite3.connect('./resource/database.db')  # isolation 설정 없음
c = conn.cursor()

# update 1
# c.execute('UPDATE users SET username="Park2" WHERE id=2')

# 여기서 SQLite 보면 그냥 Park인 것을 확인 가능
# 커밋이 안되었으므로 여기세션에서만 바뀐값 확인
# conn.rollback()
# conn.commit()

# update 2
# c.execute('UPDATE users SET username=:name WHERE id=:id', {'name': 'goodman', 'id': 5})

# update 3
# c.execute('UPDATE users SET username="%s" WHERE id="%s"' %('테스트이름',3))

conn.commit()

for user in c.execute('SELECT * FROM users'):
    print(user)



# delete1
# c.execute('DELETE FROM users WHERE id=?',(2,))

# delete2
# c.execute('DELETE FROM users WHERE id="%d"'%(4)) #하나일떄는 4괄호 안해도 됨

# delete3
c.execute('DELETE FROM users WHERE id=:id',{'id':3})

# delete All
print('table users deleted : ',c.execute('DELETE FROM users').rowcount)
conn.commit()

c.close()
conn.close()