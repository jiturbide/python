# I How many ways it can be get a number with the sum of squares 
# II What is the minimum count of squares to sum so that we can get a number

# 12 = 3x3 + 1x1 + 1x1 + 1x1 = 4
# 12 = 2x2 + 2x2 + 2x2 = 3
# 12 = 1x1 x 12 = 12

from collections import deque
from typing import List

def get_possible_squares(num) -> List:
    next = 1
    possible_squares = []

    while next*next <= num:
        possible_squares.append(next*next)
        next += 1

    return possible_squares

def calculate_ways(num):
    if num == 0:
        return 1

    squares = get_possible_squares(num)
    ways = 0
    for s in squares:
        print(f"squares: {squares}, num {num}, {s}, {num-s}")
        ways += calculate_ways(num-s)

    return ways

def calc_ways_to_reach_a_num_with_squares(num):
    if num is None or num == 0:
        return 0

    return calculate_ways(num)


if __name__ == '__main__':
    print("Start of the program")

    testCases = [
        (12, 30),
        # (3, 1),
        # (4, 2),
        # (5, 3)
    ]

    for num, expected in testCases:
        result = calc_ways_to_reach_a_num_with_squares(num)
        if result == expected:
            print("Pass", num, result)
        else:
            print("Fail", num, result, expected)
