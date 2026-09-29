class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def isEmpty(self) -> bool:
        if self.left.next == self.right:
            return True
        return False

    def append(self, value: int) -> None:
        node = ListNode(value)
        before, after = self.right.prev, self.right
        before.next = node
        node.prev = before
        node.next = after
        after.prev = node

    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        before, after = self.left, self.left.next
        before.next = node
        node.prev = before
        node.next = after
        after.prev = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        lastNode = self.right.prev
        value = lastNode.val
        prevNode = lastNode.prev

        prevNode.next = self.right
        self.right.prev = prevNode

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        firstNode = self.left.next
        value = firstNode.val
        nextNode = firstNode.next

        self.left.next = nextNode
        nextNode.prev = self.left

        return value
