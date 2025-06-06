def max_subarr_sum(arr):
    max_sum = float('-inf')
    curr_sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            curr_sum+= arr[j]
            if max_sum < curr_sum:
                max_sum = curr_sum
        curr_sum = 0
    return max_sum
# optimal approach
#Kadane's algorithm- Don't carry negative sum since it only reduces the sum
def max_subarr_sum(arr):
    max_sum = float('-inf')
    curr_sum = 0
    start = 0
    ansStart, ansEnd = -1, -1
    for i in range(len(arr)):
        if curr_sum == 0:
            start = i
        curr_sum+= arr[i]
        if max_sum < curr_sum:
            max_sum = curr_sum
            ansStart = start
            ansEnd = i
        if curr_sum < 0:
            curr_sum = 0
    return max_sum, ansStart, ansEnd
print(max_subarr_sum([-2,1,-3,4,-1,2,1,-5,4]))