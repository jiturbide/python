from functools import reduce

def getArtisticPhotographCount(N, C, X, Y):
    photographs = 0
    for i in range(len(C) - 2):
        if C[i] == 'P':
            minIndexA = i + X
            maxIndexA = i + Y
            j = minIndexA
            while j <= maxIndexA and j < len(C) - 1:
                if C[j] == 'A':
                    minIndexB = j + X
                    maxIndexB = j + Y
                    k = minIndexB
                    while k <= maxIndexB and k < len(C):
                        if C[k] == "B":
                            print(i,j,k, C[i], C[j], C[k])
                            photographs += 1
                        k += 1
                j += 1

    return photographs

if __name__ == "__main__":
    
    N = 8
    C = ".PBAAP.B"
    X = 1
    Y = 3
    
    # N = 5
    # C = "APABA"
    # X = 1
    # Y = 2
    result = getArtisticPhotographCount(N, C, X, Y) + getArtisticPhotographCount(N, "".join(reversed(C)), X, Y)
    
    print("result:", result)
    
    #Options for reversing strings
    m = "Hello world!"
    print(m[::-1])
    print("".join(reversed(m)))
    print(reduce(lambda a,b: b + a, m))
    
