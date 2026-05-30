def max_consecutive_ones(the_list):
    max = 0
    current_max = 0
    
    for n in the_list:
        if n == 1:
            current_max += 1
            if current_max > max:
                max = current_max
        else:
            current_max = 0    
    
    return max

if __name__ == "__main__":

    obtained = max_consecutive_ones([1, 1, 0, 1, 1, 1, 0, 1])
    expected = 3
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
