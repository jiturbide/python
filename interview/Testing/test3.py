if __name__ == "__main__":

    nums = [2,20,4,10,3,4,5]
    # nums.sort()
    #2,3,4,4,5,10,10
    nums_sorted = sorted(nums)

    print(nums_sorted)
    current_maximum = 0
    maximum = 0
    for i in range(len(nums_sorted)):
        print('i=', i)
        if i < len(nums_sorted) -1:
            if nums_sorted[i+1] - nums_sorted[i] <= 1:
                current_maximum = current_maximum + 1
            if current_maximum > maximum:
                maximum = current_maximum
