# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # if we reverse the second half of linked list, then we can have tow linked lists
        # iterate over them and adding the two values, as they are twins of each other after reversal

        # find middle, slwo will be starting of middle for second hald of linkedlist
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next        

        # reverse the second hald of linkedlist
        prev, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # iterate over two linkedlists and add corresponding values
        res = 0
        first, second = head, prev
        while second:
            res = max(res, first.val + second.val)
            first, second = first.next, second.next

        return res
