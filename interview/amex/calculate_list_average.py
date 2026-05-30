
def calculateAverage(lst:list):
    if len(lst) == 0:
        return 0
    
    sum = 0
    for n in lst:
        sum = sum + n

    return sum / len(lst)

if __name__ == '__main__':
    obtained = calculateAverage([10, 20, 30])
    expected = 20.0
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
