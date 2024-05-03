# Diagonal Difference
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    column = len(arr) -1
    firstDiagonals = 0
    secondDiagonals = 0
    for i in range(len(arr)):
      firstDiagonals += arr[i][i]
      secondDiagonals += arr[i][column]
      column -= 1
    return abs(firstDiagonals - secondDiagonals)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
