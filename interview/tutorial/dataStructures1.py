from collections import deque

# Data structures 

def fun(arr):
    return arr

if __name__ == '__main__':
    arr = [7, 1, 3, 2, 4, 5, 6]
    result = arr.sort()
    print(arr)
    print('result', result)
    
    # Operations with arrays
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    print('fruits', fruits)
    print('len(fruits):', len(fruits))
    print('fruits.count(apple):', fruits.count('apple'))
    print('fruits.index(apple)', fruits.index('apple'))
    
    fruits2 = fruits.copy() #deep copy
    fruits2.insert(2, 'watermelon')
    fruits2.remove('apple')
    fruits2.sort()
    print('fruits:', id(fruits), fruits)
    print('fruits2.sort:', id(fruits2), fruits2)
    
    # Delete elements
    del fruits2[len(fruits)-1]
    print('del fruits2:', fruits2)
    
    last = fruits2.pop()
    print('fruits2.pop():', last)
    
    fruits.reverse()
    print('fruits.reverse():', fruits)
    
    # Stacks queues
    stack = [3,5,7,9]
    stack.pop()
    stack.append(8)
    print('stack:', stack)
    
    queue = deque(['Eric', 'John', 'Michael'])
    print('queue:', queue)
    queue.append('Terry')
    queue.append("Graham")
    element = queue.popleft()
    print('popleft:', element, "len:", len(queue))
    
    # print("deque([]).popleft():", deque([]).popleft())
    
    # list comprenhension
    squares = []
    for x in range(10):
        squares.append(x*x)
    print('squares 1:', squares)
    
    squares = [x**2 for x in range(10)]
    print('squares 2:', squares)
    
    squares = list(range(10))
    squares = list(map(lambda x: x**2, range(10)))
    print('squares 3:', squares)
    
    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    print([x.strip() for x in freshfruit])
    
    print([(x, x**2) for x in range (1,9)])
    
    vec = [[1,2,3], [4,5,6], [7,8,9]]
    flat = [num for row in vec for num in row] 
    print(flat)
    matx = []
    for i in range(3):
        row = []
        for j in range (3):
            row.append(flat[i*3+j])
        matx.append(row)
    print('matx', matx)
            
    # del
    a = [-1, 1, 66.25, 333, 333, 1234.5, 100.0, 333.0]
    del a[0]
    del a[2:3]
    print(a)
    del a[3:]
    print(a)
    del a[:]
    print ("a", a)
    
    # tuples
    t = 1975, "Luis", "MX"
    print("t", t, "len:", len(t))
    # t2 = t.c
    arr = [t]
    print("arr", arr)
    t2 = t, (1974, "Miriam", "MX")
    print("t2", t2, "t2[0]:", t2[0], "t2[1]:", t2[1], "t2[1][1]:", t2[1][1])
    # t2[1][1] = "Lorena"
    mutable = [(1,2,3), (4,5,6)]
    mutable.append((6,7,8))
    del mutable[1]
    print('Mutable:', mutable)
    print("mutable[1][0]:", mutable[1][0])
    
    emptyTuple = ()
    tulpleOneElement = ("Luis")
    tulpleOneElement = ("Luis",)
    print("tulpleOneElement", tulpleOneElement, len(tulpleOneElement))
    
    year, name, country = t
    print('year, name, country', year, name, country)
    
    # print([].pop())
    
    a = [1,2,1]
    b = [1,2]
    
    print('Compare list', b == a)
    