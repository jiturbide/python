import heapq

arr = [3, 1, 4, 1, 5, 9, 2]

# convert array into a heap in-place. O(n)
heapq.heapify(arr)
print("1 arr:", arr)

# push 0 to the heap. O(log n)
heapq.heappush(arr, 0)
print("2 arr:", arr)

# peek the min element = 0. O(1)
arr[0]

# pop and return the min element = 0. O(log n)
min_element = heapq.heappop(arr)

# peek the new min element = 1. O(1)
arr[0]

