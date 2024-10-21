class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.end = False
        
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