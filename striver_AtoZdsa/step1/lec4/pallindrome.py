# Mathematical with last remainder
def pallindrome(n):
    rev = 0
    orig = n
    while n>0:
        ld = n%10
        rev = rev*10 + ld
        n = n//10
    return rev == orig
 
print(pallindrome(1331))