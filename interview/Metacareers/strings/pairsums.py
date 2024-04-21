import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def numberOfWays(arr, k):
   # Write your code here
  return numberOfWays2(arr, k)


def numberOfWays1(arr, k):
  numways = 0
  
  for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
      if arr[i] + arr[j] == k:
        numways += 1

  return numways

def numberOfWays2(arr, tsum):
  occurrences = {}
  numways = 0
  
  for i in range(len(arr)):
    if arr[i] in occurrences:
      occurrences[arr[i]] += 1
    else:
      occurrences[arr[i]] = 1
      
  for k, v in occurrences.items():
    if (tsum - k) in occurrences:
      if k == tsum//2:
        times = 0
        for i in range(1, v):
          times += i
        numways += times
      else:  
        times = occurrences[tsum-k]
        numways += v * times
      occurrences[tsum-k] = 0
      occurrences[k] = 0

  return numways



# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  k_1 = 6
  arr_1 = [1, 2, 3, 4, 3]
  expected_1 = 2
  output_1 = numberOfWays(arr_1, k_1)
  check(expected_1, output_1)

  k_2 = 6
  arr_2 = [1, 5, 3, 3, 3]
  expected_2 = 4
  output_2 = numberOfWays(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  