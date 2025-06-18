# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        ino=[]
        ino+=self.inorderTraversal(root.left)
        ino.append(root.val)
        ino+=self.inorderTraversal(root.right)
        return ino
