class Solution:
    # Brute force
    def minLength(self, s: str) -> int:
        while 'AB' in s or 'CD' in s:
          if 'AB' in s:
            s= s.replace('AB', '')
          elif 'CD' in s:
            s= s.replace('CD', '')
        return len(s)
    # With stacks
    def minLength2(self, s: str) -> int:
        stack = []

        # Iterate over each character in the input string
        for current_char in s:
            # If the stack is empty, simply push the current character
            if not stack:
                stack.append(current_char)
                continue

            # Check for "AB" pattern, remove the pair by popping from the stack
            if current_char == "B" and stack[-1] == "A":
                stack.pop()
            # Check for "CD" pattern, remove the pair by popping from the stack
            elif current_char == "D" and stack[-1] == "C":
                stack.pop()
            # Otherwise, push the current character onto the stack
            else:
                stack.append(current_char)

        return len(stack)
        
s = Solution()
print(s.minLength2("BFCACDAB"))