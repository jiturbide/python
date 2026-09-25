from collections import deque
from typing import List

def check_sum(num1, num2):
    sum_nums = num1 + num2
    i = 0
    result = False
    while 2**i <= sum_nums:
        if 2**i == sum_nums:
            result = True
            break
        i+= 1

    return result

def find_number_elements_to_sum(arr):
    matches = 0

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if check_sum(arr[i], arr[j]):
                matches += 1

    return matches

if __name__ == '__main__':
    print("*** Start of the program")

    testCases = [
        ([1, -1, 2, 3], 5),
        ([-2, -1, 0, 1, 2], 5),
        ([2], 1)
    ]

    for nums, expected in testCases:
        result = find_number_elements_to_sum(nums)
        if result == expected:
            print("Pass", nums, result)
        else:
            print("Fail", nums, result, expected)

    print("*** End of the program")
