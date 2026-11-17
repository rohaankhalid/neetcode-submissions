class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        initialColor = image[sr][sc]

        if color == initialColor:
            return image

        ROWS, COLS = len(image), len(image[0])

        def dfs(r, c):

            # base case to stop dfs
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                image[r][c] != initialColor):
                return

            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image


            