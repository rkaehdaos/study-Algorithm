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
    def search(self,value):
        self.current_node=self.head
        while self.current_node:
            if self.current_node.value==value:
                return self.current_node
            elif value < self.current_node.value:
                self.current_node=self.current_node.left
            else:
                self.current_node=self.current_node.right
        return None

# 초기화
head = Node(3)
BST = TreeMgmt(head)
BST.insert(2)
BST.insert(4)
BST.insert(5)
BST.insert(1)

# 탐색
for i in range(1,6):
    print(BST.search(i).value)



