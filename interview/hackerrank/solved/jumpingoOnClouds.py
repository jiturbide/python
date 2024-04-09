import os

# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def jumpingOnClouds(c):
    # Write your code here
    jumpsCount = 0
    currentPos = 0
    
    while currentPos + 1 < len(c):
        if currentPos + 2 < len(c) and c[currentPos+2] == 0:
            currentPos +=2
        else:
            currentPos += 1
        jumpsCount += 1
    
    return jumpsCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
