class Solution:
    def trap(self, height: List[int]) -> int:
        # using O(n) time and space, using leftMax and rightMax arrays
        n = len(height)
        leftMax, rightMax = 0, 0
        leftMaxArr = [0] * n
        rightMaxArr = [0] * n

        for i in range(len(height)):
            j = -i -1
            leftMaxArr[i] = leftMax
            rightMaxArr[j] = rightMax
            leftMax = max(leftMax, height[i])
            rightMax = max(rightMax, height[j])

        water = 0
        for i in range(len(height)):
            pot = min(leftMaxArr[i], rightMaxArr[i])
            if pot > height[i]:
                water += pot - height[i]

        return water