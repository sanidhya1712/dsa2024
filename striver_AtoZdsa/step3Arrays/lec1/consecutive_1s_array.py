from os import *
from sys import *
from collections import *
from math import *

def consecutiveOnes(arr):
    maxLength = 0
    currentLength = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            currentLength += 1
        else:
            currentLength = 0
        maxLength = max(maxLength, currentLength)
    return maxLength
print(consecutiveOnes([1, 1, 0, 1, 1, 1]))