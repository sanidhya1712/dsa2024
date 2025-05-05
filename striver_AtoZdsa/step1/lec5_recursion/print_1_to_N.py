def print1ToN(i, n):
    if i>n: 
        return
    print(i)
    print1ToN(i+1, n)
print(print1ToN(1, 5))