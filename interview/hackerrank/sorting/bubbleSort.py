import math
import os
import random
import re
import sys

#
#
#

def sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) -i -1):
            if arr[j] > arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp
    return arr

if __name__ == '__main__':
    arr = [7, 1, 3, 2, 4, 5, 6]
    result = sort(arr)

    print('result', result)
    