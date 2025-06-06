
def longestConsecutiveSubsequence(arr):
    n = len(arr)
    if n == 0:
        return 0
    arr.sort()
    seq = 1
    maxSeq = 1
    lastSmaller = arr[0]
    print(arr)
    for i in range(1,len(arr)):
        if lastSmaller== arr[i]-1:
            seq +=1
            lastSmaller = arr[i]
        elif arr[i]!= lastSmaller:
            seq = 1
            lastSmaller = arr[i]
        maxSeq = max(seq, maxSeq)
    return maxSeq
print(longestConsecutiveSubsequence([7, 1, 1, 5, 3, 6, 4]))