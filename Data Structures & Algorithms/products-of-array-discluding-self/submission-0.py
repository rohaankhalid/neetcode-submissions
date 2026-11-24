class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd, postProd = 1, 1
        prefix, postfix = [], []

        for i in range(len(nums)):
            j = -i -1

            preProd *= nums[i]
            postProd *= nums[j]

            prefix.append(preProd)
            postfix.append(postProd)

        # reverse postfix
        postfix.reverse()

        # to handle edge case (boundaries): insert 1 for prefix at start, append 1 for postfix at end
        prefix.insert(0, 1)
        postfix.append((1))

        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * postfix[i + 1])

        return output




"""
[1,2,4,6]
prefix = [1,2,8,48]
postfix = [48,48,24,6]

now for output, take product of prefix[i-1] and postfix[i+1]
"""