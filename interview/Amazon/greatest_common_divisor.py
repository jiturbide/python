def getGreatestCommonDivisor(arr):
    result = 0
    arr.sort()
    
    result = arr[0]
    for i in range(len(arr)):
        if arr[i] % arr[0] != 0:
            result = 0
            break
    return result
    


if __name__ == "__main__":

    arr = [2,4,6,8,10]
    expected = 2
    result = getGreatestCommonDivisor(arr)
    
    print("Result 1: ", result, (expected == result))

    arr = [3, 4, 8, 12, 20]
    expected = 0
    result = getGreatestCommonDivisor(arr)
    
    print("Result 2: ", result, (expected == result))
    
    '''
    The greates common divisor (GCD), also called highest common factor (HCF) of N numbers is the largest positive integer that divides all numbers without giving a remainder.

    Write an algorithm to determine the GCD of N positive integers.
    Input
    The input to the function/method consist of two arguments - num, an integer representing the number of positive integers (N) arr, a list of positive integers.

    Output
    Return an integer representing the GCD of the given positive integers.

    Example
    input:
    num = 5
    arr = [2,4,6,8,10]

    Output
    2
    Explanation:
    The largest positive number that divides all the positive integers 2,4,6,8,10 without remainder is 2
    So the output is 2.

    class GCD {
    public int generalizedGCD(int num, int [] arr){
    }
    }

    '''