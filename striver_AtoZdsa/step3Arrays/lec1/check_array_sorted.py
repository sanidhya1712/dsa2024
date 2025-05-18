def checkArraySorted(arr):
    flag = True
    for i in range(0,len(arr)-1):
        if arr[i]> arr[i+1]:
            flag = False
            break
    return flag
print(checkArraySorted([2,4,5,6,7,8,9]))