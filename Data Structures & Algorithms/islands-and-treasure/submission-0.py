class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        def bfs(r,c):
            q = collections.deque()
            visit = set()
            q.append((r,c, 0))
            visit.add((r,c))

            dist = 0
            while q:
                row, col, dist = q.popleft()
                # if tresure chest reached, return dist and update
                if grid[row][col] == 0:
                    return dist

                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    newRow, newCol = row + dr, col + dc

                    if (newRow in range(ROWS) and
                        newCol in range(COLS) and
                        grid[newRow][newCol] != -1 and
                        (newRow, newCol) not in visit
                        ):
                        visit.add((newRow,newCol))
                        q.append((newRow,newCol,dist + 1))

            return INF


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i,j)