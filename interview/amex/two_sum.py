def twoSum(lst, target):
    complements = {}
    
    for i in range(len(lst)):
        comp = target-lst[i]
        if comp not in complements:
            complements[lst[i]]=i
        else:
            return [complements[target-lst[i]], i]
        
    return []

if __name__ == "__main__":

    obtained = twoSum([2, 7, 11, 15], 9)
    expected = [0, 1]
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = twoSum([2, 7, 11, 15], 10)
    expected = []
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
