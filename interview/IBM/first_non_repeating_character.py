'''
Challenge 1: String Manipulation & Hashing (Easy/Medium)Problem StatementIBM
often processes large amounts of log data or textual configuration files.
Given a string s consisting of lowercase English letters, find the first
non-repeating character in it and return its 0-indexed position.
If it does not exist, return -1.

Constraints:
1 <= length of s <= 10^5
s consists of lowercase English letters only.
'''

def first_unique_char(s: str) -> int:
    index = -1

    count_map = {}

    for c in s:
        if c in count_map:
            count_map[c] += 1
        else:
            count_map[c] = 1

    for i in range(len(s)):
        if count_map[s[i]] == 1:
           index = i
           break

    return index

if __name__ == "__main__":
    result = first_unique_char("aabbcdcdew")
    expected = 8
    print("Result:", result, ", expected:", expected, ", correct:", result == expected)

    result = first_unique_char("aabbcc")
    expected = -1
    print("Result:", result, ", expected:", expected, ", correct:", result == expected)

    result = first_unique_char("abcdabw")
    expected = 2
    print("Result:", result, ", expected:", expected, ", correct:", result == expected)
