# print : 가장 기본적인 출력 함수
# 작은 따옴, 큰 따옴 다 가능
print('test1')
print("test2")
print("""test2""")
print('''test4''')

print()  # 줄바꿈

## separator 옵션 : 여러 값 join처럼
print('T', 'E', 'S', 'T')
print('T', 'E', 'S', 'T', sep='')
print('2021', '03', '15', sep='-')

## end 옵션 사용 :
print('line1', end='') # 줄바꿈이 없어짐
print('line2', end='')