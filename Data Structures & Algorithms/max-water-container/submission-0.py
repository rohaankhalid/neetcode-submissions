class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # O(n) two pointer solution
        # L at start, R at end, moving any will reduce width hence area
        # decision: move pointer which has smaller height of the two, to maximize area
        # keep calculating area

        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            length = r - l
            height = min(heights[l], heights[r])
            curArea = length * height

            maxArea = max(maxArea, curArea)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea