def checkPallindrome(n, start, end):
    if start>=end: 
        return True
    if n[start] != n[end]:
        return False
    return checkPallindrome(n, start+1, end-1)
print(checkPallindrome("abbcbba", 0, 6))