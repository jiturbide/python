from collections import deque
from typing import List


def check_match_patern(pattern, subarray):
    len_pat = len(pattern)
    for i in range(len(pattern)):
        if pattern[i] == "0":
            if subarray[i] == "a" or subarray[i] == "e" or subarray[i] == "i" or subarray[i] == "o" or subarray[i] == "u" or subarray[i] == "y":
                continue
            else:
                return False

    return True

def compute_string_pattern_matching(pattern, array):
    matches = 0
    len_pat = len(pattern)

    i = 0
    while i < len(array) - len_pat:
        if check_match_patern(pattern, array[i:i+len_pat]):
            matches += 1
        i += 1

    return matches

if __name__ == '__main__':
    print("*** Start of the program")

    testCases = [
        ("010", "amazing", 2),
        ("100", "codesignal", 0),
        ("001", "yellowstone", 1)
    ]

    for pattern, array, expected in testCases:
        result = compute_string_pattern_matching(pattern, array)
        if result == expected:
            print("Pass", pattern, array,  result)
        else:
            print("Fail", pattern, array,  result, expected)

    print("*** End of the program")
