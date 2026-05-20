from typing import List
# https://neetcode.io/problems/three-integer-sum/question?list=neetcode150

def threeSum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []

    result = []
    nums_sorted = sorted(nums)

    for i in range(1, len(nums_sorted)-1):
        for k in range(0, i):
            for j in range(i+1, len(nums)):
                ni = -nums_sorted[i]
                nk = nums_sorted[k]
                nj = nums_sorted[j]

                if -ni == nk + nj:
                    result.append([nk, ni, nj])
    return result

if __name__ == '__main__':
    # nums=[-1,0,1]
    nums=[-1,0,1,2,-1,-4]

    res = threeSum(nums)
    print('res', res)
