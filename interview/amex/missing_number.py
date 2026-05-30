def missing_number(the_list):
    sorted_list = sorted(the_list)
    
    missing = None
    previous = sorted_list[0] - 1
    for current in sorted_list:
        if current - previous > 1:
            missing = current - 1
            break
        previous = current
            
    return missing        

if __name__ == '__main__':
    obtained = missing_number([3,0,1])
    expected = 2
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
