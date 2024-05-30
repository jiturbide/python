# 


def escape(cols, rows, maze):
    route = []
    target = [rows-1, cols-1]
    
    currentCell = [0,0]
    while True:
        options = getNextPossibleCells(cols, rows, currentCell, maze, route)
        if len(options) != 0:
            # Chose the first option
            route.append(currentCell)
            print(route)
            currentCell = options[0]
            if currentCell == target:
                route.append(currentCell)
                break
        else:
            # mark current cell as an invalid option
            maze[currentCell[0]][currentCell[1]] = 2
            if len(route) != 0:
                currentCell = route.pop()
            else:
                break
    
    return route

def getNextPossibleCells(c, r, currentCell, maze, route):
    nextCells = []
    # Check next cells marked with 0
    # Do not consider what it is in the stack
    nx = currentCell[1] + 1
    ny = currentCell[0]
    if validNextCell(nx, ny, c, r, maze, route):
        nextCells.append([ny, nx])
    nx = currentCell[1]
    ny = currentCell[0] + 1
    if validNextCell(nx, ny, c, r, maze, route):
        nextCells.append([ny, nx])
    nx = currentCell[1] - 1
    ny = currentCell[0]
    if validNextCell(nx, ny, c, r, maze, route):
        nextCells.append([ny, nx])
    nx = currentCell[1]
    ny = currentCell[0] - 1
    if validNextCell(nx, ny, c, r, maze, route):
        nextCells.append([ny, nx])

    return nextCells

def validNextCell(x, y, c, r, maze, route):
    inRoute = False
    if len(route) > 0 and [y,x] == route[len(route)-1]:
        inRoute = True
    xg0 = x >= 0
    xmc = x < c
    yg0 = y >= 0
    ymr = y < r
    if xg0 and xmc and yg0 and ymr and inRoute == False and maze[y][x] == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    maze = [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
           [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
           [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
           [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]]
    cols, rows = 10, 6
    # exit is [cols-1, rows-1] [5,9]
    route = escape(cols, rows, maze)
    print("Route:", route)