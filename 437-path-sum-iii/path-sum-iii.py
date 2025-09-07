# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return 0

        def dfs(node,s):
            if not node:
                return 0
            s+=node.val
            count=1 if s==targetSum else 0

            count+=dfs(node.left,s)
            count+=dfs(node.right,s)
            return count
        return dfs(root,0)+self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum)