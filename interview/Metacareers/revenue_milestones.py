# https://www.metacareers.com/profile/coding_practice_question/?problem_id=192049171861831&c=1880764319019914&psid=275492097255885&practice_plan=0&b=0011022


def getMilestoneDays(revenues, milestones):
  # Write your code here
  days = []
  sortedMilestones = []
  for i in range(len(milestones)):
    sortedMilestones.append([milestones[i], i+1, -1])
  
  sortedMilestones.sort(key= lambda m : m[0])
  
  currIdxMilestone = 0
  currentSum = 0
  for i in range(len(revenues)):
    currentSum += revenues[i]
    while currIdxMilestone < len(sortedMilestones) and currentSum >= sortedMilestones[currIdxMilestone][0]:
      sortedMilestones[currIdxMilestone][2] = i + 1
      currIdxMilestone += 1
      
    if currIdxMilestone == len(milestones):
      break
  
  sortedMilestones.sort(key= lambda m: m[1])
    
  for i in range(len(sortedMilestones)):
      days.append(sortedMilestones[i][2])
  
  return days
  
  
  
  

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  revenues_0 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
  milestones_0 = [100, 200, 500, 2000]
  expected_0 = [4, 6, 10, -1]
  output_0 = getMilestoneDays(revenues_0, milestones_0)
  check(expected_0, output_0)
  
  revenues_1 = [100, 200, 300, 400, 500]
  milestones_1 = [300, 800, 1000, 1400]
  expected_1 = [2, 4, 4, 5]
  output_1 = getMilestoneDays(revenues_1, milestones_1)
  check(expected_1, output_1)

  revenues_2 = [700, 800, 600, 400, 600, 700]
  milestones_2 = [3100, 2200, 800, 2100, 1000] 
  expected_2 = [5, 4, 2, 3, 2]
  output_2 = getMilestoneDays(revenues_2, milestones_2)
  check(expected_2, output_2)

  # Add your own test cases here
  