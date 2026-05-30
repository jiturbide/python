def countFrequencies(lst: list):
    freqmap = {}
    
    for word in lst:
        if word.lower() not in freqmap:
            freqmap[word.lower()] = 1
        else:
            freqmap[word.lower()] = freqmap[word.lower()] + 1
    
    return freqmap
    
    
if __name__ == '__main__':
    obtained = countFrequencies(["apple", "banana", "Apple"])
    expected = {"apple": 2, "banana": 1}
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
    
