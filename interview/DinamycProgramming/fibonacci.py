from collections import deque
from typing import List

def dp_fibonacci(num, storage):

    if num in storage:
        return storage[num]
    else:
        result = dp_fibonacci(num-1, storage) + dp_fibonacci(num-2, storage)
        storage[num] = result
        return result

def fibonacci(num):
    storage = {0:0, 1:1}
    return dp_fibonacci(num, storage)
    

if __name__ == '__main__':
    print("Start of the program")

    testCases = [
        (7, 13),
        (8, 21)
    ]

    for nums, expected in testCases:
        result = fibonacci(nums)
        if result == expected:
            print("Pass", nums, result)
        else:
            print("Fail", nums, result, expected)
