def reverseArray(n, start, end):
    if start>=end: 
        return n
    n[start], n[end] = n[end], n[start]
    print(n)
    return reverseArray(n, start+1, end-1)
print(reverseArray([1,2,3,4,5], 0, 4))