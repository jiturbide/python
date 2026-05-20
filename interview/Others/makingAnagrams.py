# https://www.hackerrank.com/challenges/making-anagrams/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

def makingAnagrams(s1, s2):
    # Write your code here
    # Create a dictionary with S1, key is the letter, value the occurrence
    # Traverse S2 and look each element in dictS1, decrease the count of each letter in map if it exist, remove if 0. If the character in S2 is not in S1 then add 1 to countS2
    # Sum remaining entries in dictS1 to countS2 
    
    dictS1 = {}
    removals = 0
    
    for i in range(len(s1)):
        if s1[i] in dictS1:
            dictS1[s1[i]] = dictS1[s1[i]] + 1
        else:
            dictS1[s1[i]] = 1
    
    print("dictS1:", dictS1)
    
    for c2 in s2:
        print("c2:", c2)
        if c2 in dictS1:
            count = dictS1[c2]
            if count > 1:
                dictS1[c2] = dictS1[c2] - 1
            else:
                del dictS1[c2]
        else:
            removals += 1
    
    print("removals:", removals, dictS1)
    
    for k, v in dictS1.items():
        removals += v
    
    print("removals:", removals)
    return removals
    
        
if __name__ == '__main__':
    
    # s1 = "abc"
    # s2 = "amnop"
    s1 = "cde"
    s2 = "abc"
    
    result = makingAnagrams(s1, s2)
    print("result:", result)
    