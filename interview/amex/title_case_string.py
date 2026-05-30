def titleCase2(x: str):
    words = x.split(' ')
    title_cased = ""
        
    for word in words:
        if ord(word[0]) > ord('a') and ord(word[0]) < ord('z'):
            word[0] = ascii(ord(word[0]) + (ord('A')-ord('a')))
        title_cased = title_cased + ' '

    return title_cased

def titleCase(the_str: str):
    previous_char = ' '
    title_case = ''
    increment = ord('a')-ord('A')
    
    for c in the_str:
        ord_c = ord(c)
        if previous_char == ' ' and ord_c >=ord('A') and ord_c <= ord('z'):
            uppercase_char = chr(ord(c)+increment)
            title_case = title_case + uppercase_char
        else:
            title_case = title_case + c
        previous_char = c
            
    return title_case

if __name__ == "__main__":
    
    obtained = titleCase("this is a test sentence") 
    expected = "This Is A Test Sentence"
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
