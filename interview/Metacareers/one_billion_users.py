# https://www.metacareers.com/profile/coding_practice_question/?problem_id=951929261870357&c=1880764319019914&psid=275492097255885&practice_plan=0&b=0011022


# Add any helper functions you may need here


def getBillionUsersDay(growthRates):
  # Write your code here
  maxUsers = 1000000000
  
  currentUsers = 0
  days = 1
  cummulativePerGrowRate = [1] * len(growthRates)
  
  while currentUsers < maxUsers:
    for i in range(len(growthRates)):
      cummulativePerGrowRate[i] *= growthRates[i]
      currentUsers += cummulativePerGrowRate[i] 

    days += 1
  print('days:', days, ', cumulative:', currentUsers)

  return days


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
  test_0 = [1.5]
  expected_0 = 52
  output_0 = getBillionUsersDay(test_0)
  check(expected_0, output_0)
  
  test_1 = [1.1, 1.2, 1.3]
  expected_1 = 79
  output_1 = getBillionUsersDay(test_1)
  check(expected_1, output_1)

  test_2 = [1.01, 1.02]
  expected_2 = 1047
  output_2 = getBillionUsersDay(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  