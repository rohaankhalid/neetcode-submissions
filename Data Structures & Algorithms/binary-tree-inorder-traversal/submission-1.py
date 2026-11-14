# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
def inorder(root):
    in not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    in not root:
        return root
    postorder(root.left)
    postorder(root.right)
    print(root.val)

def reverseorder(root):
    if not root:
        return root
    reverseorder(root.right)
    print(root.val)
    reverseorder(root.left)
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return root
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res

