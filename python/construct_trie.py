class TrieNode:

    def __init__(self):
      
        # Array for child nodes of each node
        self.child = [None] * 26
        
        # for end of word
        self.word_end = False

# Method to insert a key into the Trie
def insert_key(root, key):

    # Initialize the curr pointer with the root node
    curr = root

    # Iterate across the length of the string
    for c in key:

        # Check if the node exists for the 
        # current character in the Trie
        index = ord(c) - ord('a')
        if curr.child[index] is None:

            # If node for current character does 
            # not exist then make a new node
            new_node = TrieNode()

            # Keep the reference for the newly
            # created node
            curr.child[index] = new_node

        # Move the curr pointer to the
        # newly created node
        curr = curr.child[index]

    # Mark the end of the word
    curr.word_end = True

# Method to search a key in the Trie
def search_key(root, key):

    # Initialize the curr pointer with the root node
    curr = root

    # Iterate across the length of the string
    for c in key:

        # Check if the node exists for the 
        # current character in the Trie
        index = ord(c) - ord('a')
        if curr.child[index] is None:
            return False

        # Move the curr pointer to the 
        # already existing node for the 
        # current character
        curr = curr.child[index]

    # Return true if the word exists 
    # and is marked as ending
    return curr.word_end

def isEmpty(root):
    for i in range(26):
        if root.children[i]:
            return False
    return True
 
def remove(root, key, depth = 0):
    if not root:
        return None
 
    if depth == len(key):
        if root.isEndOfWord:
            root.isEndOfWord = False
        if isEmpty(root):
            del root
            root = None
        return root
 
    index = ord(key[depth]) - ord('a')
    root.children[index] = remove(root.children[index], key, depth + 1)
 
    if isEmpty(root) and not root.isEndOfWord:
        del root
        root = None
    return root

# Create an example Trie
root = TrieNode()
arr = ["and", "ant", "do", "geek", "dad", "ball"]
for s in arr:
    insert_key(root, s)

# One by one search strings
search_keys = ["do", "gee", "bat"]
for s in search_keys:
    print(f"Key : {s}")
    if search_key(root, s):
        print("Present")
    else:
        print("Not Present")
