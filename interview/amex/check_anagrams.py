def check_anagrams(str1: str, str2: str):
    s1 = str1.lower()
    s2 = str2.lower()
    
    if s1 is None or s2 is None or len(s1) != len(s2):
        return False
    
    map_s1 = {}
    
    for c in s1:
        if c in map_s1:
            map_s1[c] = map_s1[c] + 1
        else:
            map_s1[c] = 1
            
    for c in s2:
        if c in map_s1:
            map_s1[c] = map_s1[c] - 1
            
    for val in map_s1.values():
        if val !=0:
            return False

    return True

if __name__ == '__main__':
    result = check_anagrams('listen', 'sil ent')
    expected = True
    print("check_anagrams('listen', 'silent')")
    print("Result:", result, ", expected:", expected, ", correct:", result == expected)
