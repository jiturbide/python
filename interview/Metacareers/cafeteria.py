# https://www.metacareers.com/profile/coding_puzzles?puzzle=203188678289677&source=cp_alert_email_delete
from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    morePeople = 0
    S.sort()
    place = 0
    calculatedMap = {}
    for indexS in range(len(S)):
        if indexS == 0:
          spacesAvailable = S[0] - 1
          people = calculatePeople(K, spacesAvailable, True, calculatedMap)
          morePeople += people
        
        if indexS == len(S) - 1:
          spacesAvailable = N - S[len(S)-1]
          people = calculatePeople(K, spacesAvailable, True, calculatedMap)
          morePeople += people
          break
        else:
          spacesAvailable = S[indexS + 1] - S[indexS] -1
          people = calculatePeople(K, spacesAvailable, False, calculatedMap)
          morePeople += people

    return morePeople            

  
def calculatePeople(K, spacesAvailable, edge, calculatedMap):
  sits = 0
  n = 1
  
  if spacesAvailable in calculatedMap:
    return calculatedMap[str(spacesAvailable) + str(edge)]
  
  while True:
    minimumPerPerson = 0
    if edge == True:
      minimumPerPerson = n + (n * K)
    else:
      minimumPerPerson = n + ((n+1) * K)      
      
    if spacesAvailable < minimumPerPerson:
      break
    else:
      sits += 1
      n += 1
  
  calculatedMap[str(spacesAvailable) + str(edge)] = sits
    
  return sits


if __name__ == "__main__":
    N = 10
    K = 1
    M = 2
    S = [2, 6]
    
    expected = 3
    result = getMaxAdditionalDinersCount(N, K, M, S)
    print("Result:", result, ", expected:", expected, ", correct:", result == expected)
    
    N = 15
    K = 2
    M = 3
    S = [11, 6, 14]
    expected = 1
    result = getMaxAdditionalDinersCount(N, K, M, S)
    print("Result:", result, ", expected:", expected, ", correct:", result == expected)
