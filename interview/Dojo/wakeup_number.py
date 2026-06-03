'''
not 0
not repeated
not in this sequence HLH

'''
from collections import deque

def checkif_valid_wakeup(number):
    if number < 0: return False
    tmp = number
    unique = set()
    lst_mid_num = [] # list for checking if a number is in the middle of a 2 high values
    digit = 0
    
    while tmp > 0:
        digit = tmp % 10
        tmp = tmp // 10
        if digit == 0: return False
        
        if digit in unique: 
            return False
        else:
            unique.add(digit)

        lst_mid_num.append(digit)
        if len(lst_mid_num) > 3:
            lst_mid_num.pop(0)
        elif len(lst_mid_num) == 3:
            if lst_mid_num[0] > lst_mid_num[1] and lst_mid_num[1] < lst_mid_num[2]:
                return False
        
        
    return True
        
        
if __name__ == "__main__":
    
    obtained = checkif_valid_wakeup(123456)
    expected = True
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = checkif_valid_wakeup(12)
    expected = True
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = checkif_valid_wakeup(728)
    expected = False
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
