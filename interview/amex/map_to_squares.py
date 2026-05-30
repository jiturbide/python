def mapToSquares(lst: list):
    squares = []
    
    for n in lst:
        squares.append(n*n)
        
    return squares 

if __name__ == '__main__':
    obtained = mapToSquares([2, 3, 4])
    expected = [4, 9, 16]
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)
