'''
Challenge 3: Simulation / Business Logic Parsing (Medium)
Problem StatementIBM assessments frequently include a "real-world simulation"
problem where you parse custom request schemas or simulate an application state.
An API Gateway receives a list of backend requests.
Each request is represented as a string in the format "REQUEST_ID,TIMESTAMP".
The gateway has a rate limit: it drops any request if a request with the exact
same REQUEST_ID arrived less than 5 seconds ago.Given an array of requests sorted
chronologically by timestamp, return an array of strings indicating whether each
request was "ALLOWED" or "DROPPED".
ExampleInput: requests = ["req1,1", "req2,2", "req1,3", "req1,6", "req2,8"]
Output: ["ALLOWED", "ALLOWED", "DROPPED", "ALLOWED", "ALLOWED"]
(Note: "req1" at t=3 is dropped because the previous "req1" was at t=1,
and 3 - 1 < 5. "req1" at t=6 is allowed because 6 - 1 <= 5.)
Constraints1 <= requests.length = 10^4
Timestamps are positive integers in strictly increasing order.

'''

def process_requests(requests: list[str]) -> list[str]:

    if len(requests) == 0: return []

    map_log_requests = {}
    result = []

    # Traverse requests
    for r in requests:
        req, ts = r.split(",")
        if req in map_log_requests:
            if int(ts) - int(map_log_requests[req]) >= 5:
               result.append("ALLOWED")
               map_log_requests[req] = int(ts)
            else:
                result.append("DROPPED")
        else:
            map_log_requests[req]= int(ts)
            result.append("ALLOWED")

    return result




if __name__ == "__main__":
    result = process_requests(["req1,1", "req2,2", "req1,3", "req1,6", "req2,8"])
    expected = ["ALLOWED", "ALLOWED", "DROPPED", "ALLOWED", "ALLOWED"]
    print("Result:", result, ", expected:", expected, ", correct:", result == expected)

    result = process_requests(["req1,1", "req2,2", "req3,3", "req4,6", "req5,8"])
    expected = ["ALLOWED", "ALLOWED", "ALLOWED", "ALLOWED", "ALLOWED"]
    print("Result:", result, ", expected:", expected, ", correct:", result == expected)
