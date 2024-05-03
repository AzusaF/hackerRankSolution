# Mini-Max Sum

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    max, min,sum = 0, 0, 0
    for i in range(len(arr)):
      sum += arr[i]
    for i in range(len(arr)):
      currentSum = sum - arr[i]
      if min == 0:
        min = currentSum
      elif min > currentSum:
        min = currentSum
      if max == 0:
        max = currentSum
      elif max < currentSum:
        max = currentSum
    print(min, max)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
