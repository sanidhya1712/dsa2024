def fibonacci(n):
    if n==0: 
        print(0)
        return 0
    if n == 1:
        print(1)
        return 1
    last = fibonacci(n-1)
    secondLast = fibonacci(n-2)
    print(last+ secondLast)
    return last+ secondLast
print(fibonacci(5))