
def maxSlidingWindow(nums, k):
    if len(nums) == 0:
        return []
    if k > len(nums):
        return None
    
    result=[]
    for i in range(len(nums)-k+1):
        max = sorted(nums[i:i+k])[k-1]
        result.append(max)
    return result

if __name__ == "__main__":
    
    obtained = maxSlidingWindow([2, 1, 5, 3, 6, 4, 8, 5], 3)
    expected = [5, 5, 6, 6, 8, 8]
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = maxSlidingWindow([9, 7, 2, 4, 6], 2)
    expected = [9, 7, 4, 6]
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
