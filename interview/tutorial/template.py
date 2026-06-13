from collections import deque


def fun(arr):
    return arr

if __name__ == '__main__':
    print("Start of the program")

    testCases = [
        ([7, 1, 3, 2, 4, 5, 6], 0, 0)
    ]

    for nums, k, expected in testCases:
        result = fun(nums)
        if result == expected:
            print("Pass", nums, k, result)
        else:
            print("Fail", nums, k, result, expected)
