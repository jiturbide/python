from collections import deque
from typing import List

def fun(arr):
    return arr

if __name__ == '__main__':
    print("*** Start of the program")

    testCases = [
        ([7, 1, 3, 2, 4, 5, 6], 0, 0)
    ]

    for data, k, expected in testCases:
        result = fun(data)
        if result == expected:
            print(f"Pass: {data}, k:{k}, res:{result}")
        else:
            print(f"Fail: {data}, k:{k}, res:{result}, expected:{expected}")

    print("*** End of the program")
