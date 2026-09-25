# I How many ways it can be get a number with the sum of squares 

# 12 = 3x3 + 1x1 + 1x1 + 1x1 = 4
# 12 = 2x2 + 2x2 + 2x2 = 3
# 12 = 1x1 x 12 = 12

import math
from typing import List

class Solution:
    def __init__(self):
        self.possible_squares = []
        self.map_ways = {}
        self.min_count = 0
        self.tracking = ""

    def get_possible_squares(self, num) -> List:
        next = 1
        possible_squares = []

        while next*next <= num:
            possible_squares.append(next*next)
            next += 1

        return possible_squares

    def calc_ways_to_reach_a_num_with_squares(self, num):
        if num is None or num == 0:
            return 0
        self.possible_squares = self.get_possible_squares(num)
        self.min_count = num

        ways = self.calculate_ways(num, num, "", 0)

        print(f"Ways: {ways} Tracking: {self.tracking} min_count: {self.min_count} map:{self.map_ways}")
        return ways

    def calculate_ways(self, target, num, tracking, current_count):
        if num == 0:
            if current_count < self.min_count:
                self.min_count = current_count
                self.tracking = tracking
                print(f"target: {target}, num: {num} tracking: {tracking}, current_count: {current_count}")
            return 1

        squares = self.get_possible_squares(num)

        ways = 0
        curr_tracking = tracking
        for sq in reversed(squares):
            curr_tracking = curr_tracking + "" + str(sq) + "_"
            print(f"squares: {squares}, num:{num}, sq:{sq}, num-sq:{num-sq}")
            ways += self.calculate_ways(num, num-sq, curr_tracking, current_count+1)
        return ways

if __name__ == '__main__':
    print("Start of the program")

    testCases = [
        (12, 30),
        # (3, 1),
        # (4, 2),
        # (5, 3),
        # (6,4)
    ]

    for num, expected in testCases:
        result = Solution().calc_ways_to_reach_a_num_with_squares(num)
        if result == expected:
            print("Pass", num, result)
        else:
            print("Fail", num, result, expected)
