from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None
        # self.tail = None
        self.size = 0
    def addAtHead(self, value):
        node = ListNode(value)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
        self.size+=1
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:        # My solution, failed
        if self.head:
            currNode = self.head
            while currNode:
                nextNode = currNode.next
                currNode.next = nextNode.next
                nextNode.next = currNode
                if currNode == self.head:
                    self.head = nextNode
                currNode= currNode.next
    # iterative solution
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:        # Leetcode solution
        if not head or head.next is None:
            return head
        # swap two aadjacent pair of nodes
        curr = head
        head = head.next # the issue was that the nxt node was referencing the full list but head is still
        # pointing to the old curr so ensure u update the head to point to the nxt node
        prev = None
        while curr and curr.next:
            nxt = curr.next
            if curr.next:
                foll = curr.next.next
            nxt.next = curr # set the next node to point to the current node
            # set the current node to point to the nxt.nxt node
            curr.next = foll
            if prev is not None:
                prev.next = nxt
            prev = curr
            curr = curr.next
        return head
s = Solution()
s.addAtHead(4)
s.addAtHead(3)
s.addAtHead(2)
s.addAtHead(1)
s.swapPairs(s.head)
print(s)