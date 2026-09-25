from collections import deque
from typing import List

class Solution:
    def search_brute_force(self, nums: list[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return -1

    def search(self, nums: list[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1

        start_idx = 0
        end_idx = len(nums) - 1
        middle_idx = start_idx +((end_idx - start_idx) // 2)

        while middle_idx <= end_idx:
            print (f"Iteration: nums[{start_idx}]={nums[start_idx]}, nums[{middle_idx}]={nums[middle_idx]} nums[{end_idx}]={nums[end_idx]}")
            if start_idx == middle_idx:
                if nums[start_idx] == target:
                    return start_idx
                else:
                    return -1
            # elif middle_idx < end_idx and middle_idx+1 == end_idx:
            #     if nums[end_idx] == target:
            #         return end_idx
            #     else:
            #         return -1

            if nums[start_idx] <= nums[middle_idx] and (nums[start_idx] <= target and target <= nums[middle_idx]):
                end_idx = middle_idx

            elif nums[middle_idx+1] <= nums[end_idx] and (nums[middle_idx+1] <= target and target <= nums[end_idx]):
                start_idx = middle_idx + 1

            elif nums[start_idx] > nums[middle_idx]:
                end_idx = middle_idx

            else: #nums[middle_idx + 1] > nums[end_idx]
                start_idx = middle_idx + 1

            middle_idx = start_idx +((end_idx - start_idx) // 2)


        return -1

if __name__ == '__main__':
    print("*** Start of the program")

    testCases = [
       ([4,5,6,7,0,1,2], 0, 4),
       ([4,5,6,7,0,1,2], 3, -1),
        ([1], 1, 0)
    ]

    for nums, k, expected in testCases:
        result = Solution().search(nums, k)
        if result == expected:
            print("Pass", nums, k, result)
        else:
            print("Fail", nums, k, result, expected)

    print("*** End of the program")
