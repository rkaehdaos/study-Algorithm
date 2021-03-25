# 파이썬 예외처리

# 예외 종류
# 문접적으로 에러가 없어도 런타임 에러처리도 중요
# linter : 코드 스타일,  문법 체크, (에디터라면 이것도 잘 케어해야함)

# SyntaxError : 잘못된 문법


#
# print('ffff)

# 콜론 빼먹음
# if true
#     pass


# 참조 변수 없음
# print(Novariable)

# ZeroDivision Error : 런타임 에러
# print(10/0)

# IndexError  : 인덱스 범위 오버
# x=[10,20,30]
# print(x[3])

# Key Error : dict에서 많이 발생
dic = {'name': 'kim'}
# 키가 없을때 에러 발생
# print(dic['hobby'])
# get을 사용하면 런타임 에러를 피할 수 있음
print(dic.get('hobby'))

# 어트리뷰트 에러 : 모듈, 클래스에 있는 잘못된 속성 사용시 예외
import time

print(time.time())  # 있는 함수
# print(time.month()) # 없는 함수

# Value error : 참조 값이 없을떄
x = [1, 5, 9]
# x.remove(10) # 해당 인덱스 없음
# x.index(10) # 해당 인덱스 없음

# fileNotFouundError
# f=open('nosuch.file.txt',r)

# type error
x = [1, 2]
y = (3, 4)
# print(x+y)
# 캐스팅 필요함


# 가이드
# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 런타임 예외 발생시 예외처리 코딩 권장

'''
자바 try-catch처럼 try except가 있음
else : 에러가 발생하지 않았을 경우
finally : 항싱 실행
'''
# ex1
# 계층적으로 생각할 것
# except 순서가 중요 : 모든 exception 다 캐치 하므로

name = ['kim', 'park', 'cho', 'choi']
try:
    # 핵심 부분
    z = 'a'
    x = name.index(z)
    print('{} found it in {}'.format(z, x + 1))
except IndexError as ie:
    print('index error')
except ValueError as ve:
    print('not found it!')
    print('ve:', ve)
except:
    print('other error catched')
else:
    print('Pass~!')
finally:
    print('finally ok')

# 예외처리는 아니지만 무조건 수행되는 패턴
try:
    print('try')
finally:
    print('fin')

# 예외 직접 일으키기 : raise
try:
    a='nn'
    if a=='kim':
        print('ok')
    else:
        raise ValueError
except ValueError as ex:
    print('문제발생', ex)

