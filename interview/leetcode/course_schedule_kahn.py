from collections import deque 

def findCoursesOrder(courses: map):
    if len(courses) == 0:
        return []
    
    order = []
    q = deque()
    dependencies = {}
    for c in courses.keys():
        dependencies[c] = 0
        for dep in courses[c]:
            if c in dependencies:
                dependencies[c] = dependencies[c] + 1
             
    
    # Add to the Q courses with 0 dependencies
    for c in dependencies.keys():
        if dependencies[c] == 0:
            q.append(c)

    print(dependencies)

    while len(q) > 0:
        nodependencies = q.popleft()
        order.append(nodependencies)
        for kcourse in courses.keys():
            if nodependencies in courses[kcourse] :
                dependencies[kcourse] = dependencies[kcourse]-1
                if dependencies[kcourse] == 0:
                    q.append(kcourse)
        
    for d in dependencies:
        if dependencies[d] > 0:
            return []
    
    return order


if __name__ == '__main__':
    adjacentMatrix = {0:[], 1:[0], 2:[0], 3:[1,2]}
    obtained = findCoursesOrder(adjacentMatrix)
    expected = [0,1,2,3]
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

    adjacentMatrix = {0:[], 1:[2], 2:[1], 3:[1,2]}
    obtained = findCoursesOrder(adjacentMatrix)
    expected = []
    print("Got:", obtained, ", expected:", expected, ", Correct:", obtained == expected)

'''
Course Schedule II
There are numCourses courses labeled 0 to numCourses-1. You are given an array prerequisites where prerequisites[i] = [a, b] means you must take course b before course a. Return a valid course ordering as an array. If it is impossible to finish all courses (due to a cycle), return an empty array []. This is a classic application of topological sort — used in build systems, dependency resolvers, and schedulers.
SIGNATURE
function findOrder(numCourses: number, prerequisites: number[][]): number[]
Constraints
1 ≤ numCourses ≤ 2,000
0 ≤ prerequisites.length ≤ 5,000
prerequisites[i].length === 2
0 ≤ a, b < numCourses, a ≠ b
No duplicate prerequisite pairs
Expected time complexity: O(V + E)
Examples
Test Cases
#	Input	Expected Output
1	(2, [[1,0]])	[0,1]
2	(1, [])	[0]
3	(3, [[1,0],[2,1]])	[0,1,2]
4	(3, [[0,1],[0,2],[1,2]])	[2,1,0]
5	(2, [[0,1],[1,0]])	[] (cycle)
6	(4, [[1,0],[2,0],[3,1],[3,2]])	[0,1,2,3] or equivalent
▼ Hide Hint
💡 Build an adjacency list + in-degree array. Use Kahn's algorithm (BFS) or DFS with coloring (white/gray/black). If processed count < numCourses, a cycle exists.
'''