class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k-1])
        L, R = 0, k - 1

        for L in range(len(arr) - k + 1):
            curSum += arr[R]
            if (curSum / k) >= threshold:
                res += 1
            curSum -= arr[L]
            R += 1
        
        return res