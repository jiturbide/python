'''
Challenge 2: Sliding Window / Subarray Optimization (Medium)
Problem StatementIn backend engineering, resource allocation and telemetry
monitoring often require analyzing continuous chunks of data.
You are given an array of integers server_loads representing the load on a
cluster of servers over $N$ consecutive seconds, and an integer k.
Find the maximum sum of server loads across any contiguous subarray of size k.

Constraints 1 <= k <= length of server_loads <= 10^5
-10 <= server_loads[i] <= 10^4

'''

def max_subarray_sum(server_loads: list[int], k: int) -> int:

    if len(server_loads) == 0: return 0
    max_load = 0
    idxs = 0
    idxe = k - 1

    # Initial load sum
    i = 0
    while i < len(server_loads) and i < k:
        max_load += server_loads[i]
        i += 1

    current_load = max_load
    while idxe < len(server_loads):
        if idxe + 1 < len(server_loads):
            current_load = current_load - server_loads[idxs] + server_loads[idxe+1]
            max_load = max(max_load, current_load)
        idxe += 1
        idxs += 1

    return max_load

if __name__ == "__main__":
    result = max_subarray_sum([2,4,6,8,4,2,5,9,1,6], 2)
    expected = 14
    print("Result:", result, ", expected:", expected, ", correct:", result == expected)

    result = max_subarray_sum([2,4,6,8,4,2,5,9,1,6], 3)
    expected = 18
    print("Result:", result, ", expected:", expected, ", correct:", result == expected)
