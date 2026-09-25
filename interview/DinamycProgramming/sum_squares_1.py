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

    def calculate_ways(self, target, num, curr_tracking, current_count):
        if num == 0:
            print(f"target: {target}, num: {num} tracking: {curr_tracking}, current_count: {current_count}")
            if current_count < self.min_count:
                self.min_count = current_count
                self.tracking = curr_tracking
            return 1

        squares = self.get_possible_squares(num)

        if num not in self.map_ways:
            ways = 0
            for sq in squares:
                curr_tracking = curr_tracking + "" + str(num-sq) + "_"
                if num-sq not in self.map_ways:
                    print(f"squares: {squares}, num:{num}, sq:{sq}, num-sq:{num-sq}")
                    self.map_ways[num-sq] = self.calculate_ways(num, num-sq, curr_tracking, current_count+1)
                ways += self.map_ways[num-sq]
            self.map_ways[num] = ways
        return self.map_ways[num]

if __name__ == '__main__':
    print("Start of the program")

    testCases = [
        # (12, 30),
        # (3, 1),
        # (4, 2),
        # (5, 3),
        (6,4)
    ]

    for num, expected in testCases:
        result = Solution().calc_ways_to_reach_a_num_with_squares(num)
        if result == expected:
            print("Pass", num, result)
        else:
            print("Fail", num, result, expected)
