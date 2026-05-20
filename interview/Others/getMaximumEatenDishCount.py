from typing import List
# https://www.metacareers.com/profile/coding_puzzles?puzzle=958513514962507&t=UElFRXZhbHVhdGVBdXRvQ2FuZGlkYXRlQXZhaWxhYmlsaXR5SW52aXRhdGlvbjgwNDE1NjQ3NTA4NDQ3MjpXdWhqZWtPZjZTZldLWnNZUVk0WEhaYzNIcXR4YlNUWW9OZGY0QlRLM3hrM1FGRXliek85cFMya0k3cG1rT3ht

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  eatenDish = 0
  lastRecent = []
  
  for i in range(len(D)):
    if D[i] not in lastRecent:
      eatenDish += 1
      
      if len(lastRecent) == K:
        lastRecent.pop()
      
      lastRecent.insert(0, D[i])  
    print(lastRecent)
    
  return eatenDish

if __name__ == "__main__":
    
    N = 6
    D = [1,2,3,3,2,1]
    K = 1
    
    result = getMaximumEatenDishCount(N, D, K)

    print("result=", result)
    