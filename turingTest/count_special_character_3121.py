class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char, upper = {}, {}
        count = 0
        for i in range(len(word)):
            if word[i].islower():
                char[word[i]]= i
            else:
                if not (word[i] in upper):
                    upper[word[i]]= i
        for x, y in upper.items():
            c = x.lower()
            if c in char and char[c]< y:
                count= count+1
        return count
s= Solution()
print(s.numberOfSpecialChars("cCceDC"))