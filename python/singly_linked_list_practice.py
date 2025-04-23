class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0
  def addToHead(self, value):
    node = Node(value)
    if not self.head:
      self.head = node
      self.tail = node
    else:
      node.next = self.head
      self.head = node
    self.count = self.count + 1

  def getList(self):
    node = self.head
    if self.count == 0:
      return("empty list")
    else:
      i = 1
      while i<=self.count:
        print(node.value)
        node = node.next
        i+=1
  def get(self, index):
   node = self.head
   if self.count == 0: return("empty list")
   if index >= self.count: return("Out of bound")
   i = 0
   while i < index:
    #  print(node.value)
     node = node.next
     i += 1
   return node
  def addAtTail(self,value):
   node = Node(value)
   if not self.tail:
     self.head = node
     self.tail = node
   else:
     self.tail.next = node
     self.tail = node
   self.count = self.count + 1
  def addAtIndex(self, value, index):
    node = Node(value)
    if index < 0 or index > self.count: return("Invalid Index")
    if index == self.count: self.addAtTail(value)
    if index == 0: self.addToHead(value)
    prev = self.get(index-1)
    node.next = prev.next
    prev.next = node
    self.count = self.count + 1
  def deleteAtIndex(self, index):
    if index < 0 or index >= self.count: return("Invalid Index")
    if index == 0:
      node = self.head
      self.head = node.next
      self.count-=1
      if self.count == 0:
        self.tail = None
      return node.value
    elif index == self.count-1:
      prev = self.get(index -1)
      self.tail = prev
      prev.next = None
      self.count-=1
      return prev.value
    prev = self.get(index-1)
    curr = prev.next
    prev.next = curr.next
    self.count-=1
    return curr.value
s = LinkedList()
# s.addToHead(8)
# s.addToHead(19)
# s.addToHead(11)
s.addAtTail(1)
s.addAtTail(2)
s.addAtTail(3)
s.addAtTail(4)
s.addAtTail(5)
# s.addAtIndex(16,2)
# print("Deleted- ",s.deleteAtIndex(6))
s.getList()
# s1 = modifyLL(s.head)
# s1.getList()
print("Single return - " ,s.head.value, s.tail.value, s.count)