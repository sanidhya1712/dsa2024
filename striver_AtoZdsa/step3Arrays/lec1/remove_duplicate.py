def removeDuplicate(arr):
    i = 1
    for j in range(1,len(arr)):
        if arr[j]!= arr[i-1]:
            arr[i] = arr[j]
            i+=1
    print(i) 
    return arr[0:i]
print(removeDuplicate([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))