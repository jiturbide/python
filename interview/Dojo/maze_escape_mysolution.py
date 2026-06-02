from collections import deque

def min_steps_to_escape(grid):
    # Solve edge cases
    if len(grid) == 0 or len(grid[0]) == 0:
        return -1
    
    # Find start, end cells
    rows = len(grid)
    cols = len(grid[0])
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r,c)
            if grid[r][c] == 'E':
                end = (r,c)
    
    if start == None or end == None:
        return -1
    
    # Prepare visited, queue, directions, path variables
    queue:deque = deque()
    queue.append((start[0], start[1], 0)) #j,j,steps
    visited = set()
    visited.add((start[0], start[1]))
    directions = [(-1,0), (0,-1), (0,1),(1,0)]
    
    # Traverse
    while len(queue) > 0:
        # Pop next element to analyze
        cy, cx, steps = queue.popleft()
        # If found return steps number
        if (cy, cx) == end:
            return steps
        
        # Get possible elements from the current cell, add to the Q
        for y, x in directions:
            ny = cy + y
            nx = cx + x
            if ny >= 0 and ny < rows and nx >= 0 and nx < cols: #within grid
                if grid[ny][nx] != 'X':                          #not an obstacle
                    if (ny, nx) not in visited:                 #not analyzed/visited
                        queue.append((ny, nx, steps+1))
                        visited.add((ny,nx))                    
    
    # Return -1 if path not found
    return -1


# Run tests
if __name__ == "__main__":
    test_grid = [
        ['S', '.', 'X', '.'],
        ['.', '.', 'X', '.'],
        ['.', '.', '.', 'E'],
        ['X', 'X', '.', '.']
    ]
    result = min_steps_to_escape(test_grid)
    expected = 5
    print(f"Minimum steps: {result}, expected: {expected}" )

    test_grid = [
        ['S', '.', 'X'],
        ['X', 'X', '.'],
        ['.', '.', 'E']
    ]
    # Expected Output: -1
    result = min_steps_to_escape(test_grid)
    expected = -1
    print(f"Minimum steps: {result}, expected: {expected}" )