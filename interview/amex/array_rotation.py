def array_rotation(array, times):
    if times == 0 or times % len(array) == 0:
        return array
    
    for i in range(times % len(array)):
        array.insert(0, array.pop())        
    
    return array

def array_rotation2(array, times):
    if times == 0 or times % len(array) == 0:
        return array
    
    for i in range(times % len(array)):
        array.insert(0, array.pop())        
    
    return array

if __name__ == '__main__':
    obtained = array_rotation([1, 2, 3, 4, 5], 2)
    expected =  [4, 5, 1, 2, 3]
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = array_rotation([1, 2, 3, 4, 5, 6], 6)
    expected =  [1,2,3,4,5,6]
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
