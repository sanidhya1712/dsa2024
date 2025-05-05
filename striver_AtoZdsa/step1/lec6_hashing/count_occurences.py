def countOccurence(n):
    a = {}
    high = 0
    low = float('inf')
    for i in n:
        if i in a:
            a[i]+=1
        else:
            a[i] = 1
    for i in a:
        if a[i]>high:
            high = a[i]
        if a[i]<low:
            low = a[i]
    print(a)
    print(high,low)
print(countOccurence([10,5,10,15,10,5]))