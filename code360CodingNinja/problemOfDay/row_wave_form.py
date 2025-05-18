from os import *
from sys import *
from collections import *
from math import *

def rowWaveForm(mat):
    final = []
    for i in range(len(mat)):
        if i %2 == 0:
            for j in range(len(mat[i])):
                final.append(mat[i][j])
        else:
            for j in range(len(mat[i])-1, -1, -1):
                final.append(mat[i][j])
    return final

print(rowWaveForm([
    [1, 4],
    [2, 4],
    [3,4]
]))