def filterEvens(lst: list):
    evens_list = []
    
    for n in lst:
        if n % 2 == 0:
            evens_list.append(n)
            
    return evens_list
    
if __name__ == "__main__":

    obtained = filterEvens([1, 5, 10, 10, 15])
    expected = [10,10]
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    obtained = filterEvens([10, 150, 51, 44])
    expected = [10,150,44]
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
