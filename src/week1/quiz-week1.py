# q6 출력 퀴즈
a = ['파', '이', '썬', '썬', '썬', '썬', '즐', '즐', '즐', '거', '운']
last = None
for elem in a:
    if elem == last:
        continue
    print(elem, end="")
    last = elem

print()
# q7
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = lambda x: x ** 2
c = list()
for elem in a:
    c.append(b(elem))
print(c)

print()
# q8
data1 = tuple(range(10))
data2 = list(range(10, 20))
print(data1, data2)
result = list(data1)[:6] + data2[::2]
print(result)

# q9
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c=list(set(a).intersection(set(b)))
print(c)

# q10
a = [['패스트', '완주', '반'], '코딩', ['캠', '스', '퍼'], '+', '알고리즘']
res = a[0][0]+a[2][0]+a[2][-1]+a[2][1]+a[-2]+a[-1]
print(res)
