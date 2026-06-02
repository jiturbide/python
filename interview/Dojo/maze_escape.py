from collections import deque

def min_steps_to_escape(grid):
    # Edge case: Empty grid
    if not grid or not grid[0]:
        return -1
        
    ROWS, COLS = len(grid), len(grid[0])
    start = None
    
    # 1. Find the starting position ('S')
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 'S':
                start = (r, c)
                break
        if start:
            break
            
    if not start:
        return -1 # 'S' not found in grid
        
    # 2. Initialize BFS queue and visited set
    # Queue stores: (row, col, current_steps)
    queue = deque([(start[0], start[1], 0)])
    visited = {start}
    
    # Define the 4 possible movement directions: Up, Down, Left, Right
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 3. Standard BFS loop
    while queue:
        r, c, steps = queue.popleft()
        
        # If we reached the exit, return the steps immediately
        if grid[r][c] == 'E':
            return steps
            
        # Explore neighbors
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            
            # Check bounds and constraints
            if 0 <= nr < ROWS and 0 <= nc < COLS: # Within grid
                if grid[nr][nc] != 'X':           # Not an obstacle
                    if (nr, nc) not in visited:   # Not visited yet
                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))
                        
    # If the queue is empty and 'E' wasn't reached, it's impossible
    return -1

# --- Test Execution ---
if __name__ == "__main__":
    test_grid = [
        ['S', '.', 'X', '.'],
        ['.', '.', 'X', '.'],
        ['.', '.', '.', 'E'],
        ['X', 'X', '.', '.']
    ]
    print(f"Minimum steps: {min_steps_to_escape(test_grid)}") # Output: 5

