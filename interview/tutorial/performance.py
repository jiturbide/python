from timeit import default_timer as timer
from datetime import timedelta
from collections import deque

if __name__ == "__main__":
    
    msg = "!@#$%^&*()*(((())))" * 10000
    
    aList = ["."]
    queue = deque()
    
    start = timer()
    for e in msg:
        #aList.insert(0,e)
        #aList.pop()
        aList.append(e)
    end = timer()
    
    print("List time: ", timedelta(seconds=end-start))
    
    # -----------------------------
    
    start = timer()
    for e in msg:
        queue.appendleft(e)    
    
    end = timer()
    print("List time: ", timedelta(seconds=end-start))
    print("queue len", len(queue))
    
    