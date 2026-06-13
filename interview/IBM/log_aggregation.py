def log_aggregation(logs):

    if logs is None or len(logs) == 0: return None

    map_freq = {}
    list_freq = []

    max_freq = 0
    current_freq = 0

    for l in logs:
        if l not in map_freq:
            map_freq[l] = 1
            current_freq = 1
        else:
            current_freq = map_freq[l] + 1
            map_freq[l] = current_freq

        max_freq = max(max_freq, current_freq)

    for k in map_freq.keys():
        if map_freq[k] == max_freq:
            list_freq.append(k)

    return sorted(list_freq).pop(0)


if __name__ == '__main__':
    print("Start of the program")

    testCases = [
        (["ERROR","INFO","WARNING","ERROR","INFO","ERROR"], "ERROR"),
        (["beta","alpha","beta","alpha"], "alpha")
    ]

    for logs, expected in testCases:
        result = log_aggregation(logs)
        if result == expected:
            print("Pass", logs, result)
        else:
            print("Fail", logs, result, expected)


'''
Challenge 2: Log Aggregation
Problem

A server generates log entries represented as strings.

Given a list of logs, return the log that appears most frequently.

If multiple logs have the same maximum frequency, return the lexicographically smallest one.

Example
logs = ["ERROR","INFO","WARNING","ERROR","INFO","ERROR"]

Output
ERROR

Example 2

logs = ["beta","alpha","beta","alpha"]

Output
alpha

because frequencies tie:

alpha -> 2
beta -> 2

and "alpha" is lexicographically smaller.

Constraints
1 <= n <= 200000
'''