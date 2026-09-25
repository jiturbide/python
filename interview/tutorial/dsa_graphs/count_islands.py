# https://www.hellointerview.com/learn/code/depth-first-search/introduction
from collections import deque
from typing import List


def counting_islands(data):
    if data is None or len(data) == 0:
        return 0

    visited = set()
    movs = [(-1,0), (1,0), (0,1), (0,-1)]
    islands = 0

    # if 1=land, flood island
    def dfs(coord):
        if coord in visited:
            return

        visited.add(coord)

        for y,x in movs:
            yy = coord[0]+y
            xx = coord[1]+x
            is_inside = yy >= 0 and yy < len(data) and xx >= 0 and xx < len(data[0])
            if is_inside and data[yy][xx] == 1:
                dfs((yy, xx)) 

        return

    # traverse grid
    for i in range(len(data[0])):
        for j in range(len(data)):
            if data[j][i] == 1 and (j,i) not in visited:
                dfs((j,i))
                islands += 1

    return islands

if __name__ == '__main__':
    print("*** Start of the program")

    testCases = [
        ([[0, 1, 0, 0, 0, 0],
          [0, 1, 1, 0, 1, 0],
          [0, 0, 0, 1, 1, 0],
          [1, 1, 0, 0, 0, 1],
          [1, 1, 0, 0, 0, 1]], 4),
        ([[0, 1, 0, 0, 0, 0],
          [0, 1, 1, 0, 1, 0],
          [0, 0, 0, 0, 1, 0],
          [1, 1, 0, 1, 1, 1],
          [1, 1, 0, 0, 1, 0]], 3)
    ]

    for data, expected in testCases:
        result = counting_islands(data)
        if result == expected:
            print(f"Pass: {data}, res:{result}")
        else:
            print(f"Fail: {data}, res:{result}, expected:{expected}")


    print("*** End of the program")







'''

'''