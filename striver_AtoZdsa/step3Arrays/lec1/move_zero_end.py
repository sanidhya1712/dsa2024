def moveZeroToEnd(arr):
    start = 0
    i=0
    while(i<len(arr)):
        if(arr[i]!=0):
            arr[start]= arr[i]
            start+=1
        i+=1
    while start< len(arr):
        arr[start]= 0
        start+=1
    return arr
# optimal approach
def moveZeroToEnd(arr):
    j = -1
    for i in range(len(arr)):
        if arr[i]== 0:
            j= i
            break

    if j == -1:
        return arr
    for i in range(j+1, len(arr)):
        if arr[i]!= 0:
            arr[j], arr[i]= arr[i], arr[j]
            j+=1
    return arr

print(moveZeroToEnd([1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]))