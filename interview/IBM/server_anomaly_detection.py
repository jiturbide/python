def get_server_load_anomaly(samples):
    if samples is None or len(samples) ==0: return []

    average = 0
    sum = 0
    for s in samples:
        sum += s

    average = sum/len(samples)
    anomalies = []

    for i in range(len(samples)):
        if samples[i] > average*2:
            anomalies.append(i)

    return anomalies



if __name__ == '__main__':
    print("Start of the program")

    testCases = [
        ([1,3,2,8,1,2], [3]),
        ([4,4,4,4,4,3], [])
    ]

    for nums, expected in testCases:
        result = get_server_load_anomaly(nums)
        if result == expected:
            print("Pass", nums, result)
        else:
            print("Fail", nums, result, expected)


'''
Problem Statement
You are given an integer array load of length n representing server loads recorded at consecutive timestamps. A load value is considered anomalous if it is strictly greater than twice the average load across all timestamps.
Return a list of all 0-based indices where an anomalous load was recorded, in ascending order. If no anomalies are found, return an empty list.
Input Format

First line: integer n — number of timestamps
Second line: n space-separated integers representing load values

Constraints

1 ≤ n ≤ 10^5
0 ≤ load[i] ≤ 10^6

Sample Input
6
1 3 2 8 1 2
Sample Output
3
Explanation

Average = (1+3+2+8+1+2)/6 = 2.83. Twice the average ≈ 5.67. Only load[3] = 8 exceeds it.
'''