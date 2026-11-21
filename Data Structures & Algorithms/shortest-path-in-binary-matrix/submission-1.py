class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        directions = [[0,1], [0,-1], [1,0], [-1,0], 
                        [-1,1], [1,1], [1,-1], [-1,-1]]

        q = collections.deque()
        visit = set()
        
        q.append((0,0,1))
        visit.add((0,0))

        while q:
            r, c, length = q.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (0 <= row < ROWS and 0 <= col < COLS and
                    (row, col) not in visit and grid[row][col] != 1):
                    q.append((row, col, length + 1))
                    visit.add((row, col))

        return -1
 



