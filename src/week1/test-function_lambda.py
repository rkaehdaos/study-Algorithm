# 함수 정의와 람다
# 하나의 기능을 하나의 함수로
# **파이썬은 함수 선언 위치가 중요**
# 함수 정의 방법
# def 함수명(파라미터):
#   code

# ex1
def hello(world):
    print("Hello", world)


hello('월드')


# ex2
def hello_return(world):
    v = "Hello " + str(world)
    return v


print(hello_return('월드2'))


# 다중 리턴
def func_milti_return(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    # 정수형 3개를 리턴
    return y1, y2, y3


val1, val2, val3 = func_milti_return(100)
print(val1, val2, val3)


# *args,
# 다양한 매개변수를 받을 수 있음
# 타입을 찍어보면 tuple -:> iterator가 가능하다는 부분
def args_func(*args):
    print(args)
    # iterator
    for t in args:
        print(t)
    # enumerate : 순서가 있는(리스트,튜플,문자열)을 인덱스값을
    # 포함한 enumerate 객체로 반환
    for i, v in enumerate(args):
        print(i, v)


args_func('kim')
args_func('kim', 'Park')


# * kwargs - 키워드 펑션
# * 하나일땐 튜플, ** 이면 딕셔너리
def kwargs_func(**kwargs):
    print(kwargs)


kwargs_func(name='James', age=23, address='Seoul')


# 혼합
# arg1, arg2는 필수, 나머지는 가변
def exam_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


exam_mul(10, 20)  # 가변없어도 출력은 가능, 빈 튜플과 딕셔너리 반환

exam_mul(10, 20, 'park', 'klim', age=23, weight=83)


# 중첩 함수(클로저)
# 고급 : 데코레이터
def nested_func(num):
    # 내부 함수 선언
    def func_in_func(num):
        print('>>>>>', num)

    print("in func")
    # 내부함수 호출
    func_in_func(num + 10000)


nested_func(10000)


# 힌트
# 명시적으로 입력값,출력값을 알려줄 수 있음

def func_hint(x: int) -> list:
    return [x, x * 10, x * 20]


print(func_hint(5))


# 람다
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리)할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화
# 증명

# 1)일반 함수
def mul_10(num: int) -> int:
    return num * 10


var_func1 = mul_10
print(type(var_func1))  # 클래스 function : 메모리 점유)
print(var_func1(10))

# 2) 람다식
lambda_mul_10 = lambda x: x * 1000
print('람다: ', lambda_mul_10(10))


# 3) 응용
def func_final(x, y, func):  # 함수도 매개변수
    print(x * y * func(10))


func_final(10, 10, lambda_mul_10) # 함수
func_final(10, 10, lambda x: x * 2222) #한번 사용 할거면 바로 익명함수처럼: 메모리절약

