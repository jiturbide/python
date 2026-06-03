'''
Minimum Window Substring
Given two strings s and t, return the minimum length contiguous substring of s that contains every character of t (including duplicates). If no such substring exists, return "". Your solution must run in O(n + m) time, where n = len(s) and m = len(t). This is one of the most commonly asked hard-level string problems at top tech companies.
SIGNATURE
function minWindow(s: string, t: string): string
Constraints
1 ≤ s.length ≤ 100,000
1 ≤ t.length ≤ 1,000
s and t consist of uppercase and lowercase English letters
Expected time complexity: O(n + m)
Expected space complexity: O(m)
Examples
Test Cases
Example 1
INPUT s = "ADOBECODEBANC", t = "ABC"
OUTPUT "BANC"
BANC contains A, B, C and is the shortest such window.
Example 2
INPUT s = "a", t = "a"
OUTPUT "a"
The only character matches perfectly.
Example 3
INPUT s = "a", t = "aa"
OUTPUT ""

'''


def minWindow(s: str, t: str):
    if len(s) == 0 or len(t) == 0: return ""
    
    foundsofar = set()
    chars = set()
    
    for c in t:
        chars.add(c)
    
    idxs = 0
    idxe = 0
    min_found = None
    # XADOBECODEBANC
    
    while idxe < len(s):
        if idxs == idxe and s[idxe] not in chars:
            idxs += 1
            idxe += 1
        else:
            if s[idxs] in chars:         #current start char is in list of chars
                if chars.issubset(foundsofar):  #all chars found
                    if min_found == None:
                        min_found = (idxe-idxs, idxs, idxe)
                    elif idxe-idxs < min_found[0]:
                        min_found = (idxe-idxs, idxs, idxe)
                        
                    foundsofar.remove(s[idxs])
                    idxs +=1
            else:
                idxs += 1
        idxe += 1
    return s[idxs:idxe+1]
    
if __name__ == "__main__":
    
    obtained = minWindow("XADOBECODEBANC", "ABC")
    expected = "BANC"
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
