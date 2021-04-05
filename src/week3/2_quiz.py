# q3
def hash_func(n):
    return abs((n % 10) - 5)


for i in range(1, 100):
    print(hash_func(i))
# 0~5 : 6개

# q4
import queue

a = queue.PriorityQueue()
a.put((10, '캠퍼스'))
a.put((1, '패스트'))
a.put((55, '완주반'))
a.put((11, '온라인'))
print(' '.join([a.get()[1], a.get()[1], a.get()[1], a.get()[1]]))
