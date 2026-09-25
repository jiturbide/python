from collections import deque
from typing import List

def swap_one_zero(arr):
    if arr is None or len(arr) <= 2:
        return 0

    to_move = 0

    ones = 0
    ones_left = 0
    for idx in range(len(arr)):
        if arr[idx] == 1:
            ones += 1
            if idx < len(arr)//2:
                ones_left += 1

    zeros = len(arr) - ones
    zeros_left = len(arr)//2 - ones_left
    ones_right = ones - ones_left 

    if (ones >= zeros and ones_left >= ones_right) or (zeros>=ones and ones_left >= ones_right):
        to_move = 1

    idx1 = 0
    idx2 = 0

    total_moves = 0
    while idx1 < len(arr) and idx2 < len(arr):
        idx2 = idx1 + 1

        if arr[idx1] != to_move:
            curr_moves = 1
            # print("\n1 arr:", arr)
            while idx2 < len(arr) and arr[idx2] != to_move:
                curr_moves += 1
                idx2 += 1
            
            if idx2 < len(arr):
                tmp = arr[idx1]
                arr[idx1] = arr[idx2]
                arr[idx2] = tmp        
                # print("2 arr:", arr)

                total_moves += curr_moves
            else:
                break

        idx1 += 1


    return total_moves

if __name__ == '__main__':
    print("*** Start of the program")

    testCases = [
        ([1,0,1,1], 1),
        ([0,1,0,0], 1),
        ([1,0,1,1,0,0,0,0], 2),
        ([1,1,0,1,0,1,0,0], 3),
        ([1,1,1,0,0,0,0], 0)
    ]

    for nums, expected in testCases:
        result = swap_one_zero(nums)
        if result == expected:
            print("Pass", nums, result)
        else:
            print("Fail", nums, result, expected)

    print("*** End of the program")
