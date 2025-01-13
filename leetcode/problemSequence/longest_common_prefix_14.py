# Trie Soln
class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.end = False
        self.linkCount = 0
        
def insertWord(root, word):
    curr = root
    for x in word:
        c = ord(x) - ord('a')
        if curr.child[c] is None:
            newNode = TrieNode()
            curr.child[c] = newNode
        curr = curr.child[c]
    curr.end = True

def searchWord(root, word):
    curr = root
    for x in word:
        c = ord(x) - ord('a')
        if curr.child[c] is None:
            return False
        curr = curr.child[c]
        
    return curr.end

def commonPrefix(root, word):
    curr = root
    for x in word:
        c = ord(x) - ord('a')
        if curr.child[c] is None:
            return False
        curr = curr.child[c]
        
    return curr.end
'''
root = TrieNode()
arr = ["and", "ant", "do", "geek", "dad", "ball"]
for s in arr:
    insertWord(root, s)

# One by one search strings
search_keys = ["do", "gee", "ball"]
for s in search_keys:
    print(f"Key : {s}")
    if searchWord(root, s):
        print("Present")
    else:
        print("Not Present")
'''

#Binary search soln
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        minLen = min(len(x) for x in strs)
        low, high = 1, minLen
        while low <= high:
            middle = (low + high) // 2
            if self.isCommonPrefix(strs, middle):
                low = middle + 1
                print("low - ", low)
            else:
                high = middle - 1
                print("high - ", high)
        return strs[0][: (low + high) // 2]

    def isCommonPrefix(self, strs, l):
        str1 = strs[0][:l]
        print(l, strs, str1)
        for i in range(1, len(strs)):
            if not strs[i].startswith()(str1):
                return False
        return True

s = Solution()

print(s.longestCommonPrefix(["leets","leetcode","leetc"]))