class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:  # Node 관리
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    ## 삭제 함수 만들어보기
    ## 1. head
    ## 2. 중간
    ## 3. 끝
    def delete(self, data):
        if self.head=='':
            print('node가 없음')
            return

        if self.head.data==data:
            temp=self.head
            self.head=self.head.next
            del temp ## 객체 삭제
        else:
            node=self.head
            while node.next:
                if node.next.data==data:
                    temp=node.next
                    node.next=node.next.next
                    del temp
                else:
                    node=node.next
        return


# Test
linkedlist1 = NodeMgmt(0)
linkedlist1.desc()
for data in range(1, 10):
    linkedlist1.add(data)  # 맨끝에 추가
linkedlist1.desc()  # 데이터 순회하며 출력
print('--------------------------------------------')
linkedlist1.delete(5)
linkedlist1.desc()