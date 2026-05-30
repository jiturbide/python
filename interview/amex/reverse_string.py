def reverse_string(the_string):
    reversed = ''
    for c in the_string:
        reversed = c + reversed
    return reversed

if __name__ == '__main__':
    print('reversed=' + reverse_string('hello'))
    
    