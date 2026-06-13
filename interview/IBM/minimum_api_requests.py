def minimum_api_request(nums, k):
    if nums is None or len(nums) == 0 or k == 0:
        return 0

    max_pairs = 0

    for i in range(len(nums)):
        if nums[i] != -1:
            for j in range(len(nums)):
                if nums[j] != -1:
                    if (nums[i] + nums[j]) % k == 0:
                        nums[i] = -1
                        nums[j] = -1
                        max_pairs += 1
                        break

    return max_pairs


if __name__ == '__main__':
    print("Start of the program")

    testCases = [
        ([1,2,3,4,5,10,6], 5, 3),
        ([3,3,3,3,3,0], 3, 3),
        ([7,1,3,2,4,5,6], 8, 3)
    ]

    for nums, k, expected in testCases:
        result = minimum_api_request(nums, k)
        if result == expected:
            print("Pass", nums, k, result)
        else:
            print("Fail", nums, k, ", result: ", result, ", expected: ", expected)

'''
Challenge 3: Minimum API Requests
Problem

A cloud service receives requests represented by positive integers.

Two requests may be processed together if their sum is divisible by k.

Each request may belong to at most one pair.

Return the maximum number of valid pairs.

Example

requests = [1,2,3,4,5,10,6]
k = 5

Output

3

Possible pairs

(1,4)
(2,3)
(10,5)

Remaining

6

cannot be paired.

Constraints
1 <= n <= 200000
1 <= request[i] <= 10^9
2 <= k <= 10^5
Skills tested
Modular arithmetic
Hash tables
Greedy pairing
O(n) solution
'''