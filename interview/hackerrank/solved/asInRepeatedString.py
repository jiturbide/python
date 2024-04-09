import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/repeated-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def repeatedString(str, maxNumChar):
    # Write your code here
    timesToRepeatCompleteString = maxNumChar // len(str)
    charactersRemanentString = maxNumChar % len(str)
    
    ainCompleteString = timesToRepeatCompleteString * countCharactersInString(str, len(str))
    ainRemanentString = countCharactersInString(str, charactersRemanentString)
    
    return ainCompleteString + ainRemanentString
    
    
def countCharactersInString(str, numCharToConsider):
    countA = 0
    currentIndex = 0
    if (len(str) == 0 or numCharToConsider <= 0):
        return 0
    
    for c in str:
        if c == 'a':
            countA += 1
        currentIndex += 1
        if currentIndex >= numCharToConsider:
            break
            
    return countA

if __name__ == '__main__':
    s = 'abcab'
    n = 10
    #result = countCharactersInString(s, n)
    result = repeatedString(s, n)
    print ('result', result)
