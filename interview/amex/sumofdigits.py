def sumOfDigits(num):
    sum = 0
    tmp = num
    while tmp > 0:
        sum = sum + tmp%10
        tmp = tmp //10 
    return sum

if __name__ == '__main__':
    obtained = sumOfDigits(12345)
    expected =  15
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
