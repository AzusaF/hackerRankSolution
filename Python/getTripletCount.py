#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTripletCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER d
#

def getTripletCount(arr, d):
    # Write your code here
    num_of_triplets = 0
    n = len(arr)
    
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if i < j < k:
                    current = [arr[i], arr[j], arr[k]]
                    if sum(current) % d == 0:
                        num_of_triplets += 1
    return num_of_triplets
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    d = int(input().strip())

    result = getTripletCount(arr, d)

    fptr.write(str(result) + '\n')

    fptr.close()
