# 기초 복습

# 파이썬의 철학이란?
import this

import sys

# 기본 인코딩 : UTF-8
# 2.x때는 유니코드 사용 -> 인코딩 디코딩이 필요했음
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 변수 선언
whoami = "me"
print(whoami)

한글변수 = "한글"
print(한글변수)

# 조건문
if (whoami == "me"):
    print('ok') # 파이썬은 indent도 문법

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d =' % (i, j), i * j)

# 함수 선언
def 인사(): # 한글 가능
    print('안녕하세요')

# 함수실행
인사()

## 한글은 그냥 된다는 거지 쓰라는 건 아님

# 클래스
class Cookie:
    pass

# 객체 선언
cookie =Cookie()
print(id(cookie))
print(dir(cookie))

## simple json test
import simplejson as json

test_dict = {'3': 89, '2': 90, '4': 100, '1': 99, '5': 80}
print(test_dict)
print(json.dumps(test_dict))
print(json.dumps(test_dict, sort_keys=True))
print(json.dumps(test_dict, sort_keys=True, indent=4 * ' '))
