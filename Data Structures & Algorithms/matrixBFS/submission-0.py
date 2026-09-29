class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0,0))
        visit.add((0,0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr,dc in neighbors:
                    row, col = r + dr, c + dc
                    if (row < 0 or col < 0 or
                        row == ROWS or col == COLS or
                        (row, col) in visit or
                        grid[row][col] == 1):
                        continue

                    queue.append((row,col))
                    visit.add((row,col))

            length += 1

        return -1