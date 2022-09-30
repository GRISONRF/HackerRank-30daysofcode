""" Given a square matrix, calculate the absolute difference between the sums of its diagonals. """

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
    
    left_right = 0
    right_left = 0

    for a in range(len(arr)):
        left_right += arr[a][a]
        right_left += arr[a][len(arr)-1-a] 


    return abs(left_right - right_left)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
