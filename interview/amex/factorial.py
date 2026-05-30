def factorial(x):
    calculated = None

    if x == 0:
        return 0
    
    if x > 0:
        calculated = 1
        
        for x in range(1, x+1):
            calculated = calculated * x    
    
    return calculated


if __name__ == '__main__':
    obtained = factorial(0)
    expected = 0
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = factorial(5)
    expected = 120
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = factorial(-1)
    expected = None
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
