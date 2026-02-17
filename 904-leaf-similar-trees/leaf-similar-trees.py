# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(arr, root):
            if not root:
                return
            if not root.left and not root.right:
                arr.append(root.val)
            else:
                dfs(arr, root.left)
                dfs(arr, root.right)
        one, two=[], []
        dfs(one, root1)       
        dfs(two, root2)
        return one==two