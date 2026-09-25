# https://codesignal.com/blog/example-codesignal-questions/

from collections import deque
from typing import List
import copy

def get_overlap(field, figure, position, row):
    # check if collision, if found go to next position
    width_figure = 3
    height_figure = 3
    filled_field = copy.deepcopy(field) 
    for c in range(width_figure):
        for r in range(height_figure):
            print(f"({r+row},{c+position}) f:{filled_field[r+row][c+position]} bk:{figure[r][c]}")
            overlap = filled_field[r+row][c+position] + figure[r][c]
            if overlap == 2:
                return None # invalid
            else:
                filled_field [r+row][c+position] = overlap

    field_width = len(filled_field [0])
    # if no collision check if row created
    print(f"After: {filled_field}")
    for r in range(row, row+height_figure):
        count_filled = 0
        for c in range(field_width):
            if filled_field[r][c] == 1:
                count_filled += 1
        if count_filled == field_width:
            return position

    return -1


def calculate_drop_position(field, figure):
    # Initialize
    width_figure = 3
    width_field = len(field[0])
    height_figure = 3
    height_field = len(field)

    # check on each drop position and row
    for position in range(width_field-width_figure+1):
        for row in range(height_field-height_figure+1):
            overlap = get_overlap(field, figure, position, row)
            print(f"row: {row}, c: {position}, overlap?:{overlap}")
            if overlap is not None:
                if overlap != -1:
                    return position

    return -1                


if __name__ == '__main__':
    print("*** Start of the program")

    t1 = ([[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [1, 0, 0],
             [1, 1, 0]], 
             [[0, 0, 1],
             [0, 1, 1],
             [0, 0, 1]], 0)
    t2 = ([[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [1, 1, 0, 1, 0],
              [1, 0, 1, 0, 1]],
              [[1, 1, 1],
              [1, 0, 1],
              [1, 0, 1]], 2)
    t3 = ([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 0, 0, 1],
          [1, 1, 0, 1]],
          [[1, 1, 0],
          [1, 0, 0],
          [1, 0, 0]], -1)
    testCases = [
        t1       
    ]

    for field, figure, expected in testCases:
        result = calculate_drop_position(field, figure)
        if result == expected:
            print("Pass", len(field), len(figure), result)
        else:
            print("Fail", len(field), len(figure), result, expected)

    print("*** End of the program")
