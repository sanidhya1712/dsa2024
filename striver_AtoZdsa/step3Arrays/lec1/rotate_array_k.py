def rotateArrayK(arr, k):
    # Reverse each row
    k = k % len(arr)
    arr.reverse()
    arr = arr[:k][::-1]+ arr[k:][::-1]
    print(arr)

print(rotateArrayK([1,2,3,4,5,6,7],2))