# 리스트 컴프리헨션 :리스트를 쉽게 만드는 기법
# 자동으로 append

# 일반적으로 1~100까지 리스트?
n1 = []
for n in range(1, 101):
    n1.append(n)
print(n1)

# 리스트 컴프리헨션을 쓰면
n2 = [x for x in range(1, 101)]  # 내부적으로 돌아감
print(n1 == n2)

# 예) 조건/루프 퀴즈에서 갑을병정에서 정빼는 거 컴프리헨션 쓰면?
n3 = ['갑', '을', '정', '병']
a3 = [x for x in n3 if x != '정']
print(a3)

# 예) 100까지 홀수 만 한 라인 리스트
a4 = [x for x in range(1, 101, 2)]
print(a4)
