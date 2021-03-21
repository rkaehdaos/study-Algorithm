# 반복문
# 기본 : while, for

v1 = 1
while v1 < 11:
    print('v1 is : ', v1)
    v1 += 1

for v2 in range(10):  # 0~9
    print('v2 is : ', v2)

for v3 in range(1, 10001):  # 1~10000
    print('v3 is : ', v3)

# 1~100합
# 효율성없는 예시
sum1 = 0
cnt1 = 1
while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1
print(sum1)
# 간단 예시 : sum은 리스트입력받아 전체 받음
# range는 리스트 를출력함
print(sum(range(1, 101)))

# 1부터 100까지 2개단위로 건너뛰면서?
print(sum(range(1, 101, 2)))

# 시퀀스 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 : range, reversed, enumerate, filter, map, zip


# 문자열
word = "dreamfactory"
for ch in word:
    print(ch)

# 리스트
names = ["Kim", "Park", "Cho", "Choi", "Yoo"]
for v in names:
    print('You are : ', v)
    for vv in v:
        print('\tspell:', vv)

# 딕셔너리
my_info = {
    "name": "Kim",
    "age": 33,
    "city": "Seoul"
}

# 기본값은 key
for key in my_info:
    print('key: ', key)
for value in my_info.values():
    print('value: ', value)
for k, v in my_info.items():
    print('item: ', k, v)

#대문자 소문자, 소문자 대문자
for n in 'NiceManTestString':
    if n.isupper():
        print(n.lower(),end='')
    else:
        print(n.upper(),end='')


print()
# break

# for else문
# 파이썬 독특한 부분
# break 없이 반복문이 정상적으로
# 수행된 경우 else 블럭 수행

## continue
for n in reversed('NiceManTestString'):
    print(n,end='')