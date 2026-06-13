from bisect import bisect_left, bisect_right

'''
Part 1: Tough Data Structures & Algorithms (DSA)Challenge 1: Log Aggregator & Multi-Key Range Querying (Advanced Hashing + Balanced Trees)Problem StatementIBM Cloud needs a component to monitor microservice latencies. You are given a stream of API log entries. Each entry contains a timestamp (unique integer), a service_name (string), and a latency (integer in milliseconds).Implement a system that can efficiently process these entries and answer range queries. You need to write a function get_high_latency_services(start_time, end_time, threshold) that returns the names of all unique services that had at least one request with a latency $\ge \text{threshold}$ strictly within the time window [start_time, end_time] (inclusive).
'''

def search_latencies2(start_time, end_time, threshold, logs):
    result = []
    for log in logs:
        if log[0] < start_time:
            continue
        if log[0] > end_time:
            break
        if log[0] >= start_time and log[0] <= end_time and log[2] > threshold:
            result.append(log[1])

    return result

def search_latencies(start_time, end_time, threshold, logs):
    result = set()
    #sort logs
    sorted_logs = sorted(logs, key=lambda x:x[0])
    #extract timestamps
    timestamps = [log[0] for log in logs]
    ixs = bisect_left(timestamps,start_time)
    ixe = bisect_right(timestamps,end_time)

    for i in range(ixs, ixe):
        if sorted_logs[i][2] > threshold:
            result.add(sorted_logs[i][1])

    return sorted(list(result))


if __name__ == '__main__':
    print("Start of the program")

    start_time = 105
    end_time = 125
    threshold = 200

    testCases = [
        (start_time, end_time, threshold, ["payment-service", "shipping-service"])
    ]

    logs = [
        (100, "auth-service", 120),
        (105, "payment-service", 350),
        (110, "auth-service", 95),
        (120, "shipping-service", 400),
        (130, "payment-service", 80)
    ]

    for start_time, end_time, threshold, expected in testCases:
        result = search_latencies(start_time, end_time, threshold, logs)
        if result == expected:
            print("Pass", start_time, start_time, threshold, result)
        else:
            print("Fail", start_time, start_time, threshold, result, expected)
    #        0 1 2 3 4 5  6  7
    array = [1,1,2,3,5,8,13,21]

    print("start index: ", bisect_left(array, 0))
    print("start index: ", bisect_left(array, 1))
    print("start index: ", bisect_left(array, 4))
    print("start index: ", bisect_left(array, 5))
    print("start index: ", bisect_left(array, 6))
    print("start index: ", bisect_left(array, 34))
    print("---")
    print("start index: ", bisect_right(array, 0))
    print("start index: ", bisect_right(array, 1))
    print("start index: ", bisect_right(array, 4))
    print("start index: ", bisect_right(array, 5))
    print("start index: ", bisect_right(array, 6))
    print("start index: ", bisect_right(array, 34))



