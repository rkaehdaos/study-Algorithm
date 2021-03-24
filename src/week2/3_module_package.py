# 모듈, 패키지
# 왜 모듈 형태로 개발해서 패키지 형태로 배포하는가?

# Simple
# 파일 하나하나를 모듈이라고 하면 폴더를 패키지라고 할 수 있음
# # 모듈을 독립적인 기능을 가진 단위로 개발

# test_pkg 안의 모듈을 사용해보자
# 사용 1 :  클래스의 함수 사용해보기
from test_pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print('test1: ', Fibonacci.fib2(300))
print('test1: ', Fibonacci().title)  # instance화를 해야 __init이 실행되므로

## 사용 2(클래스) : 메모리를 많이 사용하므로 권장하는 방법 아님
# from test_pkg.fibonacci import * #필요하지 않은 것도 로딩되므로
# Fibonacci.fib(300)

# 사용 3 : alias
from test_pkg.fibonacci import Fibonacci as fb

fb.fib(300)

# 사용 4: 함수
# calculation.py :  클래스 없이 함수만 존재
# 해당 파일의 모든 함수
import test_pkg.calculations as cal

print("ex4:", cal.add(10, 100))
print("ex4:", cal.mul(10, 100))

# 사용 5:
# from 절을 하면 하나만 가져올 수 있음
from test_pkg.calculations import div as d
print('ex5: ', int(d(100, 10)))

# 사용 6 , 연습삼아
import test_pkg.prints as p
p.prt1()
p.prt2()

# buildins : 파이썬 기본 제공 함수
import builtins # 명시적 임포트 필요없이 가능
print(dir(builtins)) # 기본 함수들 확인 가능