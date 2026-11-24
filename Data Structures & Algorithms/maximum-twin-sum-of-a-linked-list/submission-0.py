# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        maxSum = 0
        for i in range(len(arr) // 2):
            j = -i -1
            maxSum = max(maxSum, arr[i] + arr[j])

        return maxSum

'''
store the linkedlist vals in an arr
iterate over half of linkedlist:
    have i pointer going forward
    j going backward
    add arr[i] and arr[j]
    compare w maxSum
'''