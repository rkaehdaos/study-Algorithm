# datatype

v_str1 = "string"
v_boolean1 = True
v_boolean2 = False
v_float1 = 10.3
v_float2 = 10.
v_float3 = .7
v_int = 7

# 문자열은 ""으로
v_dict = {
    "name": "king",
    "age": 25
}

v_tuple = 3, 5, 4, 6, 7  # 튜플 : 기본 적으로 ,를 많이 사용
v_set = {7, 8, 9}  # set은 중괄호 사용
v_list = [7, 8, 9]  # list는 배열이라고 볼 수 있을 듯

## 데이터 타입 출력
print(type(v_dict))
print(type(v_set))
print(type(v_tuple))
print(type(v_int * v_float1))

v_bigint1 = 9999999999999999999999999999999999999999
v_bigint2 = 8888888888888888888888888888888888888888
print(v_bigint1 * v_bigint2)

# type cast

print(int(10.3))  # 정수형 변환
print(float(10))  # 실수형 변환
print(complex(3))  # 복소수 변환
print(complex(True))
print(complex(False))

print(int(True), int(False))  # boolean -> int
print(int('3'))  # String -> int

## 연산
'''
/ : 나누기
// :몫
% : 나머지
** : 지수
'''
## 증감
y = 100
y += 100
y /= 10

# 수치 연산 함수
# https://docs.python.org/ko/3/library/math.html
print(abs(-7))  # 절대값
n1, m1 = 10, 20  # 변수 동시 할당 : n1에 10, m1에 20
n2, m2 = divmod(100, 8) # 100/8의 몫은 n2, 나머지는 m2

import math
print(math.ceil(5.1)) # 주어진 값 이상의 가장 작은 정수
print(math.floor(3.874)) # 주어진 값 이하의 가장 큰 정수