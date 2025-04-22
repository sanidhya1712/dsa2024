from os import *
from sys import *
from collections import *
from math import *

# Brute force
'''The outer loop picks a starting element, the inner loop considers all elements (on right side of current start) as 
ending element. Whenever sum of elements between current start and end becomes greater than x, 
update the result if current length is smaller than the smallest length so far. '''
def minSubArrayLen(arr, target, n):
    ans = float('inf')
    for i in range(0,len(arr)-1):
        sum = 0
        for j in range(i, len(arr)-1):
            sum += arr[j]
            if sum> target:
                ans = min(ans, j-i+1)
                break
    if ans == float('inf'):
        return 0
    return ans

#Optimized soln
'''The idea is to use two pointer approach to maintain a sliding window, where we keep expanding the window by adding 
elements until the sum becomes greater than x, then we try to minimize this window by shrinking it from the start while 
maintaining the sum > x condition. This way, we explore all possible subarrays and keep track of the smallest valid length.'''
def minSubArrayLen2(arr, target, n):
    i, j = 0, 0
    sum = 0
    ans = float('inf')
    while j< len(arr):

        # Expand window until sum > x 
        # or end of array reached
        while j< len(arr) and sum<= target:
            sum+= arr[j]
            j+=1
        
        # If we reached end of array and sum 
        # still <= x, no valid subarray exists
        if j== len(arr) and sum<= target:
            break

        # Minimize window from start 
        # while maintaining sum > x
        while i <j and sum - arr[i]> target:
            sum -= arr[i]
            i+=1
        ans = min(ans, j-i)
        # Remove current start 
        # element and shift window
        sum-= arr[i]
        i+=1
    if ans == float('inf'):
        return 0
    return ans

print(minSubArrayLen2([1, 4, 45, 6, 10, 19], 51, 10))