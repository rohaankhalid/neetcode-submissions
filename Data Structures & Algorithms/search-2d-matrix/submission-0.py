class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        ROWS, COLS = len(matrix), len(matrix[0])

        # 1. Vertical binary search to find the correct row
        top = 0
        bottom = ROWS - 1
        targetRow = -1

        while top <= bottom:
            midRow = (top + bottom) // 2

            # check if target falls within the boundaries of the middle row
            if matrix[midRow][0] <= target <= matrix[midRow][COLS - 1]:
                targetRow = midRow
                break
            elif target < matrix[midRow][0]:
                # target is smaller than row's start, discard this row and below
                bottom = midRow - 1
            else:
                # targetis larger than the row's end, discard this row and all above
                top = midRow + 1

        # if the vertical search didnt find a valid row container, the targer isnt in the matrix
        if targetRow == -1:
            return False

        # 2. horizontal binary search on the identified row
        row = matrix[targetRow]
        left = 0
        right = COLS - 1

        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
