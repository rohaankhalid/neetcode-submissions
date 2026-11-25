from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # i can use a counter and then return most_common integer
        counts = Counter(nums)

        return counts.most_common(1)[0][0]