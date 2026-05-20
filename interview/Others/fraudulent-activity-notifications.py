   
def activityNotifications(expenditure, d):
    # Write your code here
    notification = 0
    sortedArray = []
    toRemove, toAdd = 0, 0
    for i in range(len(expenditure)):
        if i-d >= 0:
            if len(sortedArray) == 0:
                sortedArray = sorted(expenditure[0:i])
            else:
                print("sortedArray:", i, toAdd, sortedArray, toRemove)
                sortedArray = getSortedArray(sortedArray, toRemove, toAdd)
            toRemove = expenditure[i-d]
            toAdd = expenditure[i]
            
            median = getMedian(sortedArray)
            if expenditure[i] >= median*2:
                notification += 1
            # print("[" + str(i) + "]:", expenditure[i], ", m:",median, ", ", expenditure[i],">=", median*2)
        
    return notification
    
    
def getSortedArray(array, toRemove, toAdd):
    array.remove(toRemove)
    i = 0
    while i < len(array) and toAdd > array[i]:
        i += 1

    array.insert(i, toAdd)
    return array

def getMedian(array):
    median = 0        
    if len(array) % 2 == 0:
        median = (array[len(array)//2 - 1] + array[len(array)//2]) / 2
    else:
        median = array[len(array)//2]
    return median

if __name__ == '__main__':
    tr = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    days = 5
    
    tr = [1,2,3,4,4]
    days = 4
    
    # tr = [10,20,30,40,50]
    # days = 3

    # tr = [2,4,8,16,32,64,128,256]
    # days = 1
    tr = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
    days = 3
    
    print("tr:", tr, ", days:", days)
    result = activityNotifications(tr, days)
    
    print("result:", result)