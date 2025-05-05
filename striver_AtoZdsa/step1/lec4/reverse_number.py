# String manipulation
def reverseNumber(n):
    n = str(n)
    flag = 0
    rev = ""
    for i in range(len(n)-1, -1, -1):
        print(n[i])
        if n[i]== '0' and flag == 0:
            print("skip")
        else:
            rev = rev + n[i]
    print(rev)
    return int(rev)

# Mathematical with last remainder
def reverseNumber2(n):
    rev = 0
    while n>0:
        ld = n%10
        rev = rev*10 + ld
        n = n//10
    return rev
 
print(reverseNumber2(17))