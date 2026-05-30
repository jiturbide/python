def count_vowels(the_string):
    vowels_set = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    count = 0
    for c in the_string:
        if c in vowels_set:
            count += 1

    return count

if __name__ == '__main__':
    the_string = 'Programming In Java'
    result = count_vowels(the_string)
    expected = 6
    print("Result:", result, ", expected:", expected, ", correct:", result == expected)
