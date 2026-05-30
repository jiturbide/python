def moveCharToEnd(str, tomove):
    result = ''
    tmpstr = ''
    
    for c in str:
        if c == tomove:
           tmpstr = tmpstr + c
        else:
            result = result + c
    
    return result + tmpstr 
    

if __name__ == '__main__':
    obtained = moveCharToEnd("programming", 'm')
    expected =  'prograingmm'
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

