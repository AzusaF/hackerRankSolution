# Capitalize!
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # capitalize the name
    fullName = s.split(' ')
    for i in range(0, len(fullName)):
        fullName[i] = fullName[i].capitalize()
    capitalizedName = ' '.join(fullName)
    return capitalizedName

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
