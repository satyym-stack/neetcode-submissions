# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = 0
        def in_order(current):
            nonlocal count
            nonlocal answer
            if current == None:
                return 
            in_order(current.left)
            count += 1
            if count == k:
                answer = current.val
            in_order(current.right)

        in_order(root)
        return answer