from collections import deque
from typing import List

def largestRectangle(h):
    # Write your code here
    if h is None or len(h) == 0:
        return 0

    idx1 = 0
    idx2 = len(h) - 1
    
    while h[idx1] <= 0:
        idx1 += 1
        
    while h[idx2] <= 0:
        idx2 -= 1
    
    max_area = min(h[idx1], h[idx2]) * (idx2-idx1+1)
    
    while idx1 < idx2:
        curr_max_area = min(h[idx1], h[idx2]) * (idx2-idx1+1)
        if curr_max_area > max_area:
            max_area = curr_max_area
        
        if h[idx1] <= h[idx2]:
            idx1 += 1
        else:
            idx2 -= 1
              
    return max_area

if __name__ == '__main__':
    print("*** Start of the program")

    testCases = [
        ([8979, 4570, 6436, 5083, 7780, 3269, 5400, 7579, 2324, 2116], 26152),
        ([11, 11, 11, 10, 10], 50),
        ([1, 2, 3, 4, 5], 9)
    ]

    for nums, expected in testCases:
        result = largestRectangle(nums)
        if result == expected:
            print("Pass", nums, result)
        else:
            print("Fail", nums, result, expected)

    print("*** End of the program")
