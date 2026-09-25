from collections import deque
from typing import List

class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        if n != 0:
            return self.climb_and_compute(n, 0)

    def climb_and_compute(self, target, current) -> int:
        if current == target:
            return 1
        elif current > target:
            return 0
        else:
            if current + 1 not in self.memo:
                self.memo[current+1] = self.climb_and_compute(target, current+1)

            if current + 2 not in self.memo:
                self.memo[current+2] = self.climb_and_compute(target, current+2)
            
            self.memo[current] = self.memo[current+1] + self.memo[current+2]

            return self.memo[current]

if __name__ == '__main__':
    print("Start of the program")

    testCases = [
        (3, 3),
        (4, 5),
        (5, 8),
        (100, 573147844013817084101)
    ]

    for nums, expected in testCases:
        result = Solution().climbStairs(nums)
        if result == expected:
            print("Pass", nums, result)
        else:
            print("Fail", nums, result, expected)
