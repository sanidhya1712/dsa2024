from collections import deque


class Solution:
    def minSwaps(self, s: str) -> int:
        open = deque()
        unbalanced = 0
        for x in s:
          if x == '[':
            open.append(x)
          else:
            if open:
              open.pop()
            else:
              unbalanced = unbalanced+1
        return (unbalanced+1)//2        #this is like a formula, where either number of unbalanced or remaining balanced can be taken and divided by two
        
s = Solution()
print(s.minSwaps(']]]]][[[[['))