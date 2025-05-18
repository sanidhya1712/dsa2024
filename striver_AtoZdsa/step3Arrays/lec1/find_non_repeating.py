from os import *
from sys import *
from collections import *
from math import *

def findingSingleNumber(arr):
    # Optimal approach - XOR all the elements:
    xorr = 0
    for num in arr:
        xorr ^= num
    return xorr
#     # Brute force approach - using dictionary to count occurrences:
#     # Time complexity: O(n)
#     # Space complexity: O(n)
#     # This approach is not optimal for large arrays
#     # but is included for educational purposes.
    '''dict = {}
    for i in range(len(arr)):
        if arr[i] in dict:
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1
    for i in dict:
        if dict[i] == 1:
            return i
    return -1'''
# Example usage
# arr = [4, 1, 2, 1, 2]
# print(findingSingleNumber(arr))
# Test case
# arr = [2, 2, 1]
# print(findingSingleNumber(arr))
# Test case
# arr = [1]
# print(findingSingleNumber(arr))
# Test case
arr = [1, 2, 1]
print(findingSingleNumber(arr))