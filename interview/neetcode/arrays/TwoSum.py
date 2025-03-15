from typing import List
# https://neetcode.io/problems/two-integer-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        part = {}
        print(len(nums))
        for i in range(len(nums)):
            restOfSum = target -nums[i]
            if restOfSum in part:
                if i < part[restOfSum]:
                    return [i, part[restOfSum]]
                else:
                    return [part[restOfSum], i]
            else:
                part[nums[i]] = i
        return []


if __name__ == '__main__':
   nums = [3,4,5,6]
   target = 7
   expected = [0,1]

   output = Solution().twoSum(nums, target)

   print('output:', output, 'expected:', expected)
