def isPalindromeNumber(x):
    reverted = 0
    tmp = x
    while tmp > 0:
        reverted = reverted * 10 + tmp % 10
        tmp = tmp // 10
    print("reverted", reverted)
    if x == reverted:
        return True
    else:
        return False
    

if __name__ == "__main__":
    
    obtained = isPalindromeNumber(123454321)
    expected = True
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = isPalindromeNumber(110101012)
    expected = False
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
