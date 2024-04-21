import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
  # Write your code here
  return matching_pairs_2(s, t)
  
  
def matching_pairs_1(s, t):
  # inneficient
  matchingPairs = 0
  list_s = list(s)
  
  for i in range(len(s)-1):
    for j in range(i+1, len(s)):
      tmp = list_s[i]
      list_s[i] = list_s[j]
      list_s[j] = tmp
      matching = 0
      for k in range(len(s)):
        if list_s[k] == t[k]:
          matching += 1
          
      if matching > matchingPairs:
        matchingPairs = matching
      
      list_s[j] = list_s[i]
      list_s[i] = tmp

  return matchingPairs


def matching_pairs_2(s, t):
  matchingPairs = 0
  minimum_matchingPairs = 0
  list_indexes_not_matching = []
  
  for i in range(len(s)):
    if s[i] == t[i]:
      minimum_matchingPairs += 1
    else:
      list_indexes_not_matching.append(i)
  
  if minimum_matchingPairs == len(s):
    minimum_matchingPairs -= 2
  elif minimum_matchingPairs == len(s)-1:
    minimum_matchingPairs -= 1
    
  additional_matching_pair = 0
  for i in range(len(list_indexes_not_matching)):
    for j in range(i+1, len(list_indexes_not_matching)):
      if s[list_indexes_not_matching[i]] == t[list_indexes_not_matching[j]] and s[list_indexes_not_matching[j]] == t[list_indexes_not_matching[i]]:
        minimum_matchingPairs += 2
        break
      elif s[list_indexes_not_matching[i]] == t[list_indexes_not_matching[j]] or s[list_indexes_not_matching[j]] == t[list_indexes_not_matching[i]]:
        additional_matching_pair = 1

  matchingPairs = minimum_matchingPairs + additional_matching_pair 
  return matchingPairs

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
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  