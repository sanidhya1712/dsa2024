import sys

# adding Folder_2 to the system path
sys.path.insert(0, '/Users/apple/Sanidhya/dsa2024/python')
from singly_linked_list_practice import LinkedList
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2) :
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        currl1 = l1.head
        currl2 = l2.head
        while currl1 != None or currl2 != None or carry != 0:
            l1Val = currl1.value if currl1 else 0
            l2Val = currl2.value if currl2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            currl1 = currl1.next if currl1 else None
            currl2 = currl2.next if currl2 else None
        return dummyHead.next

l1 = LinkedList()
l1.addAtTail(2)
l1.addAtTail(4)
l1.addAtTail(3)
l2 = LinkedList()
l2.addAtTail(5)
l2.addAtTail(6)
l2.addAtTail(7)
s = Solution()
l1.getList()
l2.getList()
print(s.addTwoNumbers(l1, l2).value)