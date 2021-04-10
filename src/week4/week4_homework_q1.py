# q1
'''
Min Heap 자료구조를 이용하면 최대값을 O(logN)의 시간복잡도로 찾을 수 있다.
Min Heap을 이용하면 우선순위 값이 낮은 자료를 먼저 출력하는 Priority Queue를 구현할 수 있다.
Min Heap을 이용한 Priority Queue는 아래와 같은 특징을 가진다.

Min Heap을 이용한 Priority Queue의 특징
- 자료를 입력하는 동작과 출력하는 동작 모두 O(logN)으로 이루어진다.
- 우선순위 값이 낮은 자료를 먼저 출력하되, 우선순위 값이 같은 자료끼리는 순서를 고려하지 않는다.
- 다음과 같은 Method들을 구현한다.
    is_empty(): Queue가 비어있으면 True, 비어있지 않으면 False를 출력한다.
    put():  Priority Queue에 자료를 입력한다.
            자료는 길이가 2인 Tuple로, (우선순위, 자료) 형태로 입력받는다.
    get():  Priority Queue에서 자료를 출력한다.
            출력한 데이터는 Priority Queue에서 삭제한다.
            더이상 출력할 데이터가 없는 경우 None을 출력한다.
    peek(): Priority Queue에서 자료를 출력한다.
            출력한 데이터는 Priority Queue에 그대로 유지한다.
            더이상 출력할 데이터가 없는 경우 None을 출력한다.
'''


class PriorityQueue:
    def __init__(self):
        pass

    def is_empty(self):
        pass

    def put(self, data):
        pass

    def get(self):
        pass

    def peek(self):
        pass


# Test code

pq = PriorityQueue()
pq.put((0, 'a'))
pq.put((5, 'b'))
pq.put((2, 'c'))
pq.put((1, 'd'))
pq.put((3, 'e'))
pq.put((4, 'f'))

print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
print(pq.get())
