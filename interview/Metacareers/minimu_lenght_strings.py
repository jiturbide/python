# https://www.metacareers.com/profile/coding_practice_question/?problem_id=2237975393164055&c=1880764319019914&psid=275492097255885&practice_plan=0&b=0011022


# Add any helper functions you may need here

def min_length_substring(s, t):
  # Write your code here
  minimumLenght = -1
  
  # count all required characters in a map
  requiredCharacters = {}
  for i in range(len(t)):
    if t[i] in requiredCharacters:
      requiredCharacters[t[i]] += 1
    else: 
      requiredCharacters[t[i]] = 1
  
  # Look for all elements of the substring
  for i in range(len(s)):
    if s[i] in requiredCharacters:
      mapCharacters = requiredCharacters.copy()
      charactersLeft = calculateCharactersLeft(mapCharacters)
      for j in range(i, len(s)):
        cchar = s[j]
        if cchar in mapCharacters:
          if mapCharacters[cchar] > 0:
            mapCharacters[cchar] -= 1
        
          charactersLeft = calculateCharactersLeft(mapCharacters)
        
          if charactersLeft == 0:
            # done
            lenght = j - i + 1
            if minimumLenght == -1 or (minimumLenght != -1 and lenght < minimumLenght):
                minimumLenght = lenght
            break 
      #end for
      if charactersLeft != 0:
        break
    
  return minimumLenght

def calculateCharactersLeft(mapCharacters):
    charactersCount = 0
    for k, v in mapCharacters.items():
        charactersCount += v       

    return charactersCount

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
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  