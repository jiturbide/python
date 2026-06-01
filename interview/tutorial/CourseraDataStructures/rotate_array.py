# WRITE ROTATE FUNCTION HERE #
#                            #
#                            #
#                            #
#                            #
##############################
def rotate2(lst:list, k):
    if k == 0 or k % len(lst) == 0:
        return lst


    for i in range(k):
        tmp = lst[0]
        for j in range(len(lst)):
            new_index = (j + 1) % len(lst)
            tmp2 = lst[new_index]
            lst[new_index] = tmp
            tmp = tmp2
    
def rotate(lst:list, k):
    if k == 0 or k % len(lst) == 0:
        return lst

    k = k % len(lst)
    lst1 = lst[k:len(lst)]
    lst2 = lst[0:k]
    lst[:] = lst1 + lst2

    return lst

nums = [1, 2, 3, 4, 5, 6, 7]
k = 8
rotate(nums, k)
print("Rotated array:", nums)

nums = [1, 2, 3, 4, 5, 6, 7]
k = 9
rotate(nums, k)
print("Rotated array:", nums)

nums = [1, 2, 3, 4, 5, 6, 7]
k = 10
rotate(nums, k)
print("Rotated array:", nums)

nums = [1, 2, 3, 4, 5, 6, 7]
k = 11
rotate(nums, k)
print("Rotated array:", nums)

nums = [1, 2, 3, 4, 5, 6, 7]
k = 12
rotate(nums, k)
print("Rotated array:", nums)

nums = [1, 2, 3, 4, 5, 6, 7]
k = 13
rotate(nums, k)
print("Rotated array:", nums)

nums = [1, 2, 3, 4, 5, 6, 7]
k = 14
rotate(nums, k)
print("Rotated array:", nums)

"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""