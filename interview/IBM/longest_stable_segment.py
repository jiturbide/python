def longestStableSegment(nums, k):

    if nums is None or len(nums) <= 1: return 0

    lst_sub = []

    idxs = 0
    idxe = 1
    difference = max(nums[0],nums[1]) - min(nums[0], nums[1])
    lst_sub.append(nums[0])
    max_array = 1

    while idxe < len(nums):
        lst_sub.append(nums[idxe])
        difference = max(lst_sub) - min(lst_sub)
        while difference > k:
            idxs += 1
            lst_sub.pop(0)
            difference = max(lst_sub) - min(lst_sub)
        else: # difference <= k
            current_max_array = len(lst_sub)
            max_array = max(max_array, current_max_array)

        idxe += 1

    return max_array



if __name__ == '__main__':
    print("Longest Stable Segment")


    testCases = [
        ([8, 2, 4, 7], 4, 2),
        ([10,1,2,4,7,2], 5, 4),
        ([14,15,16,19,17,34,32,32], 4, 4)
    ]

    for nums, k, expected in testCases:
        result = longestStableSegment(nums, k)
        if result == expected:
            print("Pass", nums, k, result)
        else:
            print("Fail", nums, k, result, expected)



'''
Challenge 1: Longest Stable Segment
Problem

Given an array of integers, find the length of the longest contiguous subarray where the difference between the maximum and minimum element is at most k.

Example:

nums = [8, 2, 4, 7]
k = 4

Output:
2

Explanation:

[2,4] -> max=4 min=2 difference=2
[4,7] -> max=7 min=4 difference=3

Longest length = 2

Another example:

nums = [10,1,2,4,7,2]
k = 5

Output:
4

because

[2,4,7,2]

has

max = 7
min = 2
difference = 5
Constraints
1 <= n <= 100000
1 <= nums[i] <= 10^9
0 <= k <= 10^9
'''


