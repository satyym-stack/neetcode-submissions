# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {}
        for i in range(len(inorder)):
            in_map[inorder[i]] = i
        pre_index = 0
        def boundary(left, right):
            nonlocal pre_index
            if left > right:
                return None
            root = TreeNode(preorder[pre_index])
            pre_index += 1
            root_index = in_map[root.val]
            root.left = boundary(left, root_index - 1)
            root.right = boundary(root_index + 1, right)
            return root
        
        return boundary(0, len(inorder) - 1)

        