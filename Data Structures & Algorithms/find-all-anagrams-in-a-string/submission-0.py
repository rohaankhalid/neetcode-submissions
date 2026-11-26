from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        countsP = Counter(p)
        output = []
        windowMap = Counter(s[:len(p)])

        L, R = 0, len(p) - 1
        while R < len(s):
            if windowMap == countsP:
                output.append(L)

            R += 1
            if R == len(s):
                break
            windowMap[s[R]] = 1 + windowMap.get(s[R], 0)
            windowMap[s[L]] -= 1
            L += 1

        return output

"""
have a fixed window of size p, L and R
create Counter for str p
pass the window over s
for each window:
    run a hashmap
    if hasmap == Counter:
        add index to output
"""
