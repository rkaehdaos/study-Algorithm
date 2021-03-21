# 조건, 반복문 퀴즈

# 1. if를 사용해서 가을의 과일 출력
q1 = {"봄": "딸기", "야름": "토마토", "가을": "사과"}
for k in q1.keys():
    if k == '가을':
        print(q1[k])
for k, v in q1.items():
    if k == '가을':
        print(v)

# 2. 사과가 포함되어있나
q2 = {"봄": "딸기", "야름": "토마토", "가을": ""}
for k, v in q2.items():
    if v == '사과':
        print('포함됨')
        break
else:
        print('포함안됨')

# 3.
# 4.
# 5.
# 6.
# 7. 1~100까지 홀수를 1 line으로
for n in range(1,101):
    if n%2==1:
        print(n,end=',')
# 8. 5글자 이상만 출력? 조건문에 len(n)으로 체크
# 9. 소문자만 출력: islower 출력
# 10.
