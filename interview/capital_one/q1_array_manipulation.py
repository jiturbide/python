from collections import deque
from typing import List

def array_manipulation(arr):
    solution = [0 for _ in range(len(arr))]

    previous = 0
    next = 0

    for i in range(len(arr)):
        if i == len(arr)-1:
            next = 0
        else:
            next = arr[i+1]
        solution[i] = previous + arr[i] + next
        previous = arr[i]

    return solution

if __name__ == '__main__':
    print("Start of the program")

    testCases = [
        ([4, 0, 1, -2, 3], [4, 5, -1, 2, 1])
    ]

    for nums, expected in testCases:
        result = array_manipulation(nums)
        if result == expected:
            print("Pass", nums,  result)
        else:
            print("Fail", nums,  result, expected)
