def isSorted(array: list):
    if len(array) == 0:
        return False
    
    previous = -1
    
    for i in array:
        if i < previous:
            return False
        previous = i

    return True
    
if __name__ == "__main__":

    obtained = isSorted([1, 5, 10, 10, 15])
    expected = True
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = isSorted([1, 15, 5, 10])
    expected = False
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
