#!/bin/python3

import math
import os
import random
import re
import sys

def minimumSwaps(arr):
    swaps = 0

    for current_index, num in enumerate(arr):
        # check if value on current index is correct
        if arr[current_index] - 1 == current_index:
            continue

        # keep swapping and incrementing swaps variable until correct
        while arr[current_index] != current_index + 1:
            target_index = arr[current_index] - 1
            arr[target_index], arr[current_index] = arr[current_index], arr[target_index]
            swaps += 1

    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
