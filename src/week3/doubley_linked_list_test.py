class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.header = Node(data)
        self.tail = self.header

    def desc(self):
        if self.header == None:
            print('No HEader')
            return
        else:
            node = self.header
            while node:
                print(node.data)
                node = node.next

    def descReverse(self):
        if self.header == None:
            print('No HEader')
            return
        else:
            node = self.tail
            while node:
                print(node.data)
                node = node.prev

    def insert(self, data):
        if self.header == None:
            print('make header')
            self.header = Node(data)
            self.tail = self.header
        else:
            newNode = Node(data)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def insertBefore(self, data, location):
        if self.header == None:
            print('make header')
            self.header = Node(data)
            self.tail = self.header
        else:
            locationNode = self.searchNode(location)
            newNode = Node(data,locationNode.prev,locationNode)
            locationNode.prev.next=newNode
            locationNode.prev=newNode

    def searchNode(self, data):
        if self.header == None:
            return
        else:
            node = self.header
            while node:
                if node.data == data:
                    return node
                else:
                    node = node.next
            return

    def delete(self, data):
        if self.header == None:
            return
        elif self.header.data == data:
            print('헤더')
            temp = self.header
            self.header = self.header.next
            del temp
        elif self.tail.data == data:
            print('꼬리')
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
            del temp
        else:
            node = self.header
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = temp.next
                    temp.next.prev = node
                    del temp
                else:
                    node = node.next


dlink = NodeMgmt(0)
dlink.desc()
print('--------------------------------------------')
for data in range(1, 10):
    dlink.insert(data)
dlink.desc()
print('--------------------------------------------')
dlink.descReverse()
print('--------------------------------------------')

dlink.delete(7)
dlink.desc()
print('--------------------------------------------')
dlink.delete(0)
dlink.desc()
print('--------------------------------------------')
dlink.delete(9)
dlink.desc()
print('--------------------------------------------')
searchNode = dlink.searchNode(5)
print(searchNode.data)
print('--------------------------------------------')
dlink.insertBefore(100, 5)
dlink.desc()
