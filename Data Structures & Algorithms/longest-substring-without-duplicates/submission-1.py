class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        window hashset, store characters in the current window
        curLength
        maxLength
        add char in position R to window
        if char at position R already in window, 
            run while loop (until that char at R is not in window anymore)
            remove char at L, increment L
        if char at position R not in window
            add to window
            increase length by 1

        TODO: updating maxLength, and keeping track of curr length
        outsude the while loop, update the curLength by R - L + 1
        """

        window = set()
        curLen = 0
        maxLen = float('-inf')
        L = 0

        for R in range(len(s)):
            if s[R] in window:
                while s[R] in window:
                    window.remove(s[L])
                    L += 1
                window.add(s[R])
                curLen = R - L + 1
            else:
                window.add(s[R])
                curLen += 1
            maxLen = max(maxLen, curLen)

        return 0 if maxLen == float('-inf') else maxLen
