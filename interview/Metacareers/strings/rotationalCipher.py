import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input_str, rotation_factor):
  LEN_LETTERS = ord('Z') - ord('A') + 1
  LEN_NUMBERS = 10
  cyphered = ""
  
  for i in range(len(input_str)):
    newChar =''
    upperCase, lowerCase, number = False, False, False
    difference = 0
    effective_rotation_factor = 0
    
    if input_str[i] >= 'A' and input_str[i] <= 'Z':
      upperCase = True
      difference = (ord('Z') - ord(input_str[i]))
      effective_rotation_factor = rotation_factor % LEN_LETTERS
      
    if input_str[i] >= 'a' and input_str[i] <= 'z':
      lowerCase = True
      difference = (ord('z') - ord(input_str[i]))
      effective_rotation_factor = rotation_factor % LEN_LETTERS
      
    if input_str[i] >= '0' and input_str[i] <= '9':
      number = True
      difference = (ord('9') - ord(input_str[i]))
      effective_rotation_factor = rotation_factor % LEN_NUMBERS
      
    
    if upperCase or lowerCase or number:      
      if difference < effective_rotation_factor:
        effective_rotation_factor = effective_rotation_factor - difference
        if upperCase:
          newChar = chr(ord('A') + effective_rotation_factor -1)
        if lowerCase:
          newChar = chr(ord('a') + effective_rotation_factor -1)
        if number:
          newChar = chr(ord('0') + effective_rotation_factor -1) 
      else:
        newChar = chr(ord(input_str[i]) + effective_rotation_factor)
    else:   
      newChar = input_str[i]
      
    cyphered += newChar
          
  # Write your code here
  return cyphered



# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  input_3 = "abcdefghijklmNOPQRSTUVWXYZ0123456789"
  rotation_factor_3 = 39
  expected_3 = "nopqrstuvwxyzABCDEFGHIJKLM9012345678"
  output_3 = rotationalCipher(input_3, rotation_factor_3)
  check(expected_3, output_3)
  