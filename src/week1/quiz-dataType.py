# 1. 아래 문자열의 길이?
q1 = "alskjdfhalka;sjdh4kjhsfdakjh4323"

print(len(q1))
# 2. print로 출력
# apple;orange;banana;lemon
print('apple', 'orange', 'banana', 'lemon', sep=';')
# 3. 화면에 * 100개 표시
print('*' * 100)
# 4. 문자열 30을 각각 정수형, 실수형, 복소수형, 문자형변환
print(int('30'))
print(float('30'))
print(complex('30'))
print(str('30'))
# 5. "Niceman"문자열에서 "man"만 추출
print('Niceman'[4:])
# 문자열이 길때는?
q5_idx = 'Niceman'.index('man')
print('Niceman'[q5_idx:])
# 6. Strawberry" 거꾸로 출력
print("Strawberry"[::-1])
print("Strawberry"[::-1])

# 7.다음 문자열에서 '-'를 제거 후 출력 : 010-1234-1234
q7 = '010-1234-1234'
print(q7[0:3] + q7[4:8] + q7[9:13])
# 정규 표현식이 절실하다
import re

print(re.sub('[^0-9]', '', q7))

# 8

# 9. 'NiceMan' 소/대문자
print('NiceMan'.upper())
print('NiceMan'.lower())

# 11. apple 만 삭제
q11 = ["Banana", "Apple", "Orange"]
q11.remove("Apple")
print(q11)

# 12. 튜플을 리스트로 변환
q12 = (1, 2, 3, 4)
print(type(q12))
a12 = list(q12)
print(type(a12))

# 13. 딕셔너리 선언
a13 = {"성인": 100000,
       '청소년': 70000,
       '아동': 30000}
print(a13)

# 14. 위 딕셔너리에 항목 추가
a13['소아'] = 0
print(a13)

# 15. 딕셔너리의 키만 출력
print(a13.keys())
# 16. 딕셔너리의 value만 출력
print(a13.values())
# 17. 딕셔너리의 아이템만 출력
print(a13.items())

