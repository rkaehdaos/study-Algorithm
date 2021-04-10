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

    # 검색
    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                print('찾음')
                return self.current_node
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        print('못찾음')
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
        print()

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
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched == False:
            print('지울 값이 없습니다')
            return False

        # leaf일 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None

        # 자식이 1개 일 때
        elif self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # 자식이 2
        elif self.current_node.left != None and self.current_node.right != None:
            # 삭제 노드가 부모의 left일 때
            if value < self.parent.value:
                # 1번 전략 아이템 찾기 : 우측 중 가장 작은 노드
                # 헤드 초기화 했던 것처럼 초기화
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                # 1번 자식의 우측에 자식이 있 때( 좌측엔 있을 수가 없음:가장 작은 값이므로)
                if self.change_node.right:
                    self.change_node_parent.left = self.change_node.right
                # 자식이 없으면 1번 전략 노드의 부모의 left를 끊는다
                else:
                    self.change_node_parent.left = None
                ## 세팅
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left

            # 삭제 노드가 부모의 right 일 때
            else:
                #### 공통 부분 발견
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                # 1번 자식의 우측에 자식이 있 때( 좌측엔 있을 수가 없음:가장 작은 값이므로)
                if self.change_node.right:
                    self.change_node_parent.left = self.change_node.right
                # 자식이 없으면 1번 전략 노드의 부모의 left를 끊는다
                else:
                    self.change_node_parent.left = None
                ## 세팅
                self.parent.right = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left

        # 1번 전략 의 자식이 없을 때
        # 1번 자식의 우측에 자식이 있 때( 좌측엔 있을 수가 없음:가장 작은 값이므로)
        return True


# 초기화
print('------------초기화------------')
BST = TreeMgmt(Node(50))
print('------------삽입------------')
BST_DATA = {25, 75, 13, 38, 62, 88, 6, 19, 81, 95, 3, 16, 22, 92, 98, 14, 17, 91, 93, 94, 44, 58, 66, 32, 99}
for i in BST_DATA:
    BST.insert(i)
print('------------순회------------')
BST.inorder()
print('------------탐색------------')
BST.search(19)
BST.search(100)

print('------------삭제------------')

print('------------삭제 leaf------------')
BST.inorder()
BST.delete(14)
BST.inorder()
BST.delete(91)
BST.inorder()

print('------------자식1------------')
BST.inorder()
print('-------부모의 우측 자식--------')
BST.delete(98) # 부모의 우측 자식
BST.inorder()
print('-------부모의 좌측 자식--------')

BST.delete(6) # 부모의 좌측 자식
BST.inorder()

print('------------자식2, 삭제노드가 부모의 left------------')
print('------------1번 전력의 자식이 없을떄------------')
BST.delete(62)
BST.inorder()
print('------------1번 전력의 우측 자식 존재------------')
BST.delete(13)
BST.inorder()

print('------------자식2, 삭제노드가 부모의 right------------')
print('------------1번 전력의 자식이 없을떄------------')
BST.delete(38)
BST.inorder()
print('------------1번 전력의 우측 자식 존재------------')
BST.delete(95)
BST.inorder()