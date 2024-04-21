def getOptimizedRoute(maxTravelDist, forwardRoute, returnRoute):
    pairsList = []
    pairsDistanceList = []
    forwardRoute.sort(key=lambda route: route[1])
    returnRoute.sort(key=lambda route: route[1])

    currentMaximumTravel = 0
    for i in reversed(range(len(forwardRoute))):
        for j in range(len(returnRoute)):
            sumTravelDistance = forwardRoute[i][1] + returnRoute[j][1]
            if sumTravelDistance <= maxTravelDist:
                if sumTravelDistance >= currentMaximumTravel:
                    currentMaximumTravel = sumTravelDistance
                    pairsDistanceList.append([forwardRoute[i][0], returnRoute[j][0], sumTravelDistance])
    
    pairsDistanceList.sort(key= lambda pair: pair[2], reverse=True)
    for i in range(len(pairsDistanceList)):
        if pairsDistanceList[i][2] < currentMaximumTravel:
            break
        pairsList.append([pairsDistanceList[i][0], pairsDistanceList[i][1]])
    
    return pairsList

def sortRoute(): 
    pass

if __name__ == "__main__":
    
    maxTravelDist = 10000
    forwardRoute = [[4,10000], [1,3000], [2,5000], [3,7000]]
    returnRouteList = [[1,2000], [2,3000], [3,4000], [4,5000]]

    result = getOptimizedRoute(maxTravelDist, forwardRoute, returnRouteList)
    # Output: [[2,4], [3,2]]
    print("result 1:", result)


    maxTravelDist = 7000
    forwardRoute = [[2,4000], [1,2000], [3,6000]]
    returnRoute = [[1,2000]]
    # Output: [[2,1]]
    result = getOptimizedRoute(maxTravelDist, forwardRoute, returnRoute)
    print("result 2:", result)

    maxTravelDist = 20
    forwardRoute = [[1,8], [2,7], [3,14]]
    returnRoute = [[1,5], [2,10], [3,14]]
    # Output: [[3, 1]]
    result = getOptimizedRoute(maxTravelDist, forwardRoute, returnRoute)
    print("result 3:", result)


    maxTravelDist = 20
    forwardRoute = [[1,8], [2,15], [3,9]]
    returnRoute = [[1,8], [2,11], [3,12]]
    # Output: [[1,3], [3,2]]
    result = getOptimizedRoute(maxTravelDist, forwardRoute, returnRoute)
    print("result 4:", result)


    '''
    Amazon Prime Air is developing a system that divides shipping routes using flight optimization routing systems to a cluster of aircrafts that can fulfill these routes. Each shipping route is identified by a unique integer identifier, requires a fixed non-zero amount of travel distance between airports, and is defined to be either a forward shipping route or a return shipping route. Identifiers are guaranteed to be unique within their own route type, but not across route types.

    Each aircraft should be assigned two shipping routes at once one forward route and one return route. Due to the complex scheduling of flight plans, all aircraft have a fixed maximum operating travel distance, and cannot be scheduled to fly a shipping route that requires more travel distance than the prescribed maximum operating travel distance. The goal of the system is to optimize the total operating travel distance of given airfcraft. A forward/return shipping route pair is considered to be 'optimal' if there does not exist another pair that has a higer operating travel distance than this pair, and also has a total less than or equal to the maximum operating travel distance of the aircraft.

    For example, if the aircraft has a maximum operating travel distance of 3000 miles, a forward/return shipping route pair using a total of 2900 miles would be optimal if there does not exist a pair that uses a total operating travel distance of 3000 miles, but would not be considered optimal if such a pair did exist.

    Your task is to write an algorithm to optimize the sets of forward/return shipping route pairs that allow the aircraft to be optimally utilized, given a list of forward shipping routes and a list of return shipping routes.

    Input:
    The input to the function/method consists of threee arguments:
    maxTravelDist, an integer representing the maximum operating travel distance of the given aircraft.
    forwardRouteList, a list of pairs of integers where the first integer represents the unique identifier of a forward shipping route and the second integer represents the amount of travel distance required by this shipping route.
    returnRouteList, a list of pairs of integers where the first integer represents the unique identifier of a return shipping route and the second integer represents the amount of travel distance required by this shipping route.
    OutputReturn a list of pairs of integers representing the pairs of IDs of forward and return shipping routes that optimally utilize the given aircraft if no route is possible, return an empty list.

    Examples
    Example1
    Input:
    maxTravelDist = 7000
    forwardRoute = [[1,2000], [2,4000], [3,6000]]
    return routeList = [1,2000]
    Output:
    [[2,1]]
    Explanation:
    There are only 3 combinations [1,1], [2,1] and [3,1], which have a total of 4000, 6000 and 8000 miles, respectively. Since 6000 is the largest use that does not exceed 7000, [2,1] is the only optimal pair.  

    Example2
    Input:
    maxTravelDist = 10000
    forwardRouteList = [[1,3000], [2,5000], [3,7000], [4,10000]]
    returnRouteList = [[1,2000], [2,3000], [3,4000], [4,5000]]

    Output:
    [[2,4], [3,2]]

    Explanation:
    There are two pair of forward and return shipping routes possible that optimally utilizes the given aircraft.
    Shipping Route ID#2 from the forwardShippingRouteList requires 5000 miles traveled, and Shipping Route ID#4 from returnShippingRouteList also requires 5000 miles travelled. Combined they add up to 1000 miles travled.
    Similarly, Shipping Route ID#3 from forwardShippingRouteList requires 7000 miles travelled, and Shipping Route ID#2 from returnShippingRouteList requires 3000 miles travelled. There also add up to 10000 miles travelled.
    There fore the pairs of forward and return shiping routes that optimally utilize aircraft are [2,4] and [3,2].

    List<List<Integer>>

    ---------------
    Testcase 1:
    Input:
    20
    [[1,8], [2,7], [3,14]],
    [[1,5], [2,10], [3,14]]
    Expected Return value:
    3 1

    Testcase 2:
    Input:
    20,
    [[1,8], [2,15], [3,9]],
    [[1,8], [2,11], [3,12]]
    Expected return value:
    1 3
    3 2
    '''