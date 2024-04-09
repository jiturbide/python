from typing import List
# https://www.metacareers.com/profile/coding_puzzles?puzzle=203188678289677&t=UElFRXZhbHVhdGVBdXRvQ2FuZGlkYXRlQXZhaWxhYmlsaXR5SW52aXRhdGlvbjgwNDE1NjQ3NTA4NDQ3MjpXdWhqZWtPZjZTZldLWnNZUVk0WEhaYzNIcXR4YlNUWW9OZGY0QlRLM3hrM1FGRXliek85cFMya0k3cG1rT3ht

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    morePeople = 0

    place = 0
    while place < N:
        available = not ((place+1) in S)

        x = place + 1
        nextPlaceOccupied = False
        while x < place + K + 1 and x < N:
            if (x+1) in S:
                nextPlaceOccupied = True
                break
            x += 1
        
        if nextPlaceOccupied == True:
            place = x
        else:
            if available:
                print("a:", place)
                morePeople += 1
            place = x

    return morePeople            
            

if __name__ == "__main__":
    
    n = 15 #sits
    k = 2 #spacing
    m = 3 #people
    s = [11, 6, 14]

    # n = 10 #sits
    # k = 1 #spacing
    # m = 2 #people
    # s = [2,6]

    n = 3 #sits
    k = 2 #spacing
    m = 2 #people
    s = [1]

    result = getMaxAdditionalDinersCount(n,k,m,s)

    print(result)