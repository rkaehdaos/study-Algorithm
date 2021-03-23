class Fibonacci:
    def __init__(self, title="fibonacci"):  # title을 사용하고 넘어온 값이 없으면 기본 값 사용
        self.title = title

    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a + b
        print()

    def fib2(n):
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)
            a, b = b, a + b
        return result
