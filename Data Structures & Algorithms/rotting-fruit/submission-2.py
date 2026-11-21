class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))

        minutes = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        grid[nr][nc] == 0 or
                        grid[nr][nc] == 2):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = 2
            minutes += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return max(0, minutes - 1)
