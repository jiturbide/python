def first_nonrepeating_character(str):
    mapc = {}
    listc = []
    
    for c in str:
        if c not in mapc:
            mapc[c] = 1
        else:
            mapc[c] = mapc[c] + 1
    
    for c in str:
        if mapc[c] == 1:
            return c
    
    return None
    

if __name__ == '__main__':
    obtained = first_nonrepeating_character("aabbcdeef")
    expected = "c"
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
