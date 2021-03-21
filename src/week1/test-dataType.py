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
n2, m2 = divmod(100, 8)  # 100/8의 몫은 n2, 나머지는 m2

import math

print(math.ceil(5.1))  # 주어진 값 이상의 가장 작은 정수
print(math.floor(3.874))  # 주어진 값 이하의 가장 큰 정수

print('*********************')
# 자료구조 사용 이유: 효율성
# 변경등에 취약 : 생상성 저하

# List
# 순서O, 중복O , 수정O, 삭제O
# dictionary와 함께 가장 많이 사용하는 자료 구조

# 선언 5가지
list_a = []
list_b = list()
list_c = [1, 2, 3, 4]
list_d = [10, 20, 'pen', 'banana', '귤']  # 데이터 타입이 달라도 담을 수 있음
list_e = [30, 40, ['pen', 'eraser']]

# 인덱싱
print(list_d[2])
print(list_d[-2])
print(list_d[0])
print(list_d[0] + list_d[1])
print(list_e[2])
print(list_e[2][1])

# 슬라이싱
print(list_d[0:3])
print(list_e[2][0:3])

# 연산
print(list_c + list_d)
print(list_c * 3)  # 3번 반복
print('I want to eat ' + str(list_d[3]))

# 리스트 수정
print(list_c)
list_c[0] = 77
print(list_c)
list_c[1:2] = [888, 999]  # 슬라이싱인 경우 하나의 원소씩
print(list_c)
list_c[1] = [111, 222, 333]  # 인덱스를 자체로 넣으면 nested 가 됨
print(list_c)

# 리스트 삭제
del list_c[1]
print(list_c)
del list_c[-1]
print(list_c)

print('***************************')

# 리스트 함수
print(list_c)
list_c.append(10)  # 끝에 추가
print(list_c)
list_c.insert(2, 13)  # 특정인덱스에 삽입
print(list_c)
list_c.sort()  # sort
print(list_c)
list_c.reverse()  # reverse
print(list_c)
list_c.remove(999)  # 해당 값을 지우는 거 , del처럼 인덱스를 지우는게 아님을 주의
print(list_c)
print(list_c.pop())  # LIFO #스택에서 꺼내는 것처럼
print(list_c)

# append와  extend의 차이
print('***********************')
print('append와  extend의 차이')
list_c.append([1, 2, 3, 4, 5])  # nested로 들어간다
print(list_c)
del list_c[3]
print(list_c)
list_c.extend([1, 2, 3, 4, 5])  # 붙이기처럼 확장됨
print(list_c)

# 삭제 3가지 정리 : del, remove, pop(이건 overflow주의)

print('***********************')
# Tuple
# 수정 O , 중복 O
# 수정X , 삭제 X :extend, append, del등은 없음
# 선언
tuple_a = ()
tuple_b = (1,)
tuple_c = (1, 2, 3, 4)
print(type(tuple_c))
tuple_d = (10, 100, ('a', 'b', 'c'))

# indexing
print(tuple_c[2])
print(tuple_d[2])
print(tuple_d[2][2])

# slice
print(tuple_d[2:])  # 출력이 ,로 찍혀있는것은 규칙
print(tuple_c[:])
print(tuple_b[:])
print(tuple_a[:])

print(tuple_d[2:] * 3)

# 튜플 함수
print(3 in tuple_c)
print(tuple_c.index(4))  # 특정값이 있는 인덱스
print(tuple_c.count(1))

print('***********************')
############


# 딕셔너리(Dict)
# JSON과 비슷한 모습
# 순서 없음, 중복X, 수정 O, 삭제O
# Key, Value(모든 타입 가능)

# 선언
dict_a = {'name': 'kim',
          'phone': '010-1111-1111',
          'birth': '870214'}

dict_b = {0: 'hello', 1: 'hi', 2: 'bye'}
dict_c = {'arr': [1, 2, 3, 4, 5]}

# 출력
print(type(dict_a))
print(dict_a)
print(dict_b)

# dict의 특정 키 밸류 조회 : 인덱싱과 get방법
print(dict_a['name'])
# print(dict_a['name1']) # 에러남

print(dict_a.get('name'))
print(dict_a.get('name1'))  # 에러없이 None으로 출력, 안전하게 get가능

print(dict_c)
print(dict_c['arr'])
print(dict_c['arr'][1:3])

# 추가
dict_a['address'] = 'Seoul'
dict_a['rank'] = [1, 2, 3, 4, 5]
dict_a['rank2'] = (1, 2, 3, 4, 5,)

print(dict_a)

# keys, values, item
# item : key+value 한쌍
print(dict_a.keys())  # key만 리스트 형태로 가져온다, 인덱스 접근 안됨
print(type(dict_a.keys()))  # 리스트 형이 아닌 dict_keys타입 확인
print(list(dict_a.keys())[2])  # 형변환을 하면 인덱싱이 가능

print(dict_a.values())
print(type(dict_a.values()))  # 역시 형변환이 필요함

print(dict_a.items())
print(list(dict_a.items()))  # 리스트 안에 튜플 형태로 반환

# 특정 키가 있는지 확인
print(2 in dict_b)
print('name' in dict_a)

print('******************')

# 집합(Set)
# 실무 케라스나 딥러닝등에 많이 쓰임
# 순서 X, 중복  X
# 선언
set_a = set()
set_b = set([1, 2, 3, 4, 5])
set_c = set([1, 4, 5, 6, 6])
print(type(set_a))
print(set_b)
print(set_c)  ## 중복 안되는 거 확인

# set은 보통 변환해서 많이 사용한다
tuple_b = tuple(set_b)
print(tuple_b)

# 교집합
print(set_b.intersection(set_c))
print(set_b & set_c)

# 합집합 : 중복은 제거 됨
print(set_b.union(set_c))
print(set_b | set_c)

# 차집합
print(set_b-set_c)
print(set_b.difference(set_c))

## 추가 삭제
print(set_a)
set_a.add(18)
print(set_a)
set_a.add(19)
print(set_a)
set_a.add(20)
print(set_a)
set_a.remove(18)
print(set_a)
set_a.remove(19)
print(set_a)
