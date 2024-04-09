import math
import os
import random
import re
import sys

# 

def fibonacci(elements):
    arr = []
    a = 0
    b = 1
    nextElement = 0
    
    for i in range(elements):
        arr.append(nextElement)
        nextElement = a + b
        a = b
        b = nextElement
    
    return arr

def factorial(numberTo):
    if numberTo == 0: 
        return 1
    return numberTo * factorial(numberTo - 1)

if __name__ == '__main__':
    
    result = fibonacci(1)

    print('result', result)
    
    print('factorial', factorial(5))
    