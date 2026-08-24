# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = float("-inf")
        def dfs(root): 
            nonlocal global_max
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)
            if root.val + left + right > global_max:
                global_max = root.val + left + right
            return root.val + max(left, right)
        dfs(root)
        return global_max