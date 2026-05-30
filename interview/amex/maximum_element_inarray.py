def findMax(lst):
    max = -1    
    current = -1
    
    for i in lst:
        current = i
        if current > max:
            max = current
        
    
    return max

if __name__ == '__main__':
    obtained = findMax([15, 3, 88, 7, 42])
    expected =  88
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

