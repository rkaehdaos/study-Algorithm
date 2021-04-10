# study tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeMgmt:
    def __init__(self, head):
        if isinstance(head, Node):
            self.head = head
        else:
            raise TypeError('node타입이 아닙니다')

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
        print('end')

    # 검색
    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return self.current_node
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return None

    # 순회
    def inorder(self):
        def recursion(node):
            if node.left:
                recursion(node.left)
            print(node.value, end=' ')
            if node.right:
                recursion(node.right)

        recursion(self.head)

    # 삭제
    def delete(self, value):
        # leaf 노드 :삭제 노드의  부모가 해당 노드를 가르키는 곳에 None
        # 자식이 1 : 삭제 노드의  부모가 자식을 가르키도록
        # 자식이 2 : 전략 2개중 하나를 채택 해야함, 여기서는 1번
        # 1 - 삭제 노드 우측 자식중 가장 작은 값을 부모가 가르키도록 ---  1번 전략 채택
        # 2 - 삭제 노드 촤측 자식중 가장 큰 값을 부모가 가르키도록
        # 삭제 노드가 부모의 left일 때
        # 1번 전략 의 자식이 없을 때
        # 1번 자식의 우측에 자식이 있 때( 좌측엔 있을 수가 없음:가장 작은 값이므로)
        # 삭제 노드가 부모의 left일 때
        # 1번 전략 의 자식이 없을 때
        # 1번 자식의 우측에 자식이 있 때( 좌측엔 있을 수가 없음:가장 작은 값이므로)

        # 탐색
        searched = False
        # 처음에는 부모, 현재 노드 전부 head로 초기화
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.left:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched == False:
            return False

        # leaf일 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None


# 초기화
print('------------초기화------------')
head = Node(3)
BST = TreeMgmt(head)
print('------------삽입------------')
BST.insert(2)
BST.insert(4)
BST.insert(5)
BST.insert(1)
print('------------탐색------------')
for i in range(1, 6):
    print('%d번 째: ' % i, BST.search(i).value)

print('------------순회------------')
BST.inorder()