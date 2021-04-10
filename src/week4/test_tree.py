# study tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeMgmt:
    def __init__(self, head):
        if head == type(Node):
            self.head = head
        else:
            raise TypeError('node타입이 아닙니다')
