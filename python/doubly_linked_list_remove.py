class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

def linkNodes(node1,node2):
    node1.next = node2
    node2.prev = node1

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, node):
        # write code here
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
 
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        node.next = None
        node.prev = None

    def insertBefore(self, nodePosition, nodeInsert):
        self.remove(nodeInsert)
        # nodeInsert.prev = nodePosition.prev.next
        # nodeInsert.next = nodePosition.prev
        nodeInsert.next = nodePosition
        nodeInsert.prev = nodePosition.prev
        if nodePosition == self.head:
            self.head = nodeInsert
        else:
            nodePosition.prev.next = nodeInsert
        nodePosition.prev = nodeInsert
    def print(self):
        if self.head:
            node = self.head
            while(node):
                print(node.val, " - >")
                node = node.next
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
linkNodes(one,two)
linkNodes(two, three)
linkNodes(three, four)
linkNodes(four, five)

s = DoublyLinkedList()
s.head = one
s.tail = five
# s.remove(three)
s.print()
s.insertBefore(three, six)
print(s)
s.print()