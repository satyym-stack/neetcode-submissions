# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkValid(current, lower, upper):
            if not current:
                return True
            if not (lower < current.val < upper):
                return False
            return (checkValid(current.left, lower, current.val) and 
                    checkValid(current.right, current.val, upper))

        return checkValid(root, float("-inf"), float("inf"))
        