class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.count = 0

'''To use this func, copy paste in singlyLinkedListPractice file.
if the original linked list is first -> second -> third -> ……….->thirdlast -> secondlast -> last, 
then the modified linked list would be first -> last -> second -> second_last -> ...'''
def modifyLL(head):
    n1 = head
    res = []
    res2 = []
    while n1:
      res.append(n1.value)
      n1 = n1.next
    for i in range(len(res)//2):
      res2.append(res[i])
      res2.append(res[len(res)-i-1])
    if len(res)%2!=0:
      res2.append(res[len(res)//2])
    print(res2)
    n2 = LinkedList()
    for i in res2:
      n3 = Node(i)
      if n2.head:
        n3.next = n2.head
        n2.head = n3
      else:
        n2.head = n3
    return n2