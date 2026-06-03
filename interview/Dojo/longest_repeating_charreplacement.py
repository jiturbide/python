
def characterReplacement(s: str, k: int) -> int:
    max_string = 0
    dchars = set()

    for c in s:
        dchars.add(c)

    max_string = 1
    for c in dchars:
        current_max_string = 0
        remaining_gap = k
        idxs = 0
        idxe = 0

        while idxe < len(s):
            if s[idxe] != c:
                remaining_gap -= 1
                if remaining_gap < 0:
                    idxs += 1
                    if s[idxs] != c:
                        remaining_gap += 1
                else:
                    current_max_string += 1
            else:
                current_max_string += 1

            if current_max_string > max_string:
                max_string = current_max_string
            idxe += 1
    return max_string

if __name__ == "__main__":
    
    obtained = characterReplacement("AABABBA", 1)
    expected = 4
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
    
    
    
    obtained = characterReplacement("AABB", 2)
    expected = 4
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = characterReplacement("AABBBA", 2)
    expected = 5
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = characterReplacement("B", 2)
    expected = 1
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
