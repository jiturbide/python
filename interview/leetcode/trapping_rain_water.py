from collections import deque
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None or len(height) == 2:
            return 0

        idx1 = 0
        idx2 = 1
        water = 0
        while height[idx1] == 0 and idx1 < len(height) - 2:
            idx1 += 1
            idx2 += 1

        next_maximum = idx2
        
        while idx1 < len(height) - 2:
            if idx2 == len(height):
                if next_maximum < len(height):
                    container_height = min(height[idx1], height[next_maximum])
                    while idx1 < next_maximum:
                        idx1 += 1
                        current_water = container_height - height[idx1]
                        if current_water > 0:
                            water += current_water
                    idx2 = idx1 + 1
                    next_maximum = idx2
                else:
                    break
            elif height[idx2] >= height[idx1]:
                if idx1 + 1 == idx2:
                    idx1 += 1
                    idx2 += 1
                else:
                    container_height = min(height[idx1], height[idx2])
                    while idx1 < idx2:
                        idx1 += 1
                        current_water = container_height - height[idx1]
                        if current_water > 0:
                            water += current_water
                    idx2 += 1
                next_maximum = idx2
            else:
                idx2 += 1
                if idx2 < len(height) and height[idx2] >= height[next_maximum]:
                    next_maximum = idx2

        return water

if __name__ == '__main__':
    print("Start of the program")

    testCases = [
#        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
#        ([4,2,0,3,2,5], 9),
        ([4,2,3], 1)
    ]

    for nums, expected in testCases:
        result = Solution().trap(nums)
        if result == expected:
            print("Pass", nums, result)
        else:
            print("Fail", nums, result, expected)
