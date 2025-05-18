def secondHighestElement(arr):
    high = float('-inf')
    second = float('-inf')
    for i in arr:
        if i> high:
            second = high
            high = i
        elif i> second and i<=high:
            second = i
        print(high,second)
    return high, second
print(secondHighestElement([8,10,5,7,9]))