'''
Preparing for a FAANG-level interview requires mastering grid-based graph traversal, as these companies love testing your ability to optimize pathfinding under constraints.Here are two distinct, high-quality matrix escape challenges designed to match the progression of difficulty you'll face in a technical screen: a Medium-level BFS/Shortest Path problem, and a Hard-level Bitmask/State Tracking problem.Challenge 1: The Guarded Labyrinth (Medium)This challenge tests your foundational knowledge of Breadth-First Search (BFS) and finding the shortest path in an unweighted grid while handling obstacles.DescriptionYou are trapped in a 2D grid room of size $M \times N$. You start at a position marked 'S' (Start) and need to reach the exit marked 'E' (Exit).Empty spaces you can walk through are marked as '.'.Obstacles you cannot pass through are marked as 'X'.You can move in four directions: Up, Down, Left, or Right.Return the minimum number of steps required to reach the exit. If it is impossible to reach the exit, return -1.Sample Input & OutputInput Grid:Plaintext[
  ['S', '.', 'X', '.'],
  ['.', '.', 'X', '.'],
  ['.', '.', '.', 'E'],
  ['X', 'X', '.', '.']
]
Output: 5Explanation: One shortest path is $(0,0) \rightarrow (1,0) \rightarrow (2,0) \rightarrow (2,1) \rightarrow (2,2) \rightarrow (2,3)$, which takes 5 steps.Test DataPythongrid = [
    ['S', 'X', '.', '.'],
    ['.', 'X', '.', 'X'],
    ['.', '.', '.', 'E'],
    ['X', '.', 'X', '.']
]
# Expected Output: 5

grid_impossible = [
    ['S', '.', 'X'],
    ['X', 'X', '.'],
    ['.', '.', 'E']
]
# Expected Output: -1
HintsWhy BFS over DFS? Since all moves have an equal weight of 1, BFS guarantees that the first time you visit the exit 'E', you have found the absolute shortest path. DFS could find a longer path first and waste time.State Tracking: To avoid infinite loops, maintain a visited set or boolean matrix to track coordinates (row, col) you have already processed.Queue Structure: Your BFS queue should store elements as (row, col, current_steps).Challenge 2: The Multi-Key Vault (Hard)FAANG interviewers love to take a standard problem and add a "state" twist. This challenge introduces inventory management into your grid traversal.DescriptionYou are in a locked matrix room of size $M \times N$. You start at 'S' and must reach 'E'. However, the room contains several locked doors represented by uppercase letters ('A', 'B', 'C'). To pass through a door, you must first pick up its corresponding lowercase key ('a', 'b', 'c') located somewhere in the grid.'.': Walkable floor.'X': Permanent obstacle.'a' - 'f': Keys (up to 6 unique keys).'A' - 'F': Doors.You can pick up a key by stepping on it. You can hold multiple keys at once. You can revisit cells.Return the minimum steps to reach the exit with any combination of keys, or -1 if unreachable.Sample Input & OutputInput Grid:Plaintext[
  ['S', '.', 'A'],
  ['X', 'X', '.'],
  ['a', '.', 'E']
]
Output: 6Explanation: You cannot go right immediately because door 'A' is locked. You must go down to $(2,0)$ to pick up key 'a'. Now that you hold 'a', you can retrace your steps, unlock door 'A' at $(0,2)$, and walk down to 'E'. Path: $(0,0) \rightarrow (1,0) \rightarrow (2,0) \rightarrow (1,0) \rightarrow (0,0) \rightarrow (0,1) \rightarrow (0,2) \rightarrow (1,2) \rightarrow (2,2)$. Total steps = 8? Wait, a shorter path is $(0,0) \rightarrow (1,0) \rightarrow (2,0) \rightarrow (2,1) \rightarrow (2,2)$ which bypasses the door entirely! Total steps = 4.(Note: Always look for alternative paths! If the path through the door was required, it would look like the hint scenario below).Test DataPythongrid = [
    ['S', 'b', 'B'],
    ['X', 'X', 'A'],
    ['E', 'a', '.']
]
# Expected Output: 10
# Path: Get 'b' -> Get 'a' (passing 'b') -> open 'A' -> open 'B' -> reach 'E'
HintsThe Trap: If your visited array only tracks (row, col), you will fail. You need to revisit the same cell multiple times if your inventory of keys has changed.Bitmasking: Because there are at most 6 keys, you can represent your key inventory as a 6-bit integer (e.g., 000011 means you have keys 'a' and 'b').New State Space: Modify your visited tracking to include the key state: (row, col, key_mask). Your BFS queue will now store (row, col, key_mask, steps).Which of these two paradigms would you like to practice implementing first, and would you like to write the solution in Python, Java, or C++?
'''

    
'''    
Step-by-Step Explanation
FAANG interviewers look for a structured breakdown. When explaining this solution, walk through these three phases:

Locating the Source: We scan the 2D matrix using a nested loop to find the coordinates of 'S'. This gives us our entry point into the graph.

The "Wavefront" Expansion (BFS): We use a Queue (collections.deque in Python for efficient O(1) pops) to explore the grid level by level. Think of it like a ripple in water expanding outward.

Dead-End & Obstacle Prevention: * visited Set: Crucial to prevent spinning in circles. Once we queue a coordinate, we flag it so we never evaluate it again.

In-Bounds Check: 0 <= nr < ROWS and 0 <= nc < COLS prevents Python from throwing an IndexError.

Wall Check: grid[nr][nc] != 'X' effectively treats walls as non-existent edges in our graph.

Complexity Analysis
An interviewer will always ask for this. Be ready to state it confidently:

Time Complexity: O(M×N)
In the worst-case scenario, we might visit every single cell in the grid exactly once. For a grid of size M×N, checking neighbors takes constant O(1) time, leading to a linear time complexity relative to the number of cells.

Space Complexity: O(M×N)
The space is dominated by the visited hash set and the queue. In a wide-open grid with no obstacles, both the queue and the visited set could store up to a significant fraction of the total cells, bounded by M×N.

Would you like to move on to the solution for Challenge 2 (The Multi-Key Vault), or would you like to explore how to optimize this first solution to use In-Place Modification (to achieve O(1) auxiliary space)?
'''