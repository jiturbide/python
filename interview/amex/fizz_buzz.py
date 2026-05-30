def fizz_buzz(x):
    the_list = []
    
    for i in range(1, x+1):
        if i%3 == 0 and i%5 == 0:
            the_list.append("FizzBuzz")
        elif i%3 == 0:
            the_list.append("Fizz")
        elif i%5 == 0:
            the_list.append("Buzz")
        else:
            the_list.append(str(i))
    
    return the_list

if __name__ == "__main__":

    obtained = fizz_buzz(15)
    expected = ["1", "2", "Fizz", "4", "Buzz"]
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
