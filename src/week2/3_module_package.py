# 모듈, 패키지
# 왜 모듈 형태로 개발해서 패키지 형태로 배포하는가?

# Simple
# 파일 하나하나를 모듈이라고 하면 폴더를 패키지라고 할 수 있음
# # 모듈을 독립적인 기능을 가진 단위로 개발

# test_pkg 안의 모듈을 사용해보자
# 피보나치 클래스의 함수 사용해보기
from test_pkg.fibonacci import Fibonacci
Fibonacci.fib(300)