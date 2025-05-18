def linearSearch(arr, v):
    present = -1
    for i in range(len(arr)):
        if arr[i]== v:
            present = i
            return present
    return present
print(linearSearch([8,10,5,7,9], 5))