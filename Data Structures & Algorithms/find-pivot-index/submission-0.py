class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        preSum, postSum = 0, 0
        prefix, postfix = [], []

        for i in range(len(nums)):
            j = -i -1

            preSum += nums[i]
            postSum += nums[j]

            prefix.append(preSum)
            postfix.insert(0, postSum)

        for i in range(len(nums)):
            if prefix[i] == postfix[i]:
                return i
        
        return -1


"""
[1,7,3,6,5,6]
prefix = [1,8,11,17,22,28]
postfix = [28,27,20,17,11,6]

# create prefix and postfix arrays
# use i to iterate over, the index at which prefix[i] == postfix[i] : return i
# else return -1

# edge case
[2,1,-1]
prefix = [2,3,2]
postfix = [2,0,-1]
""" 

