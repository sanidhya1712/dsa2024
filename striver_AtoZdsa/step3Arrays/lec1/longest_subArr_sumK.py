def longestSubArrWithsumK2(arr, k):
    # brute force
    sum = 0
    maxLength = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum == k:
                maxLength = max(maxLength, j - i + 1)
    return maxLength
# optimal approach
def longestSubArrWithsumK(arr, k):
    sum = 0
    maxLength = 0
    sumMap = {}
    for i in range(len(arr)):
        sum += arr[i]
        if sum == k:
            maxLength = max(maxLength, i + 1)
        if sum - k in sumMap:
            maxLength = max(maxLength, i - sumMap[sum - k])
        if sum not in sumMap:
            sumMap[sum] = i
    return maxLength
    
print(longestSubArrWithsumK([2,3,5,1,9], 10))