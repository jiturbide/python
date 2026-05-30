def isPowerOfTwo(x):
    tmp = x
    powoftwo = False
    
    while tmp > 0:
        if tmp // 2 > 0 and tmp % 2 > 0:
            return False
        tmp = tmp // 2
    
    return True
    
if __name__ == '__main__':
    obtained = isPowerOfTwo(23)
    expected =  False
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = isPowerOfTwo(32)
    expected =  True
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

