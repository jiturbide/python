import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(n, ar):
    # Write your code here
    socksCounting = {}
    pairs = 0
    for item in ar:
        if item in socksCounting:
            socksCounting[item] += 1
        else:
            socksCounting[item] = 1
    
    for k in socksCounting:
        pairs += socksCounting[k]//2
        
    return pairs

if __name__ == '__main__':
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sockMerchant(ar.count, ar)
    print('Pairs', result)