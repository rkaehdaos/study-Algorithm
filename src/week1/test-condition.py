# 조건문

# boolean type
print(type(True))
print(type(False))

# True : 내용있는 문자열, 튜플 , 리스트 , 딕셔너리 1 등
# false : 비어있는 문자열, 튜플, 리스트, 딕셔너리 0 등


# ex1
if True:
    print('True')

# ex2
if False:
    print('출력되지 않음')

# ex3
if False:
    print('출력되지 않음')
else:
    print('출력됨')

# 관계 연산자
# >, >=, <, <=, ==, !=

# 논리 연산자
# and or not


# 우선순위
# 산술 > 관계 > 논리
print('ex1: ', 5 + 10 > 0 and not 7 + 3 == 10)  # True and False => False

## 다중 조건
num = 82
if num >= 90:
    print('A')
elif num >= 80:
    print('B')
else:
    print('c')

## 중첩 조건 : if 안의 if