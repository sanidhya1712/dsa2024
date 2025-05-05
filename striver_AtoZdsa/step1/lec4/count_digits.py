def countDigits(n):
    # n = str(n)
    length = 0
    # return len(n)
    while (n != 0):
        length+=1
        n = n//10
    return length
        
print(countDigits(17))