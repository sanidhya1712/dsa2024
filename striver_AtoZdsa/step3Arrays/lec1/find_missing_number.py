from os import *
from sys import *
from collections import *
from math import *

def findMissingNumber(arr):
    final = []
    for i in range(len(arr)):
        if arr[i] != i+1:
            return i+1
print(findMissingNumber([1,2,4,5]))