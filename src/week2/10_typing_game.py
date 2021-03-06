# 타이핑 게임 제작

import random
import time
import datetime
import winsound
import sqlite3

## db conn and auto commit
conn = sqlite3.connect('./resource/records.db', isolation_level=None)
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS records(\
    id INTEGER PRIMARY KEY AUTOINCREMENT,\
    cor_cnt INTEGER,\
    record text,\
    regdate text)')

words = []  # 영어단어 리스트로 1000개 로딩

n = 1  # 게임 시도 횟수
correct_count = 0  # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())
print(words)  # 단어 확인

a = input('Ready? Press Enter Key~')
print(a)  # 무조건 문자형으로 받음
start = time.time()
print('-----')
while n <= 5:  # 1~5
    random.shuffle(words)  # 섞어줌
    q = random.choice(words)
    print()
    print('*Question # {}'.format(n))
    print(q)  # 문제 출력

    x = input()  # 사용자 입력
    print()
    a1 = str(q).strip()
    a2 = str(x).strip()
    print('temp: ', a1, a2)
    if a1 == a2:
        print('Pass!!')
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        correct_count += 1
    else:
        print('Wrong!!')
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)

    n += 1
end = time.time()
et = end - start
# 기록 db

cursor.execute('INSERT INTO records(cor_cnt,record,regdate) VALUES (?,?,?)',
               (correct_count, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

print('총 시간: ', format(et, ".3f"))
print('맞춘 갯수 : %d/5' % correct_count)
if correct_count >= 3:
    print('합격!')
else:
    print('불합격')

cursor.close()
conn.close()
# 시작 시점
if __name__ == '__main__':
    pass
