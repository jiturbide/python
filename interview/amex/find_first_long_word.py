def findFirstLongWord(lst: list, greater_than: int):
   
    for w in lst:
        if len(w) > greater_than:
            return w
        
    return None
    

if __name__ == '__main__':
    obtained = findFirstLongWord(["cat", "elephant", "dog"], 5)
    expected = "elephant"
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
    
if __name__ == '__main__':
    obtained = findFirstLongWord(["cat", "elephant", "dog"], 15)
    expected = None
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

