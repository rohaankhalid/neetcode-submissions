class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        def bfs(grid, r, c, visit):
            ROWS, COLS = len(grid), len(grid[0])
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))

            length = 0
            while q:
                for i in range(len(q)):
                    row, col = q.popleft()
                    if row == ROWS - 1 and col == COLS - 1:
                        return length

                    directions = [[0,1], [0,-1], [1,0], [-1,0]]
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if (r < 0 or c < 0 or r == ROWS or c == COLS or
                            grid[r][c] == 1 or (r,c) in visit):
                            continue
                        q.append((r,c))
                        visit.add((r,c))
                length += 1

            return -1

        return bfs(grid, 0, 0, set())