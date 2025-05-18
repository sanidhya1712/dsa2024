def largestArrayElement(arr):
    high = -1
    for i in arr:
        if i> high:
            high = i
    return high
print(largestArrayElement([8,10,5,7,9]))