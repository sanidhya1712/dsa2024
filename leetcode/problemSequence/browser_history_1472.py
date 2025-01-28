class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

def linkNodes(node1,node2):
    node1.next = node2
    node2.prev = node1

class BrowserHistory:

    def __init__(self, homepage: str):
        node = Node(homepage)
        self.head = node
        self.tail = node
        self.curr = node

    def visit(self, url: str) -> None:
        if self.curr:
            node = Node(url)
            currNode = self.curr
            node.prev = currNode
            currNode.next = node
            self.curr = node
            self.tail = node

    def back(self, steps: int) -> str:
        i = 0
        currNode = self.curr
        while i< steps and self.curr.prev: 
            currNode = currNode.prev
            self.curr = currNode
            i+=1
        return currNode.val

    def forward(self, steps: int) -> str:
        i = 0
        currNode = self.curr
        while i< steps and self.curr.next:
            currNode = currNode.next
            self.curr = currNode
            i+=1
        return currNode.val

# Your BrowserHistory object will be instantiated and called as such:
browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com");       #You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     #You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      #You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   #You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   # You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                # You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     # You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                # You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
finalParam = browserHistory.back(7);                   # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
print(finalParam)