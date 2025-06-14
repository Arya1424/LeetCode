# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        pre=[]
        pre.append(root.val)
        pre+=self.preorderTraversal(root.left)
        pre+=self.preorderTraversal(root.right)

        return pre